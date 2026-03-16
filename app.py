import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. INITIALISATION
st.set_page_config(page_title="HediAyoub - Predator V24", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE PRÉCISION
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    .stApp { background-color: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    
    /* Inputs Lisibles */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 4px !important; }
    input { color: #000000 !important; font-weight: bold !important; }
    label { color: #888 !important; font-size: 10px !important; letter-spacing: 2px !important; text-transform: uppercase !important; }

    /* News Ticker */
    .news-ticker { background: #050505; border: 1px solid #111; padding: 10px; overflow: hidden; white-space: nowrap; margin-bottom: 25px; }
    .news-content { display: inline-block; animation: ticker 45s linear infinite; color: #ff0000; font-size: 12px; font-weight: bold; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* Stealth Cards */
    .stealth-card { background: #050505; border: 1px solid #111; border-left: 4px solid #ff0000; padding: 25px; margin-bottom: 20px; }
    .label-mini { color: #666; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px; }
    
    /* Table d'exécution */
    .exec-table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    .exec-table th { color: #444; text-align: left; font-size: 10px; padding: 12px; border-bottom: 1px solid #222; }
    .exec-table td { padding: 15px 12px; font-size: 15px; border-bottom: 1px solid #111; }

    /* Matrix Grid - NEW LOOK */
    .matrix-container {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 15px;
        margin-top: 20px;
    }
    .matrix-item {
        background: #080808;
        border: 1px solid #151515;
        padding: 20px 10px;
        text-align: center;
        transition: 0.3s;
    }
    .matrix-item:hover { border: 1px solid #ff0000; background: #0c0000; }
    .pair-name { color: #fff; font-family: 'Orbitron'; font-size: 18px; font-weight: 900; margin: 0; letter-spacing: 1px; }
    .pair-score { font-size: 14px; margin-top: 5px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- LOGIN BYPASS ---
st.session_state.auth = True 

# --- NEWS TICKER ---
st.markdown("<div class='news-ticker'><div class='news-content'>⚡ MARKET UPDATE: NQ REACHING CRITICAL SUPPLY ZONE • XAUUSD SHOWING SMT DIVERGENCE • FED SPEECH INBOUND • PREDATOR ALGORITHM MONITORING 10+ ASSETS...</div></div>", unsafe_allow_html=True)

col_left, col_right = st.columns([2.8, 1.2])

with col_right:
    st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Account & Risk</p>", unsafe_allow_html=True)
    acc_val = st.number_input("ACCOUNT ($)", value=100000)
    r_pct = st.slider("RISK %", 0.1, 5.0, 1.0)
    r_money = acc_val * (r_pct / 100)
    lots = round(r_money / 350, 2)
    st.markdown(f"<div style='text-align:center; margin-top:20px;'><p class='label-mini'>Lot Size</p><p style='font-family:Orbitron; font-size:55px; margin:0;'>{lots}</p><p style='color:red; font-size:12px;'>RISK: ${r_money:,.2f}</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='stealth-card' style='text-align:center;'>", unsafe_allow_html=True)
    components.html("""<div style="font-family:'Orbitron'; color:red; font-size:40px; font-weight:900; text-align:center;" id="t">00:00</div><script>var s=300; setInterval(function(){var m=Math.floor(s/60); var sec=s%60; document.getElementById('t').innerHTML=(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec; if(s>0)s--;else s=300;},1000);</script>""", height=55)
    st.markdown("<p class='label-mini'>Macro Timer</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_left:
    st.markdown(f"<div class='stealth-card'><p class='label-mini'>Primary Hunter</p><h1 style='font-family:Orbitron; font-size:50px; margin:0;'>NASDAQ <span style='color:red;'>NQ1!</span></h1><div style='display:flex; gap:60px; margin-top:15px;'><div><p class='label-mini'>Confluence</p><p style='font-family:Orbitron; font-size:30px; color:red;'>99.2%</p></div><div><p class='label-mini'>Neural Bias</p><p style='font-family:Orbitron; font-size:30px;'>BULLISH</p></div></div></div>", unsafe_allow_html=True)

    st.markdown("<p class='label-mini'>Active Execution Matrix</p>", unsafe_allow_html=True)
    st.markdown(f"""<table class='exec-table'><tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>ENTRY</th><th>TP / SL</th><th>PNL</th></tr><tr><td><b>NQ1!</b></td><td style='color:red;'>BUY MARKET</td><td><b>{lots}</b></td><td>18245.25</td><td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td><td style='color:#00ff41; font-family:Orbitron; font-size:18px;'>+${(lots * 248):,.2f}</td></tr></table>""", unsafe_allow_html=True)

# --- SECTION DES 10 PAIRES (LA MATRICE) ---
st.markdown("<br><p class='label-mini'>Global Asset Intelligence (All Pairs)</p>", unsafe_allow_html=True)

# Liste des 10 actifs
matrix_data = [
    ("NQ1!", 99.2), ("ES1!", 85.4), ("XAUUSD", 72.1), ("EURUSD", 96.5), ("GBPUSD", 88.3),
    ("BTCUSD", 91.0), ("USDJPY", 84.2), ("AUDUSD", 79.5), ("USDCAD", 82.7), ("ETHUSD", 65.4)
]

# Génération de la grille HTML
cols_html = ""
for name, score in matrix_data:
    color = "#ff0000" if score > 90 else "#ffffff"
    border = "2px solid #ff0000" if score > 90 else "1px solid #151515"
    cols_html += f"""
        <div class="matrix-item" style="border-bottom: {border};">
            <p class="pair-name">{name}</p>
            <p class="pair-score" style="color: {color};">{score}%</p>
        </div>
    """

st.markdown(f"<div class='matrix-container'>{cols_html}</div>", unsafe_allow_html=True)

st.code("> PREDATOR_V24: Global Matrix Synchronized. 10/10 Assets Tracked.", language="bash")
