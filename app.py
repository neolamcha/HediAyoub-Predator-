import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. INITIALISATION - On force le layout
st.set_page_config(page_title="HediAyoub - Predator V25", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE SURVIE (Force le noir et blanc partout)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    /* Global Noir */
    .stApp { background-color: #000 !important; color: #fff !important; font-family: 'JetBrains Mono', monospace; }
    
    /* FIX INPUTS : Fond Blanc, Texte Noir, Bordure Grise */
    div[data-baseweb="input"] { background-color: white !important; border: 2px solid #333 !important; border-radius: 4px !important; }
    input { color: black !important; font-weight: 800 !important; font-size: 18px !important; }
    
    /* FIX SLIDER */
    .stSlider [data-baseweb="slider"] { margin-bottom: 20px !important; }

    /* News Ticker */
    .news-ticker { background: #050505; border: 1px solid #111; padding: 10px; overflow: hidden; white-space: nowrap; margin-bottom: 20px; }
    .news-content { display: inline-block; animation: ticker 40s linear infinite; color: #ff0000; font-size: 12px; font-weight: bold; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* Cards */
    .stealth-card { background: #080808; border: 1px solid #151515; border-left: 4px solid #ff0000; padding: 20px; margin-bottom: 15px; }
    .label-mini { color: #555; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px; }
    
    /* Table Fix */
    .exec-table { width: 100%; border-collapse: collapse; background: #050505; }
    .exec-table th { color: #444; text-align: left; font-size: 9px; padding: 10px; border-bottom: 1px solid #111; }
    .exec-table td { padding: 12px 10px; font-size: 14px; border-bottom: 1px solid #080808; color: #eee; }

    /* Matrix de paires */
    .matrix-box {
        background: #080808; border: 1px solid #151515;
        padding: 15px 5px; text-align: center; border-radius: 2px;
        margin-bottom: 10px;
    }
    .pair-title { font-family: 'Orbitron'; font-size: 16px; font-weight: 900; color: #fff; margin:0; }
    .pair-pct { font-size: 13px; font-weight: bold; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

# 3. HEADER & NEWS
st.markdown("<div class='news-ticker'><div class='news-content'>⚡ SYSTEM NOTIFICATION: CORE V25 ONLINE • CROSS-ASSET CONFLUENCE SCANNING • VOLATILITY SPIKE ALERT ON NQ • HEDI AYOUB PREDATOR TERMINAL...</div></div>", unsafe_allow_html=True)

# 4. MAIN LAYOUT
col_left, col_right = st.columns([2.5, 1.5])

with col_right:
    # CALCULATEUR
    st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Account & Risk Unit</p>", unsafe_allow_html=True)
    
    # On utilise des colonnes internes pour mieux organiser l'espace
    acc_val = st.number_input("CAPITAL ($)", value=100000, step=1000)
    risk_p = st.slider("RISK %", 0.1, 5.0, 1.0, step=0.1)
    
    risk_m = acc_val * (risk_p / 100)
    lots = round(risk_m / 350, 2)
    
    st.markdown(f"""
        <div style='text-align:center; margin-top:15px; border-top:1px solid #111; padding-top:15px;'>
            <p class='label-mini'>Execution Size</p>
            <p style='font-family:Orbitron; font-size:50px; color:white; margin:0;'>{lots}</p>
            <p style='color:red; font-size:12px; font-weight:bold;'>MAX RISK: ${risk_m:,.2f}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # TIMER
    st.markdown("<div class='stealth-card' style='text-align:center; padding:10px;'>", unsafe_allow_html=True)
    components.html("""<div style="font-family:'Orbitron'; color:red; font-size:38px; font-weight:900; text-align:center;" id="t">00:00</div><script>var s=300; setInterval(function(){var m=Math.floor(s/60); var sec=s%60; document.getElementById('t').innerHTML=(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec; if(s>0)s--;else s=300;},1000);</script>""", height=50)
    st.markdown("<p class='label-mini'>Macro Impact</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_left:
    # FOCUS PAIR
    st.markdown(f"""
        <div class='stealth-card'>
            <p class='label-mini'>Neural Hunt Target</p>
            <h1 style='font-family:Orbitron; font-size:42px; margin:0;'>NASDAQ <span style='color:red;'>NQ1!</span></h1>
            <div style='display:flex; gap:40px; margin-top:10px;'>
                <div><p class='label-mini'>Confluence</p><p style='font-family:Orbitron; font-size:25px; color:red;'>99.2%</p></div>
                <div><p class='label-mini'>Bias</p><p style='font-family:Orbitron; font-size:25px; color:white;'>BULLISH</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # LIVE LOGS
    st.markdown("<p class='label-mini'>Active Execution Tracker</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='exec-table'>
            <tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>TP / SL</th><th>LIVE PNL</th></tr>
            <tr>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td><b style='font-family:Orbitron;'>{lots}</b></td>
                <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                <td style='color:#00ff41; font-family:Orbitron; font-size:18px;'>+${(lots * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

# --- MATRIX GLOBAL (10 Paires) ---
st.markdown("<br><p class='label-mini'>Market Intelligence Matrix</p>", unsafe_allow_html=True)

# Les 10 paires organisées en 5 colonnes sur 2 lignes
pairs = [
    ("NQ1!", 99.2), ("ES1!", 85.4), ("XAUUSD", 72.1), ("EURUSD", 96.5), ("GBPUSD", 88.3),
    ("BTCUSD", 91.0), ("USDJPY", 84.2), ("AUDUSD", 79.5), ("USDCAD", 82.7), ("ETHUSD", 65.4)
]

m_cols = st.columns(5)
for i, (name, score) in enumerate(pairs):
    with m_cols[i % 5]:
        color = "red" if score > 90 else "#444"
        border = "1px solid red" if score > 90 else "1px solid #151515"
        st.markdown(f"""
            <div class="matrix-box" style="border-bottom: 2px solid {color};">
                <p class="pair-title">{name}</p>
                <p class="pair-pct" style="color: {color};">{score}%</p>
            </div>
        """, unsafe_allow_html=True)

st.code(f"> TERMINAL_SYNC: V25 Operational. Inputs Locked. Matrix Scanning...", language="bash")
