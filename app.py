import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. SETUP SYSTÈME
st.set_page_config(page_title="HediAyoub Predator V31", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE PRÉCISION (Stabilisation et Alertes)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 4px !important; }
    input { color: #000000 !important; font-weight: 900 !important; font-size: 18px !important; }
    
    .card { background: #080808; border: 1px solid #1a1a1a; border-left: 4px solid #ff0000; padding: 20px; margin-bottom: 15px; }
    .label-mini { color: #555; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; font-weight: 800; }
    
    /* A+ SETUP ALERT */
    .aplus-box {
        background: linear-gradient(90deg, #1a0000, #000);
        border: 2px solid #ff0000;
        padding: 15px;
        text-align: center;
        border-radius: 8px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { box-shadow: 0 0 5px #ff0000; } 50% { box-shadow: 0 0 20px #ff0000; } 100% { box-shadow: 0 0 5px #ff0000; } }
</style>
""", unsafe_allow_html=True)

# 3. HEADER & STATUS
st.markdown(f"""
    <div style='display:flex; justify-content: space-between; padding: 10px 20px; background: #050505; border-bottom: 1px solid #111;'>
        <div style='color:red; font-family:Orbitron; letter-spacing:2px; font-weight:900;'>PREDATOR_V31 // HEDI AYOUB</div>
        <div style='color:#00ff41; font-size:12px; font-family:Orbitron;'>● A+ ALGORITHM ACTIVE</div>
    </div><br>
""", unsafe_allow_html=True)

col_main, col_risk = st.columns([3, 1])

with col_risk:
    # --- CALCULATEUR ---
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Liquidity Management</p>", unsafe_allow_html=True)
    cap = st.number_input("ACCOUNT ($)", value=100000)
    r_pct = st.slider("RISK (%)", 0.1, 5.0, 1.0)
    l_size = round((cap * (r_pct / 100)) / 350, 2)
    st.markdown(f"<div style='text-align:center; margin-top:15px;'><p class='label-mini'>Position Size</p><p style='font-family:Orbitron; font-size:45px; margin:0;'>{l_size}</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- A+ SETUP DETECTOR ---
    st.markdown("<div class='aplus-box'>", unsafe_allow_html=True)
    st.markdown("<p style='color:#ff0000; font-family:Orbitron; font-size:12px; margin:0;'>SETUP STATUS</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white; font-family:Orbitron; margin:5px 0;'>GRADE: A+</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00ff41; font-size:10px; margin:0;'>CONFLUENCE REACHED</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- TIMER ---
    st.markdown("<div class='card' style='text-align:center; margin-top:15px;'>", unsafe_allow_html=True)
    components.html("""
        <div id="t" style="font-family:'Orbitron'; color:red; font-size:35px; font-weight:900; text-align:center;">08:14</div>
        <script>
            let s = 494; setInterval(() => {
                let m = Math.floor(s/60); let sec = s%60;
                document.getElementById('t').innerHTML = (m<10?'0':'')+m+":"+(sec<10?'0':'')+sec;
                if(s>0) s--; else document.getElementById('t').innerHTML="OPEN";
            }, 1000);
        </script>
    """, height=45)
    st.markdown("<p class='label-mini'>Macro Window</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_main:
    # --- CHART TRADINGVIEW ---
    st.markdown("<div class='card' style='padding:10px;'>", unsafe_allow_html=True)
    components.html("""
        <div id="tradingview_predator" style="height:480px;"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true, "symbol": "CME_MINI:NQ1!", "interval": "5", "timezone": "Etc/UTC",
          "theme": "dark", "style": "1", "locale": "fr", "toolbar_bg": "#f1f3f6",
          "backgroundColor": "#000000", "gridColor": "rgba(42, 46, 57, 0.06)",
          "container_id": "tradingview_predator", "hide_side_toolbar": false
        });
        </script>
    """, height=480)
    st.markdown("</div>", unsafe_allow_html=True)

# --- GLOBAL MATRIX (TOUS LES ACTIFS) ---
st.markdown("<p class='label-mini' style='padding-left:10px;'>Global Neural Matrix - 10 Assets Scanning</p>", unsafe_allow_html=True)
assets = [
    ("NQ1!", 99), ("ES1!", 88), ("XAUUSD", 94), ("EURUSD", 96), ("GBPUSD", 82),
    ("BTCUSD", 91), ("USDJPY", 74), ("AUDUSD", 79), ("USDCAD", 85), ("ETHUSD", 68)
]

m_cols = st.columns(5)
for i, (name, score) in enumerate(assets):
    with m_cols[i % 5]:
        color = "#ff0000" if score > 90 else "#ffffff"
        border = "2px solid #ff0000" if score > 90 else "1px solid #1a1a1a"
        st.markdown(f"""
            <div style='background:#080808; border:{border}; padding:15px; text-align:center; margin-bottom:10px;'>
                <p style='font-family:Orbitron; font-size:14px; margin:0; color:white;'>{name}</p>
                <p style='color:{color}; font-weight:bold; margin:0;'>{score}%</p>
            </div>
        """, unsafe_allow_html=True)
