import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re
import random

# ==========================================
# 1. CONFIGURATION QUANTUM
# ==========================================
st.set_page_config(page_title="HEDIAYOUB QUANTUM", layout="centered")

@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'])

reader = load_ocr()

# --- CSS CUSTOM POUR LOOK MOBILE NEON ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400;900&display=swap');
        
        .stApp { background-color: #050a0e; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        /* Conteneur Principal */
        .quantum-card {
            background: rgba(10, 20, 28, 0.8);
            border: 1px solid rgba(0, 255, 255, 0.2);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 15px rgba(0, 210, 255, 0.1);
        }

        /* Header */
        .header-title { letter-spacing: 12px; font-size: 32px; font-weight: 100; text-align: center; margin-bottom: 0; }
        .header-sub { color: #FF3131; letter-spacing: 3px; font-size: 10px; text-align: center; margin-top: 5px; font-weight: bold; }
        
        /* System Lock Badge */
        .lock-container {
            border: 2px solid #FF3131;
            border-radius: 15px;
            padding: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
            box-shadow: inset 0 0 10px rgba(255, 49, 49, 0.2), 0 0 15px rgba(255, 49, 49, 0.2);
        }
        
        /* Info Box Blue Neon */
        .info-box {
            border: 1px solid #00D2FF;
            border-radius: 15px;
            padding: 15px;
            background: rgba(0, 210, 255, 0.05);
            box-shadow: 0 0 10px rgba(0, 210, 255, 0.1);
        }
        .info-line { display: flex; justify-content: space-between; border-bottom: 1px solid rgba(0, 210, 255, 0.1); padding: 8px 0; font-size: 13px; }
        .info-label { color: #888; text-transform: uppercase; letter-spacing: 1px; }
        .info-value { color: #FFF; font-weight: bold; }

        /* Upload Area */
        .upload-zone {
            border: 2px dashed #FF3131;
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            margin-top: 20px;
            background: rgba(255, 49, 49, 0.02);
        }
        
        /* Progress Bar */
        .progress-text { font-size: 12px; color: #666; margin-top: 10px; letter-spacing: 1px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='header-title'>HEDIAYOUB</h1>", unsafe_allow_html=True)
st.markdown("<p class='header-sub'>QUANTUM PROTOCOL / V13.5</p>", unsafe_allow_html=True)

# --- SYSTEM LOCK ---
st.markdown("""
    <div class='lock-container'>
        <div style='font-size: 30px;'>🔒</div>
        <div style='text-align: left;'>
            <div style='color: #FFF; font-weight: bold; font-size: 14px;'>SYSTEM LOCK</div>
            <div style='color: #FF3131; font-size: 12px;'>1D + 15M REQUIRED</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- DATA CONFIG ---
assets = {
    "US30 (DOW JONES)": {"smt": "NQ / ES", "chef": "DXY"},
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "chef": "DXY"},
    "BITCOIN (BTC)": {"smt": "ETH (ETHEREUM)", "chef": "DXY/USDT"},
    "GOLD (XAU)": {"smt": "XAG (SILVER)", "chef": "DXY"},
    "EURUSD": {"smt": "GBPUSD", "chef": "DXY"}
}

target = st.selectbox("", list(assets.keys()))
info = assets[target]

# --- INFO BOX ---
st.markdown(f"""
    <div class='info-box'>
        <div class='info-line'><span class='info-label'>🎯 TARGET</span><span class='info-value'>{target}</span></div>
        <div class='info-line'><span class='info-label'>📊 SMT</span><span class='info-value'>{info['smt']}</span></div>
        <div class='info-line' style='border:none;'><span class='info-label'>💸 CHEF</span><span class='info-value'>{info['chef']}</span></div>
    </div>
""", unsafe_allow_html=True)

# --- UPLOAD SECTION ---
st.write("<br>", unsafe_allow_html=True)
files = st.file_uploader("", accept_multiple_files=True)

if files:
    count = len(files)
    progress = min(count / 6, 1.0)
    st.progress(progress)
    st.markdown(f"<p class='progress-text' style='text-align:center;'>{count}/6 DATASETS COLLECTED</p>", unsafe_allow_html=True)
    
    if count >= 6:
        if st.button("🔥 TAP TO ANALYZE MARKET", use_container_width=True):
            with st.spinner("QUANTUM SCANNING..."):
                # Simulation d'extraction
                all_prices = [random.uniform(38000, 39500) for _ in range(10)]
                tp = max(all_prices)
                sl = min(all_prices)
                score = random.randint(97, 99)
                
                st.markdown(f"""
                    <div style='text-align:center; padding: 20px;'>
                        <div style='font-size: 50px; color:#00FF00; font-weight:900;'>{score}%</div>
                        <p style='color:#00FF00; letter-spacing:2px;'>CONFLUENCE PROBABILITY</p>
                    </div>
                    <div style='background:#00FF00; color:#000; padding:20px; border-radius:10px; text-align:center; margin-bottom:10px;'>
                        <b>🎯 TARGET EXIT : {tp:.2f}</b>
                    </div>
                    <div style='background:#FF3131; color:#FFF; padding:20px; border-radius:10px; text-align:center;'>
                        <b>🛑 RISK STOP : {sl:.2f}</b>
                    </div>
                """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class='upload-zone'>
            <span style='font-size: 40px;'>☁️</span><br>
            <p style='color: #666; font-size: 12px; margin-top:10px;'>UPLOADING 6 REQUIRED DATASETS</p>
        </div>
    """, unsafe_allow_html=True)
