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

# Initialisation sécurisée pour éviter l'erreur de ta capture
if 'trade_setup' not in st.session_state:
    st.session_state['trade_setup'] = None

st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

# --- DESIGN TACTIQUE PREMIUM ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .sub-title { text-align: center; color: #FF3131; font-size: 10px; margin-top: -15px; letter-spacing: 3px; font-weight: bold;}
        .res-box { background: #0a0a0a; padding: 25px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 15px 0; }
        .smt-info { background: rgba(255, 49, 49, 0.1); border-left: 3px solid #FF3131; padding: 12px; font-size: 11px; margin-bottom: 20px; border-radius: 0 10px 10px 0; }
        
        div.stButton > button {
            background: linear-gradient(90deg, #800000 0%, #ff0000 100%) !important;
            color: white !important;
            border: none !important;
            font-size: 18px !important;
            font-weight: bold !important;
            letter-spacing: 4px !important;
            padding: 15px !important;
            border-radius: 12px !important;
            box-shadow: 0 0 25px rgba(255, 0, 0, 0.5) !important;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>NEURAL PREDATOR V49.0</div>", unsafe_allow_html=True)

# Configuration complète des actifs avec SMT et Timeframe
assets = {
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "SILVER (XAG)", "anchor": "DXY 1H"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "S&P 500 (ES)", "anchor": "DXY 1H"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "S&P 500 (ES)", "anchor": "DXY 1H"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY Index", "anchor": "DXY 1H"},
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETHEREUM (ETH)", "anchor": "DXY 1H"}
}

target_label = st.selectbox("ACTIF", list(assets.keys()), label_visibility="collapsed")
c = assets[target_label]

# Retour du bloc de rappel opérationnel que tu voulais
st.markdown(f"""
    <div class="smt-info">
        📌 <b>LOGIQUE INSTITUTIONNELLE</b><br>
        🔄 <b>SMT :</b> Divergence vs <b>{c['smt']}</b> | <b>Anchor :</b> {c['anchor']}<br>
        ⏱️ <b>TIMEFRAMES :</b> Biais 1H | Structure 15M | Entrée 5M
    </div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader("CHARGE TES 6 DATASETS (DXY 1H + ASSET 15M/5M + BOOKMAP)", accept_multiple_files=True)

def get_full_analysis(files, asset_name, smt, anchor):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        Analyse institutionnelle lorde pour {asset_name}.
        1. Vérifie le DXY 1H ({anchor}).
        2. Détecte la divergence SMT avec {smt}.
        3. Analyse l'Order Flow sur Bookmap (Delta/Absorption).
        4. Valide l'entrée en 5M.

        Réponds en JSON :
        {{"side": "BUY", "conf": 95, "reason": "...", "flow": "Absorption Achat"}}
        SI DOUTE: {{"side": "NEUTRAL", "conf": 0, "reason": "Désalignement SMT/DXY"}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "conf": 0, "reason": "Erreur de synchronisation neurale."}

if uploaded_files:
    if st.button("🔥 EXECUTE NEURAL QUANT SCAN"):
        with st.status("📡 SYNCHRONISATION DES FLUX...") as status:
            ticker = yf.Ticker(c['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            res = get_full_analysis(uploaded_files, target_label, c['smt'], c['anchor'])
            
            if res['side'] in ["BUY", "SELL"]:
                is_fx = "USD=X" in c['symbol']
                sl_dist = price * 0.0010 if is_fx else price * 0.005
                m = 1 if res['side'] == "BUY" else -1
                
                st.session_state['trade_setup'] = {
                    "side": res['side'], "entry": price,
                    "tp": price + (sl_dist * 4.2 * m),
                    "sl": price - (sl_dist * m),
                    "reason": res['reason'], "conf": res['conf'], "flow": res.get('flow', 'N/A')
                }
            else:
                st.session_state['trade_setup'] = {"side": "NEUTRAL", "reason": res['reason'], "conf": res['conf']}
            status.update(label="SCAN TERMINÉ", state="complete")

# Affichage sécurisé
setup = st.session_state.get('trade_setup')

if setup:
    if setup['side'] == "NEUTRAL":
        st.markdown(f'<div class="res-box" style="text-align:center; opacity:0.6;">⚖️ {setup["side"]}<br><small>{setup["reason"]}</small></div>', unsafe_allow_html=True)
    else:
        color = "#00FF66" if setup['side'] == "BUY" else "#FF3131"
        fmt = ".5f" if "USD=X" in c['symbol'] else ".2f"
        st.markdown(f"""
            <div class="res-box">
                <div style="text-align:right; font-size:10px; color:#00FF66;">CONFIDENCE: {setup['conf']}%</div>
                <h1 style="text-align:center; color:{color}; font-size:55px; margin:0;">{setup['side']}</h1>
                <p style="text-align:center; font-size:12px; margin-top:10px;">{setup['reason']}</p>
                <div style="background:rgba(255,255,255,0.05); padding:5px; border-radius:5px; font-size:9px; text-align:center; margin-top:10px;">FLOW: {setup['flow']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.metric("ENTRÉE LIVE", f"{setup['entry']:{fmt}}")
        c1, c2 = st.columns(2)
        c1.success(f"TARGET (TP)\n\n{setup['tp']:{fmt}}")
        c2.error(f"PROTECTION (SL)\n\n{setup['sl']:{fmt}}")

    if st.button("🔄 RESET"):
        st.session_state['trade_setup'] = None
        st.rerun()
