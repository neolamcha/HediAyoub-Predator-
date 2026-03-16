import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. SETUP
st.set_page_config(page_title="HediAyoub Predator V28", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS FINAL (Alignement parfait & Design Pro)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    
    /* FIX INPUTS */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 4px !important; height: 45px !important; }
    input { color: #000000 !important; font-weight: 900 !important; font-size: 20px !important; }
    
    /* CARDS */
    .card { background: #080808; border: 1px solid #1a1a1a; border-left: 4px solid #ff0000; padding: 25px; margin-bottom: 20px; }
    .label-mini { color: #555; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px; font-weight: 800; }
    
    /* TABLE */
    .trading-table { width: 100%; border-collapse: collapse; }
    .trading-table th { color: #444; text-align: left; font-size: 10px; padding: 12px; border-bottom: 2px solid #111; letter-spacing: 2px; }
    .trading-table td { padding: 18px 12px; font-size: 16px; border-bottom: 1px solid #0a0a0a; font-family: 'JetBrains Mono'; }

    /* MATRIX GRID */
    .matrix-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin-top: 20px; }
    .matrix-box { background: #080808; border: 1px solid #1a1a1a; padding: 20px; text-align: center; border-bottom: 3px solid #333; transition: 0.3s; }
    .matrix-box:hover { border-color: #ff0000; background: #0c0000; }
</style>
""", unsafe_allow_html=True)

# --- TOP STATUS BAR ---
st.markdown(f"""
    <div style='display:flex; justify-content: space-between; padding: 10px 20px; background: #050505; border-bottom: 1px solid #111;'>
        <div style='color:red; font-family:Orbitron; letter-spacing:2px; font-weight:900;'>PREDATOR_CORE_V28</div>
        <div style='color:#444; font-size:12px;'>SYSTEM_STATUS: <span style='color:#00ff41;'>ONLINE</span></div>
        <div style='color:#444; font-size:12px;'>UTC: {datetime.now().strftime('%H:%M:%S')}</div>
    </div><br>
""", unsafe_allow_html=True)

col_main, col_risk = st.columns([2.8, 1.2])

with col_risk:
    # RISK MODULE
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Liquidity / Risk Unit</p>", unsafe_allow_html=True)
    
    cap = st.number_input("ACCOUNT ($)", value=100000)
    r_pct = st.slider("RISK EXPOSURE (%)", 0.1, 5.0, 1.0)
    
    r_val = cap * (r_pct / 100)
    l_size = round(r_val / 350, 2)
    
    st.markdown(f"""
        <div style='text-align:center; margin-top:25px; border-top:1px solid #111; padding-top:20px;'>
            <p class='label-mini'>Computed Position</p>
            <p style='font-family:Orbitron; font-size:55px; color:white; margin:0; line-height:1;'>{l_size}</p>
            <p style='color:red; font-weight:bold; margin-top:10px;'>MAX DRAWDOWN: ${r_val:,.2f}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # TIMER MODULE (MACRO WINDOW)
    st.markdown(f"""
        <div class='card' style='text-align:center;'>
            <p class='label-mini'>Macro Window Open In</p>
            <p style='font-family:Orbitron; font-size:45px; color:red; margin:0; text-shadow: 0 0 10px rgba(255,0,0,0.5);'>08:14</p>
            <p style='color:#333; font-size:10px; margin-top:5px;'>ALGORITHMIC VOLATILITY DETECTED</p>
        </div>
    """, unsafe_allow_html=True)

with col_main:
    # TARGET CARD
    st.markdown(f"""
        <div class='card'>
            <p class='label-mini'>Predator Target</p>
            <h1 style='font-family:Orbitron; font-size:55px; margin:0;'>NASDAQ <span style='color:red;'>NQ1!</span></h1>
            <div style='display:flex; gap:60px; margin-top:20px;'>
                <div><p class='label-mini'>Confluence Score</p><p style='font-family:Orbitron; font-size:32px; color:red; margin:0;'>99.2%</p></div>
                <div><p class='label-mini'>Institutional Bias</p><p style='font-family:Orbitron; font-size:32px; color:white; margin:0;'>BULLISH</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # TABLEAU
    st.markdown("<p class='label-mini'>Current Market Operations</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='trading-table'>
            <tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>TARGET / STOP</th><th>PNL</th></tr>
            <tr style='background: rgba(255,0,0,0.02);'>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td><b style='font-family:Orbitron; font-size:20px;'>{l_size}</b></td>
                <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                <td style='color:#00ff41; font-family:Orbitron; font-size:20px; font-weight:900;'>+${(l_size * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

# MATRIX (10 PAIRES)
st.markdown("<br><p class='label-mini'>Global Asset Confluence Matrix</p>", unsafe_allow_html=True)
pairs = [("NQ1!", 99), ("ES1!", 85), ("XAUUSD", 72), ("EURUSD", 96), ("GBPUSD", 88), 
         ("BTCUSD", 91), ("USDJPY", 84), ("AUDUSD", 79), ("USDCAD", 82), ("ETHUSD", 65)]

cols = st.columns(5)
for i, (name, score) in enumerate(pairs):
    with cols[i % 5]:
        b_color = "red" if score > 90 else "#222"
        s_color = "red" if score > 90 else "white"
        st.markdown(f"""
            <div class='matrix-box' style='border-bottom-color: {b_color};'>
                <p style='font-family:Orbitron; font-size:18px; margin:0; color:white;'>{name}</p>
                <p style='color:{s_color}; font-weight:bold; margin:5px 0 0 0; font-size:14px;'>{score}%</p>
            </div>
        """, unsafe_allow_html=True)

st.code("> PREDATOR_V28: Global Matrix & Risk Units Ready. All systems green.", language="bash")
