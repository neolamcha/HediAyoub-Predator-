import streamlit as st
import yfinance as yf
import google.generativeai as genai
import PIL.Image
import json
import re

# --- CONFIGURATION API ---
GENAI_API_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg" 
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

# --- DESIGN TACTIQUE V45 ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .sub-title { text-align: center; color: #FF3131; font-size: 10px; margin-top: -15px; letter-spacing: 3px; font-weight: bold;}
        .res-box { background: #0a0a0a; padding: 25px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 15px 0; }
        .config-pill { background: #111; border: 1px solid #333; padding: 8px 15px; border-radius: 8px; font-size: 10px; color: #aaa; margin: 5px; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>TOP-DOWN NARRATIVE V45.0</div>", unsafe_allow_html=True)

# --- CONFIGURATION SMT & TIMEFRANES ---
assets = {
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETH", "anchor": "DXY 1H"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "XAG (SILVER)", "anchor": "DXY 1H"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY 1H", "anchor": "DXY 1H"}
}

target_label = st.selectbox("ACTIF", list(assets.keys()), label_visibility="collapsed")
c = assets[target_label]

# Interface de rappel des timeframes
cols = st.columns(3)
cols[0].markdown(f"<div class='config-pill'>🌐 ANCHOR: {c['anchor']}</div>", unsafe_allow_html=True)
cols[1].markdown(f"<div class='config-pill'>🔄 SMT: {c['smt']}</div>", unsafe_allow_html=True)
cols[2].markdown(f"<div class='config-pill'>⏱️ ENTRY: 5M / 15M</div>", unsafe_allow_html=True)

uploaded_files = st.file_uploader("CHARGE TES DATASETS (DXY 1H + ACTIF 15M/5M)", accept_multiple_files=True)

def get_top_down_analysis(files, asset_name, smt, anchor):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        ANALYSE TOP-DOWN INSTITUTIONNELLE.
        1. Regarde le graphique DXY en 1H : Quel est le biais directionnel (Narratif HTF) ?
        2. Regarde l'actif {asset_name} en 15M : La structure est-elle alignée avec le DXY ?
        3. Cherche la divergence SMT avec {smt}.
        4. Identifie l'entrée précise en 5M (CHoCH / FVG / Liquidity Sweep).

        SI TOUS LES TIMEFRAMES SONT ALIGNÉS, RÉPONDS EN JSON :
        {{"side": "BUY", "bias": "BULLISH", "reason": "Détail du narratif 1H vs 5M", "conf": 98}}
        SINON : {{"side": "NEUTRAL", "reason": "Désalignement DXY 1H / Actif 5M", "conf": 0}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "reason": "Analyse du narratif HTF impossible."}

if uploaded_files:
    if st.button("🔥 EXECUTE TOP-DOWN SCAN"):
        with st.status("📡 ANALYSE DU NARRATIF 1H...") as status:
            ticker = yf.Ticker(c['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            res = get_top_down_analysis(uploaded_files, target_label, c['smt'], c['anchor'])
            
            if res['side'] in ["BUY", "SELL"]:
                is_fx = "USD=X" in c['symbol']
                sl_dist = price * 0.0010 if is_fx else price * 0.005
                m = 1 if res['side'] == "BUY" else -1
                
                st.session_state.trade_setup = {
                    "side": res['side'], "entry": price,
                    "tp": price + (sl_dist * 4.2 * m), # Ratio augmenté car narratif HTF
                    "sl": price - (sl_dist * m),
                    "reason": res['reason'], "bias": res.get('bias', 'N/A')
                }
            else:
                st.session_state.trade_setup = {"side": "NEUTRAL", "reason": res['reason']}
            status.update(label="STRATÉGIE VALIDÉE", state="complete")

if st.session_state.trade_setup:
    t = st.session_state.trade_setup
    if t['side'] == "NEUTRAL":
        st.markdown(f'<div class="res-box" style="text-align:center; color:#666;">⚖️ {t["side"]}<br><small>{t["reason"]}</small></div>', unsafe_allow_html=True)
    else:
        color = "#00FF66" if t['side'] == "BUY" else "#FF3131"
        fmt = ".5f" if "USD=X" in c['symbol'] else ".2f"
        st.markdown(f"""
            <div class="res-box">
                <div style="display:flex; justify-content:space-between; font-size:10px; opacity:0.5;">
                    <span>BIAIS HTF: {t['bias']}</span>
                    <span>TIMEFRAME: M5/M15</span>
                </div>
                <h1 style="text-align:center; color:{color}; font-size:55px; margin:10px 0;">{t['side']}</h1>
                <p style="text-align:center; font-size:12px; font-style:italic;">"{t['reason']}"</p>
            </div>
        """, unsafe_allow_html=True)
        st.metric("ENTRÉE MARCHÉ", f"{t['entry']:{fmt}}")
        c1, c2 = st.columns(2)
        c1.success(f"🎯 TP (Liquidity Target)\n\n{t['tp']:{fmt}}")
        c2.error(f"📍 SL (Invalidation)\n\n{t['sl']:{fmt}}")
    
    if st.button("🔄 NOUVEAU CYCLE"):
        st.session_state.trade_setup = None
        st.rerun()
