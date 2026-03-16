import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re
import random

# ==========================================
# SYSTEM CORE : HEDIAYOUB QUANTUM V13.1
# ==========================================
st.set_page_config(page_title="HEDIAYOUB QUANTUM", page_icon="🔴", layout="wide")

@st.cache_resource
def load_quantum_vision():
    return easyocr.Reader(['en'])

reader = load_quantum_vision()

# ==========================================
# DESIGN : APEX PRECISION (SMT FOCUS)
# ==========================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400;900&family=JetBrains+Mono:wght@100&display=swap');

        .stApp { background: #000; color: #fff; font-family: 'Inter', sans-serif; }
        
        /* Header */
        .quantum-header { padding: 50px 0; text-align: center; border-bottom: 1px solid #111; }
        .main-title { letter-spacing: 25px; font-weight: 100; font-size: 45px; margin: 0; }
        .sub-brand { color: #FF3131; letter-spacing: 8px; font-size: 14px; font-weight: 900; }
        
        /* Les Nouveaux SMT (Puissants & Esthétiques) */
        .confluence-container {
            display: flex; justify-content: center; gap: 20px; margin: 30px 0;
        }
        .confluence-box {
            background: rgba(255, 255, 255, 0.03);
            border-left: 3px solid #FF3131;
            padding: 15px 40px;
            text-align: left;
            min-width: 250px;
        }
        .conf-label { color: #444; font-size: 10px; letter-spacing: 3px; margin-bottom: 5px; }
        .conf-value { color: #fff; font-size: 22px; font-weight: 900; letter-spacing: 2px; }
        
        /* Badge TF */
        .tf-lock { 
            background: #FF3131; color: #000; padding: 5px 20px; 
            font-weight: 900; letter-spacing: 2px; font-size: 12px;
        }

        /* Data Cards */
        .data-card {
            background: #050505; border: 1px solid #111; padding: 40px; text-align: center;
        }
        .tp-glow { color: #00FF00; font-size: 45px; font-weight: 900; text-shadow: 0 0 20px rgba(0, 255, 0, 0.2); }
        .sl-glow { color: #FF3131; font-size: 45px; font-weight: 900; text-shadow: 0 0 20px rgba(255, 49, 49, 0.2); }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class='quantum-header'>
        <h1 class='main-title'>HEDIAYOUB</h1>
        <p class='sub-brand'>QUANTUM PROTOCOL / V13.1</p>
        <span class='tf-lock'>SYSTEM LOCK : 1D + 15M REQUIRED</span>
    </div>
""", unsafe_allow_html=True)

# --- CONFIGURATION ---
orchestra = {
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "chef": "DXY"},
    "BITCOIN (BTC)": {"smt": "ETH (Ethereum)", "chef": "DXY/USDT"},
    "GOLD (XAU)": {"smt": "XAG (Silver)", "chef": "DXY"},
    "EURUSD": {"smt": "GBPUSD (Cable)", "chef": "DXY"}
}

target = st.selectbox("", list(orchestra.keys()), label_visibility="collapsed")
info = orchestra[target]

# --- AFFICHAGE SMT PUISSANT ---
st.markdown(f"""
    <div class='confluence-container'>
        <div class='confluence-box'>
            <div class='conf-label'>SMT CORRELATION</div>
            <div class='conf-value'>{info['smt']}</div>
        </div>
        <div class='confluence-box'>
            <div class='conf-label'>CONDUCTOR SYNC</div>
            <div class='conf-value'>{info['chef']}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- UPLOAD ---
files = st.file_uploader("", accept_multiple_files=True, label_visibility="collapsed")

if files and len(files) >= 6:
    with st.status("NEURAL SCANNING...", expanded=False) as status:
        prices = []
        for f in files:
            img = np.array(Image.open(f))
            res = reader.readtext(img)
            for (_, text, _) in res:
                nums = re.findall(r'\d+[.,]\d+|\d{4,}', text)
                for n in nums:
                    try:
                        v = float(n.replace(',', '.'))
                        if v > 1.0: prices.append(v)
                    except: continue
        status.update(label="SCAN COMPLETE", state="complete")

    if prices:
        tp, sl = max(prices), min(prices)
        st.write("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='data-card'><p style='color:#444; font-size:10px; letter-spacing:3px;'>TARGET LIQUIDITY</p><p class='tp-glow'>{tp:.2f}</p></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='data-card'><p style='color:#444; font-size:10px; letter-spacing:3px;'>INVALIDATION POINT</p><p class='sl-glow'>{sl:.2f}</p></div>", unsafe_allow_html=True)

        # --- CHECKLIST ---
        st.write("<br>", unsafe_allow_html=True)
        chk_1, chk_2, chk_3, chk_4 = st.columns(4)
        with chk_1: b1 = st.checkbox("BOOKMAP")
        with chk_2: b2 = st.checkbox("SMT DIV")
        with chk_3: b3 = st.checkbox("DXY SYNC")
        with chk_4: b4 = st.checkbox("1D/15M")

        if b1 and b2 and b3 and b4:
            st.success("PROTOCOL VALIDATED.")
        if st.button("RESET"): st.rerun()
else:
    st.markdown("<p style='text-align:center; color:#222; letter-spacing:3px; margin-top:50px;'>AWAITING 6 DATASETS (1D/15M)...</p>", unsafe_allow_html=True)
