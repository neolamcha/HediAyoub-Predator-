import streamlit as st
import time
import random

# 1. NETTOYAGE RADICAL DE L'INTERFACE
st.set_page_config(page_title="HEDI AYOUB", layout="centered")

st.markdown("""
    <style>
        /* Masquer les éléments techniques Streamlit & GitHub */
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        .stDeployButton {display:none !important;}
        div[data-testid="stToolbar"] {display: none !important;}
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400;900&display=swap');
        .stApp { background-color: #030608; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .block-container { padding-top: 0px !important; max-width: 400px; padding-bottom: 100px; }

        /* NOM : HEDI AYOUB SUR DEUX LIGNES */
        .identity-header { text-align: center; margin-bottom: 25px; margin-top: 20px; }
        .first-name { letter-spacing: 18px; font-size: 36px; font-weight: 100; margin: 0; color: #FFF; line-height: 1.1; }
        .last-name { letter-spacing: 18px; font-size: 36px; font-weight: 100; margin: 0; color: #FFF; line-height: 1.1; }
        .quantum-sub { color: #FF3131; letter-spacing: 4px; font-size: 10px; margin-top: 12px; font-weight: bold; }
        
        /* LOCK BOX STYLE ILLUST */
        .lock-container {
            border: 2px solid #FF3131;
            border-radius: 20px;
            padding: 20px;
            background: rgba(255, 49, 49, 0.05);
            display: flex; align-items: center; justify-content: center; gap: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 25px rgba(255, 49, 49, 0.2);
        }
        .lock-icon { font-size: 32px; filter: drop-shadow(0 0 8px #FF3131); color: #FF3131; }
        
        /* INFO CARD */
        .info-card {
            border: 1.5px solid #00D2FF;
            border-radius: 20px;
            padding: 18px;
            background: rgba(0, 210, 255, 0.02);
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.15);
            margin-bottom: 20px;
        }
        .info-row { display: flex; justify-content: space-between; border-bottom: 1px solid rgba(0, 210, 255, 0.1); padding: 12px 0; font-size: 13px; }
        .info-label { color: #555; font-weight: 900; letter-spacing: 1px; }

        /* NAV BAR BAS DE PAGE (SIMULATION MAQUETTE) */
        .nav-bar {
            position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
            width: 250px; display: flex; justify-content: space-around;
            background: rgba(10, 10, 10, 0.8); backdrop-filter: blur(10px);
            padding: 15px; border-radius: 50px; border: 1px solid #222;
        }
        .nav-icon { font-size: 20px; opacity: 0.5; cursor: pointer; }
        .nav-active { color: #FF3131; opacity: 1; filter: drop-shadow(0 0 5px #FF3131); }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='identity-header'><div class='first-name'>H E D I</div><div class='last-name'>A Y O U B</div><p class='quantum-sub'>QUANTUM PROTOCOL / V16.0</p></div>", unsafe_allow_html=True)

# Lock Box
st.markdown("<div class='lock-container'><div class='lock-icon'>🔒</div><div><div style='font-weight:bold; font-size:15px;'>SYSTEM LOCK</div><div style='color:#FF3131; font-size:11px; font-weight:bold;'>1D + 15M REQUIRED</div></div></div>", unsafe_allow_html=True)

# Actifs
assets = {
    "US30 (DOW JONES)": {"smt": "NQ / ES", "chef": "DXY"},
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "chef": "DXY"},
    "BITCOIN (BTC)": {"smt": "ETH (ETHEREUM)", "chef": "DXY/USDT"},
    "GOLD (XAU)": {"smt": "XAG (SILVER)", "chef": "DXY"},
    "EURUSD": {"smt": "GBPUSD", "chef": "DXY"}
}

target = st.selectbox("", list(assets.keys()), label_visibility="collapsed")
info = assets[target]

# Card Info
st.markdown(f"<div class='info-card'><div class='info-row'><span class='info-label'>🎯 TARGET</span><span>{target}</span></div><div class='info-row'><span class='info-label'>📊 SMT</span><span>{info['smt']}</span></div><div class='info-row' style='border:none;'><span class='info-label'>💸 CHEF</span><span>{info['chef']}</span></div></div>", unsafe_allow_html=True)

# Upload Section (Simplifiée pour éviter le plantage)
uploaded = st.file_uploader("", accept_multiple_files=True, label_visibility="collapsed")

if uploaded:
    count = len(uploaded)
    st.progress(min(count/6, 1.0))
    if count >= 6:
        if st.button("🔥 TAP TO DECRYPT DATA", use_container_width=True):
            # Animation rapide sans EasyOCR pour tester la stabilité
            with st.status("📡 CONNECTING TO QUANTUM CORE...", expanded=True) as status:
                time.sleep(1)
                status.update(label="SCANNING DATASETS...", state="running")
                time.sleep(1)
                status.update(label="ACCESS GRANTED", state="complete")
            
            st.balloons()
            st.success("PREDATOR VISION ACTIVE")
else:
    st.markdown("<div style='border: 2px dashed #FF3131; border-radius:25px; padding:35px; text-align:center; background:rgba(255,49,49,0.02);'><div style='font-size:35px; color:#FF3131; opacity:0.5; margin-bottom:10px;'>☁️</div><p style='color:#666; font-size:11px; letter-spacing:1px;'>UPLOADING 6 REQUIRED DATASETS</p></div>", unsafe_allow_html=True)

# Barre de Navigation (Visuelle uniquement)
st.markdown("""
    <div class='nav-bar'>
        <div class='nav-icon'>🌍</div>
        <div class='nav-icon'>🧭</div>
        <div class='nav-icon nav-active'>👑</div>
    </div>
""", unsafe_allow_html=True)
