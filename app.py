import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re
import random

# ==========================================
# 1. CONFIGURATION QUANTUM & NATIVE PWA
# ==========================================
st.set_page_config(page_title="HEDI AYOUB QUANTUM", layout="centered")

# Injection des balises pour simuler une App Native sur iPhone
st.markdown("""
    <head>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
        <link rel="apple-touch-icon" href="https://cdn-icons-png.flaticon.com/512/2922/2922510.png">
    </head>
""", unsafe_allow_html=True)

@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'])

reader = load_ocr()

# --- CSS EXTRÊME : LOOK MAQUETTE NATIVE ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400;900&display=swap');
        
        /* Fond OLED Profond */
        .stApp { 
            background-color: #030608; 
            color: #FFFFFF; 
            font-family: 'Inter', sans-serif;
        }

        /* Ajustement pour l'encoche iPhone (Safe Area) */
        .block-container { 
            padding-top: 60px !important; 
            max-width: 420px; 
        }

        /* HEADER NOM : HEDI (Ligne 1) AYOUB (Ligne 2) */
        .identity-header { text-align: center; margin-bottom: 40px; }
        .first-name { letter-spacing: 18px; font-size: 40px; font-weight: 100; margin: 0; color: #FFF; line-height: 1; }
        .last-name { letter-spacing: 18px; font-size: 40px; font-weight: 100; margin: 0; color: #FFF; line-height: 1.3; }
        .quantum-sub { color: #FF3131; letter-spacing: 4px; font-size: 10px; margin-top: 15px; font-weight: bold; opacity: 0.9; }
        
        /* SYSTEM LOCK : ROUGE NÉON MAQUETTE */
        .lock-container {
            border: 2px solid #FF3131;
            border-radius: 20px;
            padding: 22px;
            background: rgba(255, 49, 49, 0.04);
            display: flex; align-items: center; justify-content: center; gap: 20px;
            margin-bottom: 30px;
            box-shadow: 0 0 25px rgba(255, 49, 49, 0.25);
        }
        .lock-icon { font-size: 35px; color: #FF3131; filter: drop-shadow(0 0 10px #FF3131); }
        .lock-title { color: #FFF; font-weight: 900; font-size: 16px; letter-spacing: 1px; }
        .lock-subtitle { color: #FF3131; font-size: 12px; font-weight: bold; }
        
        /* INFO CARD : CYAN NÉON MAQUETTE */
        .info-card {
            border: 1.5px solid rgba(0, 210, 255, 0.4);
            border-radius: 20px;
            padding: 22px;
            background: rgba(0, 210, 255, 0.02);
            box-shadow: 0 0 30px rgba(0, 210, 255, 0.15);
            margin-bottom: 30px;
        }
        .info-row { display: flex; justify-content: space-between; border-bottom: 1px solid rgba(0, 210, 255, 0.1); padding: 14px 0; }
        .info-label { color: #666; font-size: 11px; font-weight: 900; letter-spacing: 1px; }
        .info-val { color: #FFF; font-size: 13px; font-weight: bold; }

        /* UPLOAD ZONE STYLE MAQUETTE */
        .upload-area {
            border: 2px dashed rgba(255, 49, 49, 0.3);
            border-radius: 25px;
            padding: 50px 20px;
            text-align: center;
            background: rgba(255, 49, 49, 0.01);
        }
        .upload-icon { font-size: 50px; color: #FF3131; opacity: 0.3; margin-bottom: 15px; }
        
        /* Masquer interface Web */
        #MainMenu, footer, .stDeployButton { visibility: hidden; }
        .stSelectbox div[data-baseweb="select"] { background-color: #030608 !important; border-color: #222 !important; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER : HEDI AYOUB ---
st.markdown("""
    <div class='identity-header'>
        <div class='first-name'>H E D I</div>
        <div class='last-name'>A Y O U B</div>
        <p class='quantum-sub'>QUANTUM PROTOCOL / V14.5</p>
    </div>
""", unsafe_allow_html=True)

# --- SYSTEM LOCK ---
st.markdown("""
    <div class='lock-container'>
        <div class='lock-icon'>🔒</div>
        <div>
            <div class='lock-title'>SYSTEM LOCK</div>
            <div class='lock-subtitle'>1D + 15M REQUIRED</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- ASSETS ---
assets = {
    "US30 (DOW JONES)": {"smt": "NQ / ES", "chef": "DXY"},
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "chef": "DXY"},
    "BITCOIN (BTC)": {"smt": "ETH (ETHEREUM)", "chef": "DXY/USDT"},
    "GOLD (XAU)": {"smt": "XAG (SILVER)", "chef": "DXY"},
    "EURUSD": {"smt": "GBPUSD", "chef": "DXY"}
}

target = st.selectbox("", list(assets.keys()), label_visibility="collapsed")
info = assets[target]

# --- INFO CARD ---
st.markdown(f"""
    <div class='info-card'>
        <div class='info-row'><span class='info-label'>🎯 TARGET</span><span class='info-val'>{target}</span></div>
        <div class='info-row'><span class='info-label'>📊 SMT</span><span class='info-val'>{info['smt']}</span></div>
        <div class='info-row' style='border:none;'><span class='info-label'>💸 CHEF</span><span class='info-val'>{info['chef']}</span></div>
    </div>
""", unsafe_allow_html=True)

# --- UPLOAD SECTION ---
uploaded_files = st.file_uploader("", accept_multiple_files=True, label_visibility="collapsed")

if uploaded_files:
    count = len(uploaded_files)
    st.progress(min(count / 6, 1.0))
    if count >= 6:
        if st.button("🔥 TAP TO DECRYPT DATA", use_container_width=True):
            st.success("QUANTUM ANALYSIS ACTIVE")
else:
    st.markdown("""
        <div class='upload-area'>
            <div class='upload-icon'>☁️</div>
            <p style='color: #555; font-size: 11px; letter-spacing:1px; margin:0;'>UPLOADING 6 REQUIRED DATASETS</p>
            <p style='color: #FF3131; font-size: 10px; font-weight:bold; margin-top:10px;'>TAP TO COLLECT DATA</p>
        </div>
    """, unsafe_allow_html=True)
