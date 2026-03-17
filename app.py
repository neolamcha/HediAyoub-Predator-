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

# --- DESIGN TACTIQUE V42 ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .sub-title { text-align: center; color: #FF3131; font-size: 10px; margin-top: -15px; letter-spacing: 3px; font-weight: bold;}
        .res-box { background: #0a0a0a; padding: 20px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 10px 0; }
        .smt-info { background: rgba(255, 49, 49, 0.1); border-left: 3px solid #FF3131; padding: 10px; font-size: 11px; margin-bottom: 20px; border-radius: 0 10px 10px 0; }
        
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
            transition: 0.3s;
        }
    </style>
""", unsafe_allow_html=True)

if 'trade_setup' not in st.session_state:
    st.session_state.trade_setup = None

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>NEURAL PREDATOR V42.0</div>", unsafe_allow_html=True)

# Configuration des actifs et de leur SMT corrélé
assets = {
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETHEREUM (ETH)"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "DOW JONES (YM)"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "NASDAQ (NQ)"},
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "DXY (DOLLAR INDEX)"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY (DOLLAR INDEX)"}
}

target_label = st.selectbox("ACTIF", list(assets.keys()), label_visibility="collapsed")
current_asset = assets[target_label]

# Affichage dynamique du rappel SMT et Timeframe
st.markdown(f"""
    <div class="smt-info">
        📌 <b>RAPPEL OPÉRATIONNEL</b><br>
        🔄 <b>SMT :</b> Cherche la divergence avec <b>{current_asset['smt']}</b><br>
        ⏱️ <b>TIMEFRAMES :</b> Structure en <b>15M</b> | Entrée en <b>5M</b>
    </div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader("CHARGE TES 6 DATASETS", accept_multiple_files=True)

def get_neural_analysis(files, asset_name, smt_asset):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        Analyse institutionnelle pour {asset_name}. 
        Structure demandée : 15M (Trend/OB) et 5M (Entrée/CHoCH).
        SMT : Compare avec {smt_asset} pour détecter les divergences de liquidité.
        
        Réponds uniquement en JSON: {{"side": "BUY", "reason": "Détail technique court"}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "reason": "Analyse de structure en cours..."}

if uploaded_files:
    if st.button("EXECUTE NEURAL SCAN"):
        with st.status("📡 SYNCHRONISATION NEURALE...") as status:
            ticker = yf.Ticker(current_asset['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            verdict = get_neural_analysis(uploaded_files, target_label, current_asset['smt'])
            
            # Logique de calcul dynamique 1:3
            is_fx = "USD=X" in current_asset['symbol']
            sl_dist = price * 0.0012 if is_fx else price * 0.006
            side_mult = 1 if verdict['side'] == "BUY" else -1
            
            st.session_state.trade_setup = {
                "side": verdict['side'],
                "entry": price,
                "tp": price + (sl_dist * 3.5 * side_mult),
                "sl": price - (sl_dist * side_mult),
                "reason": verdict['reason']
            }
            status.update(label="SCAN TERMINÉ", state="complete")

if st.session_state.trade_setup:
    t = st.session_state.trade_setup
    color = "#00FF66" if t['side'] == "BUY" else "#FF3131"
    fmt = ".5f" if "USD=X" in current_asset['symbol'] else ".2f"
    
    st.markdown(f"""
        <div class="res-box">
            <h1 style="text-align:center; color:{color}; font-size:50px; margin:0;">{t['side']}</h1>
            <p style="text-align:center; font-size:12px; opacity:0.8;">{t['reason']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.metric("ENTRÉE LIVE", f"{t['entry']:{fmt}}")
    c1, c2 = st.columns(2)
    c1.success(f"TARGET (TP)\n\n{t['tp']:{fmt}}")
    c2.error(f"PROTECTION (SL)\n\n{t['sl']:{fmt}}")
    
    if st.button("🔄 RESET"):
        st.session_state.trade_setup = None
        st.rerun()
