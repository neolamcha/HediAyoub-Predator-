import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. SETUP GLOBAL
st.set_page_config(page_title="HediAyoub - Live Predator", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS POUR LE DYNAMISME ET LES NEWS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    .stApp { background-color: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    .stealth-card { background: #050505; border: 1px solid #111; border-left: 3px solid #ff0000; padding: 20px; margin-bottom: 20px; }
    .label-mini { color: #444; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; }
    
    /* Animation pour les News */
    .news-ticker { background: #050505; border: 1px solid #111; padding: 10px; overflow: hidden; white-space: nowrap; margin-bottom: 20px; }
    .news-content { display: inline-block; animation: ticker 30s linear infinite; color: #ff0000; font-size: 12px; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* Tableau */
    .exec-table { width: 100%; border-collapse: collapse; }
    .exec-table th { color: #333; text-align: left; font-size: 9px; padding: 10px; border-bottom: 1px solid #111; }
    .exec-table td { padding: 12px 10px; font-size: 14px; border-bottom: 1px solid #080808; }
    .pnl-green { color: #00ff41; font-family: 'Orbitron'; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. AUTHENTICATION (Simplifiée pour le déploiement)
if "auth" not in st.session_state: st.session_state.auth = True 

# --- HEADER NEWS TICKER ---
st.markdown("""
    <div class='news-ticker'>
        <div class='news-content'>
            ⚠️ HIGH IMPACT NEWS: FOMC MEETING IN 2H 15M • NASDAQ VOLATILITY INDEX AT PEAK • INSTITUTIONAL ACCUMULATION DETECTED ON NQ • DXY DIVERGENCE CONFIRMED • HEDIAYOUB PREDATOR CORE ONLINE...
        </div>
    </div>
""", unsafe_allow_html=True)

# --- CALCULATEUR (Placé AVANT pour que les variables existent) ---
with st.sidebar:
    st.markdown("<p class='label-mini'>Execution Settings</p>", unsafe_allow_html=True)
    bal = st.number_input("Account ($)", value=100000)
    risk_p = st.slider("Risk (%)", 0.1, 5.0, 1.0)
    
    # Calculs dynamiques
    risk_dollars = bal * (risk_p / 100)
    lots_dynamiques = round(risk_dollars / 350, 2)

# --- MAIN INTERFACE ---
c1, c2 = st.columns([2.8, 1.2])

with c1:
    # TARGET PANEL
    st.markdown(f"""
        <div class='stealth-card'>
            <p class='label-mini'>Current Hunting Target</p>
            <h1 style='font-family:Orbitron; font-size:40px; margin:0;'>NASDAQ-100 (NQ1!)</h1>
            <div style='display:flex; gap:40px; margin-top:15px;'>
                <div><p class='label-mini'>Risk per Trade</p><p style='font-size:24px; color:red;'>${risk_dollars:,.2f}</p></div>
                <div><p class='label-mini'>Neural Bias</p><p style='font-size:24px;'>BULLISH</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # TABLEAU DYNAMIQUE (Ici on utilise les variables !)
    st.markdown("<p class='label-mini'>Live Execution Tracker</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='exec-table'>
            <tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>ENTRY</th><th>TP / SL</th><th>LIVE PNL</th></tr>
            <tr>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td><b style='font-size:18px; color:white;'>{lots_dynamiques}</b></td>
                <td>18245.25</td>
                <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                <td class='pnl-green'>+${(lots_dynamiques * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

with c2:
    # RISK CARD
    st.markdown(f"""
        <div class='stealth-card' style='text-align:center;'>
            <p class='label-mini'>Calculated Size</p>
            <p style='font-family:Orbitron; font-size:55px; margin:0;'>{lots_dynamiques}</p>
            <p style='color:#444; font-size:10px;'>LOTS BASED ON {risk_p}% RISK</p>
        </div>
    """, unsafe_allow_html=True)

    # TIMER
    st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
    components.html("""
        <div style="font-family:'Orbitron'; color:red; font-size:35px; font-weight:900; text-align:center;" id="t">00:00</div>
        <script>
            var s=450; setInterval(function(){
                var m=Math.floor(s/60); var sec=s%60;
                document.getElementById('t').innerHTML=(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec;
                if(s>0)s--;else s=450;
            },1000);
        </script>
    """, height=50)
    st.markdown("<p class='label-mini' style='text-align:center;'>Macro Collision</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# MATRIX
st.markdown("<p class='label-mini'>Global Neural Scan</p>", unsafe_allow_html=True)
m_cols = st.columns(5)
assets = [("NQ", 99), ("ES", 85), ("XAU", 72), ("EURUSD", 96), ("BTC", 91)]
for i, (name, score) in enumerate(assets):
    with m_cols[i]:
        st.markdown(f"<div style='background:#050505; border:1px solid #111; padding:10px; text-align:center; border-bottom:2px solid {'red' if score > 90 else '#111'}'><p style='color:#444; font-size:9px; margin:0;'>{name}</p><p style='font-family:Orbitron; color:{'red' if score > 90 else '#fff'}; margin:0;'>{score}%</p></div>", unsafe_allow_html=True)
