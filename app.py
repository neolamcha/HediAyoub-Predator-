import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import random
import time

# ==========================================
# 1. SETUP & NETTOYAGE RADICAL
# ==========================================
st.set_page_config(
    page_title="HEDI AYOUB", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- CSS SUPRÊME : NETTOYAGE INTERFACE ---
st.markdown("""
    <style>
        /* Supprime le Header Streamlit (GitHub, Deploy, Menu) */
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        .stDeployButton {display:none !important;}
        
        /* Supprime les paddings inutiles en haut pour le plein écran */
        .block-container {
            padding-top: 10px !important;
            padding-bottom: 0px !important;
            max-width: 400px;
        }

        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400;900&display=swap');
        
        .stApp { background-color: #030608; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        /* HEADER NOM : HEDI / AYOUB */
        .identity-header { text-align: center; margin-bottom: 25px; }
        .first-name { letter-spacing: 15px; font-size: 38px; font-weight: 100; margin: 0; color: #FFF; line-height: 1; }
        .last-name { letter-spacing: 15px; font-size: 38px; font-weight: 100; margin: 0; color: #FFF; line-height: 1.2; }
        .quantum-sub { color: #FF3131; letter-spacing: 3px; font-size: 10px; margin-top: 10px; font-weight: bold; }
        
        /* BOITE LOCK AVEC GLOW ROUGE */
        .lock-container {
            border: 2px solid #FF3131;
            border-radius: 20px;
            padding: 20px;
            background: rgba(255, 49, 49, 0.05);
            display: flex; align-items: center; justify-content: center; gap: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 25px rgba(255, 49, 49, 0.2);
        }
        .lock-icon { font-size: 30px; filter: drop-shadow(0 0 5px #FF3131); }
        .lock-title { color: #FFF; font-weight: bold; font-size: 14px; }
        .lock-subtitle { color: #FF3131; font-size: 11px; font-weight: bold; }
        
        /* INFO CARD AVEC BORDURE CYAN */
        .info-card {
            border: 1.5px solid #00D2FF;
            border-radius: 20px;
            padding: 18px;
            background: rgba(0, 210, 255, 0.02);
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.15);
            margin-bottom: 20px;
        }
        .info-row { display: flex; justify-content: space-between; border-bottom: 1px solid rgba(0, 210, 255, 0.1); padding: 10px 0; font-size: 13px; }
        .info-label { color: #555; font-weight: 900; text-transform: uppercase; }
        .info-val { color: #FFF; font-weight: bold; }

        /* ZONE UPLOAD DISCRÈTE */
        .upload-area {
            border: 2px dashed rgba(255, 49, 49, 0.3);
            border-radius: 25px;
            padding: 30px;
            text-align: center;
            background: rgba(255, 49, 49, 0.01);
        }
        
        /* Style des inputs Streamlit pour rester sombre */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #030608 !important;
            border: 1px solid #333 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTENU DE L'APP ---

# Header
st.markdown("""
    <div class='identity-header'>
        <div class='first-name'>H E D I</div>
        <div class='last-name'>A Y O U B</div>
        <p class='quantum-sub'>QUANTUM PROTOCOL / V14.5</p>
    </div>
""", unsafe_allow_html=True)

# Lock Box
st.markdown("""
    <div class='lock-container'>
        <div class='lock-icon'>🔒</div>
        <div>
            <div class='lock-title'>SYSTEM LOCK</div>
            <div class='lock-subtitle'>1D + 15M REQUIRED</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Asset Selection
assets = {
    "US30 (DOW JONES)": {"smt": "NQ / ES", "chef": "DXY"},
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "chef": "DXY"},
    "GOLD (XAU)": {"smt": "XAG (SILVER)", "chef": "DXY"}
}

target = st.selectbox("", list(assets.keys()), label_visibility="collapsed")
info = assets[target]

# Info Card
st.markdown(f"""
    <div class='info-card'>
        <div class='info-row'><span class='info-label'>🎯 TARGET</span><span class='info-val'>{target}</span></div>
        <div class='info-row'><span class='info-label'>📊 SMT</span><span class='info-val'>{info['smt']}</span></div>
        <div class='info-row' style='border:none;'><span class='info-label'>💸 CHEF</span><span class='info-val'>{info['chef']}</span></div>
    </div>
""", unsafe_allow_html=True)

# Upload Section
uploaded = st.file_uploader("", accept_multiple_files=True, label_visibility="collapsed")

if not uploaded:
    st.markdown("""
        <div class='upload-area'>
            <div style='font-size:30px; margin-bottom:10px;'>☁️</div>
            <p style='color:#666; font-size:11px; margin:0;'>UPLOADING 6 REQUIRED DATASETS</p>
        </div>
    """, unsafe_allow_html=True)
else:
    count = len(uploaded)
    st.progress(min(count/6, 1.0))
    if count >= 6:
        if st.button("🔥 START QUANTUM SCAN", use_container_width=True):
            st.balloons()
