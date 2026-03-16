import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. SETUP SYSTÈME
st.set_page_config(page_title="HediAyoub Predator V29", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE PRÉCISION (Stabilisation des couleurs et des polices)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    
    /* FIX INPUTS : Visibilité maximale */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 4px !important; }
    input { color: #000000 !important; font-weight: 900 !important; font-size: 20px !important; }
    
    /* DESIGN CARDS */
    .card { background: #080808; border: 1px solid #1a1a1a; border-left: 4px solid #ff0000; padding: 25px; margin-bottom: 20px; }
    .label-mini { color: #555; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px; font-weight: 800; }
    
    /* TABLEAU D'EXÉCUTION */
    .trading-table { width: 100%; border-collapse: collapse; }
    .trading-table th { color: #444; text-align: left; font-size: 10px; padding: 12px; border-bottom: 2px solid #111; }
    .trading-table td { padding: 18px 12px; font-size: 16px; border-bottom: 1px solid #0a0a0a; font-family: 'JetBrains Mono'; }

    /* GRILLE DE LA MATRICE */
    .matrix-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin-top: 20px; }
    .matrix-box { background: #080808; border: 1px solid #1a1a1a; padding: 20px; text-align: center; border-bottom: 3px solid #333; }
</style>
""", unsafe_allow_html=True)

# 3. BARRE DE STATUT SUPÉRIEURE
st.markdown(f"""
    <div style='display:flex; justify-content: space-between; padding: 10px 20px; background: #050505; border-bottom: 1px solid #111;'>
        <div style='color:red; font-family:Orbitron; letter-spacing:2px; font-weight:900;'>HEDI AYOUB // PREDATOR_V29</div>
        <div style='color:#00ff41; font-size:12px; font-family:Orbitron;'>● SYSTEM_LIVE</div>
    </div><br>
""", unsafe_allow_html=True)

col_main, col_risk = st.columns([2.8, 1.2])

with col_risk:
    # --- MODULE DE GESTION DU RISQUE ---
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Liquidity Management</p>", unsafe_allow_html=True)
    
    cap = st.number_input("ACCOUNT CAPITAL ($)", value=100000)
    r_pct = st.slider("RISK EXPOSURE (%)", 0.1, 5.0, 1.0)
    
    r_val = cap * (r_pct / 100)
    l_size = round(r_val / 350, 2)
    
    st.markdown(f"""
        <div style='text-align:center; margin-top:25px; border-top:1px solid #111; padding-top:20px;'>
            <p class='label-mini'>Calculated Size</p>
            <p style='font-family:Orbitron; font-size:55px; color:white; margin:0;'>{l_size}</p>
            <p style='color:red; font-weight:bold; margin-top:5px;'>RISK: ${r_val:,.2f}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- TIMER MACRO DYNAMIQUE (JS ENGINE) ---
    st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Macro Window Open In</p>", unsafe_allow_html=True)
    
    components.html("""
        <div id="timer" style="font-family:'Orbitron'; color:red; font-size:45px; font-weight:900; text-align:center; text-shadow: 0 0 10px rgba(255,0,0,0.5);">08:14</div>
        <script>
            let s = (8 * 60) + 14;
            const d = document.getElementById('timer');
            setInterval(() => {
                let m = Math.floor(s / 60);
                let sec = s % 60;
                d.innerHTML = (m<10?'0':'')+m + ":" + (sec<10?'0':'')+sec;
                if(s > 0) s--; else { d.innerHTML = "OPEN"; d.style.color = "#00ff41"; }
            }, 1000);
        </script>
    """, height=60)
    st.markdown("<p style='color:#333; font-size:10px; margin-top:5px;'>ALGORITHMIC VOLATILITY SCAN</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_main:
    # --- TARGET CARD ---
    st.markdown(f"""
        <div class='card'>
            <p class='label-mini'>Primary Predator Target</p>
            <h1 style='font-family:Orbitron; font-size:55px; margin:0;'>NASDAQ <span style='color:red;'>NQ1!</span></h1>
            <div style='display:flex; gap:60px; margin-top:15px;'>
                <div><p class='label-mini'>Confluence Score</p><p style='font-family:Orbitron; font-size:32px; color:red; margin:0;'>99.2%</p></div>
                <div><p class='label-mini'>Bias</p><p style='font-family:Orbitron; font-size:32px; color:white; margin:0;'>BULLISH</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- TABLEAU DYNAMIQUE ---
    st.markdown("<p class='label-mini'>Active Execution Tracker</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='trading-table'>
            <tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>TARGET / STOP</th><th>LIVE PNL</th></tr>
            <tr style='background: rgba(255,0,0,0.02);'>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td><b style='font-family:Orbitron; font-size:20px;'>{l_size}</b></td>
                <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                <td style='color:#00ff41; font-family:Orbitron; font-size:20px; font-weight:900;'>+${(l_size * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

# --- MATRICE DES 10 PAIRES ---
st.markdown("<br><p class='label-mini'>Global Asset Intelligence Matrix</p>", unsafe_allow_html=True)
pairs = [("NQ1!", 99), ("ES1!", 85), ("XAUUSD", 72), ("EURUSD", 96), ("GBPUSD", 88), 
         ("BTCUSD", 91), ("USDJPY", 84), ("AUDUSD", 79), ("USDCAD", 82), ("ETHUSD", 65)]

cols = st.columns(5)
for i, (name, score) in enumerate(pairs):
    with cols[i % 5]:
        b_color = "red" if score > 90 else "#222"
        st.markdown(f"""
            <div style='background:#080808; border:1px solid #1a1a1a; padding:20px; text-align:center; border-bottom:3px solid {b_color}; margin-bottom:10px;'>
                <p style='font-family:Orbitron; font-size:18px; margin:0; color:white;'>{name}</p>
                <p style='color:{'red' if score > 90 else 'white'}; font-weight:bold; margin-top:5px;'>{score}%</p>
            </div>
        """, unsafe_allow_html=True)
