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

if 'trade_setup' not in st.session_state:
    st.session_state['trade_setup'] = None

st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

# --- DESIGN "QUANTUM DARK" V48 ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #020202; color: white; }
        .main-title { text-align: center; letter-spacing: 15px; font-weight: 100; font-size: 32px; margin-top: 20px; }
        .sub-title { text-align: center; color: #FF3131; font-size: 9px; margin-top: -15px; letter-spacing: 5px; font-weight: bold;}
        .res-box { background: #080808; padding: 30px; border-radius: 20px; border: 1px solid #1a1a1a; margin: 20px 0; }
        .risk-gauge { border-radius: 10px; padding: 10px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>QUANTUM RISK ENGINE V48.0</div>", unsafe_allow_html=True)

# --- ASSETS & SMT ---
assets = {
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "XAG (SILVER)", "anchor": "DXY 1H"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY 1H", "anchor": "DXY 1H"},
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETH", "anchor": "DXY 1H"}
}

target_label = st.selectbox("SÉLECTION ACTIF", list(assets.keys()), label_visibility="collapsed")
c = assets[target_label]

uploaded_files = st.file_uploader("DXY 1H + ASSET 5M + BOOKMAP FLOW", accept_multiple_files=True)

def get_quantum_analysis(files, asset_name, smt, anchor):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        ANALYSTE DE RISQUE QUANTITATIF.
        Analyse la confluence : {anchor} -> {asset_name} -> {smt} -> Bookmap Flow.
        
        CRITÈRES DE CONFIANCE (0-100) :
        - Alignement Narratif DXY 1H.
        - Présence de divergence SMT.
        - Confirmation Order Flow (Delta/Absorption).
        
        RÉPONDS UNIQUEMENT EN JSON :
        {{
            "side": "BUY", 
            "confidence": 92, 
            "risk_recommendation": "High Conviction - Max Risk",
            "reason": "..."
        }}
        SI CONFIDENCE < 75%: {{"side": "NEUTRAL", "confidence": 50, "reason": "Manque de confluence"}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "confidence": 0, "reason": "Scan impossible."}

if uploaded_files:
    if st.button("🚀 EXECUTE QUANTUM SCAN"):
        with st.status("🧠 ÉVALUATION DU RISQUE...") as status:
            ticker = yf.Ticker(c['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            res = get_quantum_analysis(uploaded_files, target_label, c['smt'], c['anchor'])
            
            if res['side'] in ["BUY", "SELL"]:
                is_fx = "USD=X" in c['symbol']
                sl_dist = price * 0.0008 if is_fx else price * 0.004
                m = 1 if res['side'] == "BUY" else -1
                
                st.session_state['trade_setup'] = {
                    "side": res['side'], "entry": price,
                    "tp": price + (sl_dist * 4.5 * m),
                    "sl": price - (sl_dist * m),
                    "conf": res['confidence'], "risk": res.get('risk_recommendation', 'Standard'),
                    "reason": res['reason']
                }
            else:
                st.session_state['trade_setup'] = {"side": "NEUTRAL", "reason": res['reason'], "conf": res['confidence']}
            status.update(label="ANALYSE QUANTIQUE TERMINÉE", state="complete")

# --- AFFICHAGE DU SETUP ---
setup = st.session_state.get('trade_setup')

if setup:
    if setup['side'] == "NEUTRAL":
        st.markdown(f'<div class="res-box" style="text-align:center;">⚖️ {setup["side"]} ({setup["conf"]}%)<br><small>{setup["reason"]}</small></div>', unsafe_allow_html=True)
    else:
        color = "#00FF66" if setup['side'] == "BUY" else "#FF3131"
        risk_color = "#00FF66" if setup['conf'] > 90 else "#FFA500"
        
        st.markdown(f"""
            <div class="res-box">
                <div class="risk-gauge" style="background: {risk_color}22; color: {risk_color}; border-color: {risk_color};">
                    SCORE DE CONFIANCE : {setup['conf']}% | {setup['risk']}
                </div>
                <h1 style="text-align:center; color:{color}; font-size:60px; margin:0;">{setup['side']}</h1>
                <p style="text-align:center; font-size:12px; opacity:0.8; margin-top:10px;">{setup['reason']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        fmt = ".5f" if "USD=X" in c['symbol'] else ".2f"
        st.metric("ENTRÉE", f"{setup['entry']:{fmt}}")
        c1, c2 = st.columns(2)
        c1.success(f"TP (4.5R)\n\n{setup['tp']:{fmt}}")
        c2.error(f"SL (PROTECTION)\n\n{setup['sl']:{fmt}}")

    if st.button("🔄 RESET"):
        st.session_state['trade_setup'] = None
        st.rerun()
