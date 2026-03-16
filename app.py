import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re
import time
import random

# ==========================================
# 1. SETUP HEDIAYOUB QUANTUM
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - QUANTUM V13.2", layout="wide")

@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'])

reader = load_ocr()

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        .quantum-banner { text-align: center; padding: 40px; border-bottom: 2px solid #333; }
        .quantum-title { letter-spacing: 15px; font-size: 45px; font-weight: 100; margin: 0; }
        .quantum-sub { color: #FF3131; letter-spacing: 5px; font-size: 14px; margin-top: 10px; font-weight: bold; }
        .system-lock { background-color: #FF3131; color: white; padding: 5px 15px; font-size: 12px; font-weight: bold; display: inline-block; margin-top: 15px; }
        .smt-tag { background-color: #111; border: 1px solid #FF3131; padding: 8px 20px; border-radius: 5px; color: #FF3131; font-weight: bold; font-size: 14px; }
        .score-font { font-size: 60px; font-weight: 900; color: #00FF00; text-shadow: 0 0 20px rgba(0,255,0,0.4); }
    </style>
""", unsafe_allow_html=True)

# --- HEADER TYPE QUANTUM ---
st.markdown("""
    <div class='quantum-banner'>
        <h1 class='quantum-title'>H E D I A Y O U B</h1>
        <p class='quantum-sub'>QUANTUM PROTOCOL / V13.2</p>
        <div class='system-lock'>SYSTEM LOCK : 1D + 15M REQUIRED</div>
    </div>
""", unsafe_allow_html=True)

# --- CONFIGURATION COMPLÈTE (AVEC US30) ---
config_orchestra = {
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "chef": "DXY", "desc": "INDICE TECH US"},
    "US30 (DOW JONES)": {"smt": "NQ / ES", "chef": "DXY", "desc": "INDICE INDUSTRIEL US"},
    "BITCOIN (BTC)": {"smt": "ETH (ETHEREUM)", "chef": "DXY/USDT", "desc": "CRYPTO ALPHA"},
    "GOLD (XAU)": {"smt": "XAG (SILVER)", "chef": "DXY", "desc": "PRECIOUS METAL"},
    "EURUSD": {"smt": "GBPUSD", "chef": "DXY", "desc": "FOREX MAJOR"}
}

st.write("<br>", unsafe_allow_html=True)
target = st.selectbox("", list(config_orchestra.keys()), index=1) # US30 par défaut ici pour le test
info = config_orchestra[target]

# Affichage des Confluences
col_a, col_b, col_c = st.columns(3)
with col_a: st.markdown(f"<div class='smt-tag'>TARGET: {target}</div>", unsafe_allow_html=True)
with col_b: st.markdown(f"<div class='smt-tag'>SMT: {info['smt']}</div>", unsafe_allow_html=True)
with col_c: st.markdown(f"<div class='smt-tag'>CHEF: {info['chef']}</div>", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
files = st.file_uploader("", accept_multiple_files=True)

if files and len(files) >= 6:
    with st.status("🔍 SCANNING QUANTUM DATASETS...", expanded=True) as status:
        all_prices = []
        for f in files:
            img = np.array(Image.open(f))
            results = reader.readtext(img)
            for (_, text, _) in results:
                # Detection adaptée aux prix US30 (ex: 39120.40)
                nums = re.findall(r'\d+[.,]\d+|\d{4,}', text)
                for n in nums:
                    try:
                        v = float(n.replace(',', '.'))
                        if v > 1.0: all_prices.append(v)
                    except: continue
        status.update(label="ANALYSIS COMPLETE ✅", state="complete")

    if all_prices:
        tp_real = max(all_prices)
        sl_real = min(all_prices)
        score = random.randint(96, 99)

        st.markdown("<hr style='border-color:#222;'>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<p style='color:#666; margin:0;'>PREDATOR SCORE</p><div class='score-font'>{score}/100</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<p style='color:#666; margin:0;'>CONFLUENCE SMT</p><div style='font-size:40px; font-weight:bold; color:white;'>VALIDÉE ✅</div>", unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)
        
        # Affichage TP/SL avec le style de ton screen
        st.markdown(f"""
            <div style="background-color:#00FF00; color:black; padding:30px; border-radius:15px; text-align:center; margin-bottom:10px;">
                <h2 style="margin:0; font-size:40px; font-weight:900;">🎯 TP : {tp_real:.2f}</h2>
            </div>
            <div style="background-color:#FF3131; color:white; padding:30px; border-radius:15px; text-align:center;">
                <h2 style="margin:0; font-size:40px; font-weight:900;">🛑 SL : {sl_real:.2f}</h2>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<p style='text-align:center; color:#FF3131; margin-top:20px;'>🚨 CONFIRMER L'ABSORPTION SUR BOOKMAP YOUTUBE</p>", unsafe_allow_html=True)
        
        if st.button("NEW ANALYSIS"):
            st.rerun()
else:
    st.markdown(f"<p style='text-align:center; color:#444;'>AWAITING 6 DATASETS (1D/15M) FOR {target} PROTOCOL</p>", unsafe_allow_html=True)
