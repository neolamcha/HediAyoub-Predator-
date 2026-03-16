import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re
import random

# ==========================================
# SYSTEM CORE : HEDIAYOUB QUANTUM V13.0
# ==========================================
st.set_page_config(
    page_title="HEDIAYOUB QUANTUM",
    page_icon="🔴",
    layout="wide",
)

@st.cache_resource
def load_quantum_vision():
    return easyocr.Reader(['en'])

reader = load_quantum_vision()

# ==========================================
# DESIGN : LUXURY OBSIDIAN INTERFACE
# ==========================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400;900&family=JetBrains+Mono:wght@100&display=swap');

        /* Background Principal */
        .stApp { 
            background: radial-gradient(circle at top, #1a0505 0%, #000000 100%); 
            color: #FFFFFF; 
            font-family: 'Inter', sans-serif;
        }

        /* Header Ultra-Luxe */
        .quantum-header {
            padding: 60px 20px;
            text-align: center;
            border-bottom: 1px solid rgba(255, 49, 49, 0.2);
            margin-bottom: 40px;
        }
        .main-title {
            font-family: 'Inter', sans-serif;
            font-weight: 100;
            letter-spacing: 25px;
            font-size: 45px;
            text-transform: uppercase;
            margin-bottom: 10px;
            color: #fff;
            text-shadow: 0 0 30px rgba(255,255,255,0.2);
        }
        .sub-brand {
            font-family: 'JetBrains Mono', monospace;
            color: #FF3131;
            letter-spacing: 10px;
            font-size: 14px;
            text-transform: uppercase;
            opacity: 0.9;
        }

        /* Badge de Rempart TF */
        .tf-status-bar {
            background: rgba(255, 49, 49, 0.05);
            border: 1px solid #FF3131;
            padding: 12px 30px;
            display: inline-block;
            margin-top: 30px;
            font-weight: 900;
            color: #FF3131;
            letter-spacing: 3px;
            box-shadow: 0 0 20px rgba(255, 49, 49, 0.1);
        }

        /* Cartes de Data (Glassmorphism) */
        .data-card {
            background: rgba(10, 10, 10, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 40px;
            border-radius: 2px;
            text-align: center;
            transition: 0.3s;
        }
        .data-card:hover {
            border-color: rgba(255, 49, 49, 0.3);
            background: rgba(20, 20, 20, 0.9);
        }

        .label-text {
            color: #444;
            font-size: 11px;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-bottom: 20px;
        }
        .tp-glow {
            color: #00FF00;
            font-size: 42px;
            font-weight: 900;
            text-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
        }
        .sl-glow {
            color: #FF3131;
            font-size: 42px;
            font-weight: 900;
            text-shadow: 0 0 20px rgba(255, 49, 49, 0.2);
        }

        /* Sidebar & Selectbox */
        .stSelectbox label { color: #555 !important; letter-spacing: 2px; }
        
    </style>
""", unsafe_allow_html=True)

# --- UI HEADER ---
st.markdown("""
    <div class='quantum-header'>
        <h1 class='main-title'>HEDIAYOUB</h1>
        <p class='sub-brand'>QUANTUM PROTOCOL / V13.0</p>
        <div class='tf-status-bar'>SYSTEM LOCK : 1D + 15M REQUIRED</div>
    </div>
""", unsafe_allow_html=True)

# --- SELECTION ---
orchestra = {
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "chef": "DXY"},
    "BITCOIN (BTC)": {"smt": "ETH (Ethereum)", "chef": "DXY/USDT"},
    "GOLD (XAU)": {"smt": "XAG (Silver)", "chef": "DXY"},
    "EURUSD": {"smt": "GBPUSD (Cable)", "chef": "DXY"}
}

c_sel, c_info = st.columns([2, 1])
with c_sel:
    target = st.selectbox("", list(orchestra.keys()), label_visibility="collapsed")
    info = orchestra[target]

with c_info:
    st.markdown(f"<p style='text-align:right; color:#444; font-size:12px; letter-spacing:2px;'>SYNC: {info['smt']} | CONDUCTOR: {info['chef']}</p>", unsafe_allow_html=True)

# --- UPLOAD SECTION ---
st.divider()
files = st.file_uploader("", accept_multiple_files=True, label_visibility="collapsed")

if files and len(files) >= 6:
    with st.status("INITIALIZING NEURAL SCAN...", expanded=False) as status:
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
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
                <div class='data-card'>
                    <p class='label-text'>TARGET LIQUIDITY</p>
                    <p class='tp-glow'>{tp:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
                <div class='data-card'>
                    <p class='label-text'>INVALIDATION POINT</p>
                    <p class='sl-glow'>{sl:.2f}</p>
                </div>
            """, unsafe_allow_html=True)

        # --- CHECKLIST DE CONFLUENCE ---
        st.write("<br><br>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#333; letter-spacing:5px; font-size:10px;'>CONFLUENCE FINAL CHECK</p>", unsafe_allow_html=True)
        
        chk_1, chk_2, chk_3, chk_4 = st.columns(4)
        with chk_1: b1 = st.checkbox("BOOKMAP")
        with chk_2: b2 = st.checkbox("SMT DIV")
        with chk_3: b3 = st.checkbox("DXY SYNC")
        with chk_4: b4 = st.checkbox("1D/15M")

        if b1 and b2 and b3 and b4:
            st.success("PROTOCOL VALIDATED. READY FOR EXECUTION.")
            st.toast("Access Granted", icon="🔴")
        
        if st.button("RESET SYSTEM"):
            st.rerun()

else:
    st.markdown("<p style='text-align:center; color:#222; letter-spacing:3px; margin-top:50px;'>AWAITING 6 QUANTUM DATASETS (1D/15M)...</p>", unsafe_allow_html=True)
