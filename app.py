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

# --- INITIALISATION SÉCURISÉE DU SESSION STATE ---
if 'trade_setup' not in st.session_state:
    st.session_state['trade_setup'] = None

st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

# --- DESIGN INSTITUTIONNEL ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .sub-title { text-align: center; color: #FF3131; font-size: 10px; margin-top: -15px; letter-spacing: 3px; font-weight: bold;}
        .res-box { background: #0a0a0a; padding: 25px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 15px 0; }
        .smt-pill { background: #111; border: 1px solid #FF3131; color: #FF3131; padding: 5px 10px; border-radius: 5px; font-size: 9px; font-weight: bold; margin-right: 5px; }
        
        div.stButton > button {
            background: linear-gradient(90deg, #600000 0%, #ff0000 100%) !important;
            color: white !important;
            border: none !important;
            font-size: 16px !important;
            font-weight: bold !important;
            letter-spacing: 3px !important;
            padding: 18px !important;
            border-radius: 12px !important;
            box-shadow: 0 10px 30px rgba(255, 0, 0, 0.3) !important;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>TOP-DOWN NARRATIVE V46.0</div>", unsafe_allow_html=True)

# Configuration Actifs avec ta logique SMT
assets = {
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "XAG (SILVER)", "anchor": "DXY 1H"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY 1H", "anchor": "DXY 1H"},
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETH", "anchor": "DXY 1H"}
}

target_label = st.selectbox("SÉLECTION ACTIF", list(assets.keys()), label_visibility="collapsed")
c = assets[target_label]

st.markdown(f"""
    <div style='margin-bottom: 20px; text-align: center;'>
        <span class="smt-pill">SMT: {c['smt']}</span>
        <span class="smt-pill">ANCHOR: {c['anchor']}</span>
    </div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader("DATASETS (DXY 1H + ASSET 15M/5M)", accept_multiple_files=True)

def get_institutional_analysis(files, asset_name, smt, anchor):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        EXPERT SMC/ICT NARRATIVE.
        1. Analyse le DXY en 1H pour le biais global.
        2. Analyse {asset_name} en 15M/5M.
        3. Cherche la divergence SMT avec {smt}.
        4. Si le DXY 1H est baissier et que {asset_name} fait un CHoCH 5M haussier avec SMT, c'est un BUY.
        
        SI LE SETUP EST VALIDE, RÉPONDS EN JSON :
        {{"side": "BUY", "bias": "BEARISH DXY", "reason": "...", "confidence": 98}}
        SINON : {{"side": "NEUTRAL", "reason": "Désalignement Narratif/SMT"}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "reason": "Erreur de lecture du narratif."}

if uploaded_files:
    if st.button("🔥 EXECUTE TOP-DOWN SCAN"):
        with st.status("📡 ANALYSE DU NARRATIF INSTITUTIONNEL...") as status:
            ticker = yf.Ticker(c['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            res = get_institutional_analysis(uploaded_files, target_label, c['smt'], c['anchor'])
            
            if res['side'] in ["BUY", "SELL"]:
                is_fx = "USD=X" in c['symbol']
                sl_dist = price * 0.0010 if is_fx else price * 0.005
                m = 1 if res['side'] == "BUY" else -1
                
                st.session_state['trade_setup'] = {
                    "side": res['side'], "entry": price,
                    "tp": price + (sl_dist * 4.2 * m),
                    "sl": price - (sl_dist * m),
                    "reason": res['reason'], "bias": res.get('bias', 'N/A')
                }
            else:
                st.session_state['trade_setup'] = {"side": "NEUTRAL", "reason": res['reason']}
            status.update(label="ANALYSE TERMINÉE", state="complete")

# --- AFFICHAGE SÉCURISÉ (PLUS D'ATTRIBUTE ERROR) ---
current_setup = st.session_state.get('trade_setup')

if current_setup:
    if current_setup['side'] == "NEUTRAL":
        st.markdown(f"""
            <div class="res-box" style="text-align:center; border: 1px dashed #333;">
                <h3 style="color:#555;">⚖️ NEUTRAL</h3>
                <p style="font-size:11px; opacity:0.6;">{current_setup['reason']}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        color = "#00FF66" if current_setup['side'] == "BUY" else "#FF3131"
        fmt = ".5f" if "USD=X" in c['symbol'] else ".2f"
        st.markdown(f"""
            <div class="res-box">
                <div style="display:flex; justify-content:space-between; font-size:10px; opacity:0.5;">
                    <span>BIAIS HTF: {current_setup['bias']}</span>
                    <span>TIMEFRAME: M5/M15/H1</span>
                </div>
                <h1 style="text-align:center; color:{color}; font-size:55px; margin:10px 0;">{current_setup['side']}</h1>
                <p style="text-align:center; font-size:12px;">"{current_setup['reason']}"</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.metric("PRIX D'ENTRÉE", f"{current_setup['entry']:{fmt}}")
        c1, c2 = st.columns(2)
        c1.success(f"🎯 TARGET (TP)\n\n{current_setup['tp']:{fmt}}")
        c2.error(f"📍 PROTECTION (SL)\n\n{current_setup['sl']:{fmt}}")
    
    if st.button("🔄 RESET ENGINE"):
        st.session_state['trade_setup'] = None
        st.rerun()
