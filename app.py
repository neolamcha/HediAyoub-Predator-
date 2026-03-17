import streamlit as st
import yfinance as yf
import google.generativeai as genai
import PIL.Image
import json
import re
from datetime import datetime
import pytz

# --- CONFIGURATION API ---
GENAI_API_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg" 
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialisation sécurisée
if 'trade_setup' not in st.session_state:
    st.session_state['trade_setup'] = None

st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

# --- LOGIQUE DE TIMING OPÉRATIONNEL (NY TIME) ---
def get_market_advice():
    tz_ny = pytz.timezone('America/New_York')
    now_ny = datetime.now(tz_ny)
    hour = now_ny.hour
    
    if 2 <= hour < 5:
        return "🕒 LONDRES OPEN : Focus EURUSD & GOLD. Cherche SMT sur DXY Index."
    elif 8 <= hour < 10:
        return "🕒 NY PRE-MARKET : Focus NASDAQ & US30. Surveille divergence ES (S&P500)."
    elif 10 <= hour < 12:
        return "🔥 SILVER BULLET / NY OPEN : Haute volatilité NQ/GOLD. Cherche le Judas Swing."
    elif 13 <= hour < 16:
        return "🕒 NY PM SESSION : Focus BTC & Indices. Attention au Power of 3 (PO3)."
    else:
        return "🌙 ASIA SESSION : Volatilité faible. Focus BTC ou prépare la session de Londres."

advice = get_market_advice()

# --- DESIGN UI PREMIUM ---
st.markdown(f"""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {{visibility: hidden !important;}}
        .stApp {{ background-color: #050505; color: white; }}
        
        .ticker-wrapper {{
            width: 100%; overflow: hidden; background: #800000; 
            border-bottom: 2px solid #ff0000; padding: 8px 0;
            position: fixed; top: 0; left: 0; z-index: 999;
        }}
        .ticker-text {{
            display: inline-block; white-space: nowrap;
            padding-left: 100%; animation: ticker 30s linear infinite;
            font-family: 'Courier New', monospace; font-size: 13px; color: white; font-weight: bold;
        }}
        @keyframes ticker {{
            0% {{ transform: translate(0, 0); }}
            100% {{ transform: translate(-100%, 0); }}
        }}
        .main-title {{ text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 60px; }}
        .sub-title {{ text-align: center; color: #FF3131; font-size: 10px; margin-top: -15px; letter-spacing: 3px; font-weight: bold;}}
        .res-box {{ background: #0a0a0a; padding: 25px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 15px 0; }}
        
        div.stButton > button {{
            background: linear-gradient(90deg, #800000 0%, #ff0000 100%) !important;
            color: white !important; font-size: 18px !important; font-weight: bold !important;
            letter-spacing: 4px !important; padding: 18px !important; border-radius: 12px !important;
            box-shadow: 0 0 30px rgba(255, 0, 0, 0.4) !important; width: 100%; border: none !important;
        }}
    </style>
""", unsafe_allow_html=True)

# Bandeau de timing
st.markdown(f'<div class="ticker-wrapper"><div class="ticker-text">🚀 INSTRUCTION : {advice} ——— ANALYSEUR SMT ACTIF ——— DXY 1H NARRATIVE ——— HEDI AYOUB QUANTUM V52</div></div>', unsafe_allow_html=True)

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>QUANTUM PREDATOR V52.0</div>", unsafe_allow_html=True)

# --- ASSETS ---
assets = {
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "SILVER (XAG)", "anchor": "DXY 1H"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "S&P 500 (ES)", "anchor": "DXY 1H"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "S&P 500 (ES)", "anchor": "DXY 1H"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY Index", "anchor": "DXY 1H"},
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETH", "anchor": "DXY 1H"}
}

target_label = st.selectbox("CHOISIR L'ACTIF À SCANNER", list(assets.keys()))
c = assets[target_label]

st.info(f"🎯 STRATÉGIE : {target_label} vs {c['smt']} | Anchor : {c['anchor']}")

uploaded_files = st.file_uploader("UPLOAD DATASETS (DXY 1H, ASSET M15/M5, BOOKMAP)", accept_multiple_files=True)

# --- FONCTION D'ANALYSE ---
def get_quantum_analysis(files, asset_name, smt, anchor):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        ANALYSTE SMC/ORDERFLOW. Actif: {asset_name}. SMT: {smt}. Anchor: {anchor}.
        Vérifie l'heure actuelle (Session Killzone).
        Si setup clair (SMT + Flow confirmation), donne BUY ou SELL. Sinon NEUTRAL.
        Réponds en JSON : {{"side": "BUY", "conf": 92, "reason": "...", "flow": "..."}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "reason": "Erreur d'analyse visuelle."}

# --- LE BOUTON EST ICI ---
if uploaded_files:
    if st.button("🔥 EXECUTE QUANTUM SCAN"):
        with st.status("📡 ANALYSE DES FLUX EN COURS...") as status:
            ticker = yf.Ticker(c['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            res = get_quantum_analysis(uploaded_files, target_label, c['smt'], c['anchor'])
            
            if res.get('side') in ["BUY", "SELL"]:
                is_fx = "USD=X" in c['symbol']
                sl_dist = price * 0.0010 if is_fx else price * 0.005
                m = 1 if res['side'] == "BUY" else -1
                st.session_state['trade_setup'] = {
                    "side": res['side'], "entry": price,
                    "tp": price + (sl_dist * 4.2 * m),
                    "sl": price - (sl_dist * m),
                    "reason": res['reason'], "conf": res.get('conf', 0), "flow": res.get('flow', 'N/A')
                }
            else:
                st.session_state['trade_setup'] = {"side": "NEUTRAL", "reason": res['reason']}
            status.update(label="ANALYSE TERMINÉE", state="complete")

# --- AFFICHAGE RÉSULTATS ---
setup = st.session_state.get('trade_setup')
if setup:
    if setup['side'] == "NEUTRAL":
        st.markdown(f'<div class="res-box" style="text-align:center;">⚖️ {setup["side"]}<br><small>{setup["reason"]}</small></div>', unsafe_allow_html=True)
    else:
        color = "#00FF66" if setup['side'] == "BUY" else "#FF3131"
        fmt = ".5f" if "USD=X" in c['symbol'] else ".2f"
        st.markdown(f"""
            <div class="res-box">
                <div style="text-align:right; font-size:10px; color:#00FF66;">CONFIANCE: {setup['conf']}%</div>
                <h1 style="text-align:center; color:{color}; font-size:55px; margin:0;">{setup['side']}</h1>
                <p style="text-align:center; font-size:12px; margin-top:10px;">{setup['reason']}</p>
            </div>
        """, unsafe_allow_html=True)
        st.metric("PRIX D'ENTRÉE", f"{setup['entry']:{fmt}}")
        c1, c2 = st.columns(2)
        c1.success(f"TP\n\n{setup['tp']:{fmt}}")
        c2.error(f"SL\n\n{setup['sl']:{fmt}}")
    
    if st.button("🔄 RESET"):
        st.session_state['trade_setup'] = None
        st.rerun()
