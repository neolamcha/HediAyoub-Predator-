import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. INITIALISATION
st.set_page_config(page_title="HediAyoub - Predator V23", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS ULTIME (Correction de la visibilité des inputs)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    .stApp { background-color: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }

    /* --- CORRECTION VISIBILITÉ INPUTS --- */
    /* On force le fond en blanc et le texte en noir pour les champs de saisie */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border-radius: 4px !important;
    }
    input {
        color: #000000 !important; /* Texte Noir */
        font-weight: bold !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    /* Style du label (le titre au-dessus de la boîte) */
    label {
        color: #444 !important;
        font-size: 10px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
    }

    /* News Ticker */
    .news-ticker { background: #050505; border: 1px solid #111; padding: 8px; overflow: hidden; white-space: nowrap; margin-bottom: 20px; }
    .news-content { display: inline-block; animation: ticker 40s linear infinite; color: #ff0000; font-size: 11px; letter-spacing: 2px; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* Stealth Cards */
    .stealth-card { background: #050505; border: 1px solid #111; border-left: 3px solid #ff0000; padding: 20px; margin-bottom: 15px; }
    .label-mini { color: #444; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 8px; }
    
    /* Table */
    .exec-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .exec-table th { color: #333; text-align: left; font-size: 9px; padding: 10px; border-bottom: 1px solid #111; }
    .exec-table td { padding: 12px 10px; font-size: 14px; border-bottom: 1px solid #080808; }
</style>
""", unsafe_allow_html=True)

# 3. AUTH (Bypass)
st.session_state.auth = True 

# --- NEWS TICKER ---
st.markdown("""
    <div class='news-ticker'>
        <div class='news-content'>
            ⚡ BREAKING: NQ LIQUIDITY SWEEP DETECTED • US CPI DATA EXPECTED VOLATILITY • INSTITUTIONAL ORDER FLOW ALIGNED BULLISH • PREDATOR SYSTEM V23 ONLINE...
        </div>
    </div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([2.8, 1.2])

with col_right:
    # --- MODULE DE GESTION DU COMPTE ---
    st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Account Control</p>", unsafe_allow_html=True)
    
    # Ici les inputs seront Blanc avec texte Noir grâce au CSS ci-dessus
    account_val = st.number_input("CAPITAL ($)", value=100000, step=1000)
    risk_percent = st.slider("RISK EXPOSURE (%)", 0.1, 5.0, 1.0, step=0.1)
    
    risk_money = account_val * (risk_percent / 100)
    lots = round(risk_money / 350, 2)
    
    st.markdown(f"""
        <div style='text-align:center; margin-top:20px; padding-top:15px; border-top:1px solid #111;'>
            <p class='label-mini'>Neural Lot Size</p>
            <p style='font-family:Orbitron; font-size:55px; color:white; margin:0;'>{lots}</p>
            <p style='color:red; font-size:11px; font-weight:bold;'>MAX RISK: ${risk_money:,.2f}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # TIMER
    st.markdown("<div class='stealth-card' style='text-align:center;'>", unsafe_allow_html=True)
    components.html("""
        <div style="font-family:'Orbitron'; color:red; font-size:40px; font-weight:900; text-align:center;" id="t">00:00</div>
        <script>
            var s=450; setInterval(function(){
                var m=Math.floor(s/60); var sec=s%60;
                document.getElementById('t').innerHTML=(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec;
                if(s>0)s--;else s=450;
            },1000);
        </script>
    """, height=55)
    st.markdown("<p class='label-mini'>Macro Impact Timer</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_left:
    # FOCUS PANEL
    st.markdown(f"""
        <div class='stealth-card'>
            <p class='label-mini'>Target Identification</p>
            <h1 style='font-family:Orbitron; font-size:45px; margin:0;'>NASDAQ-100 <span style='color:red;'>NQ1!</span></h1>
            <div style='display:flex; gap:50px; margin-top:15px;'>
                <div><p class='label-mini'>Confluence Score</p><p style='font-family:Orbitron; font-size:28px; color:red;'>99.2%</p></div>
                <div><p class='label-mini'>System Bias</p><p style='font-family:Orbitron; font-size:28px;'>BULLISH</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # TABLEAU D'EXÉCUTION DYNAMIQUE
    st.markdown("<p class='label-mini'>Live Order Matrix</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='exec-table'>
            <tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>ENTRY</th><th>TP / SL</th><th>LIVE PNL</th></tr>
            <tr>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td><b style='font-family:Orbitron; font-size:18px; color:white;'>{lots}</b></td>
                <td>18245.25</td>
                <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                <td style='color:#00ff41; font-family:Orbitron; font-size:18px;'>+${(lots * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

    # GRAPHIQUE DE PRESSION
    st.markdown("<br><p class='label-mini'>Institutional Order Flow</p>", unsafe_allow_html=True)
    c_data = pd.DataFrame(np.random.randint(10, 100, size=(20, 2)), columns=['Buys', 'Sells'])
    st.bar_chart(c_data, height=200, color=["#ff0000", "#111111"])

# MATRIX GLOBAL
st.markdown("<p class='label-mini' style='margin-top:20px;'>Global Neural Scan</p>", unsafe_allow_html=True)
m_cols = st.columns(5)
assets = [("NQ", 99), ("ES", 85), ("XAU", 72), ("EURUSD", 96), ("BTC", 91)]
for i, (name, score) in enumerate(assets):
    with m_cols[i]:
        st.markdown(f"<div style='background:#050505; border:1px solid #111; padding:12px; text-align:center; border-bottom:2px solid {'red' if score > 90 else '#111'}'><p style='color:#444; font-size:9px; margin:0;'>{name}</p><p style='font-family:Orbitron; font-size:18px; color:{'red' if score > 90 else '#fff'}; margin:0;'>{score}%</p></div>", unsafe_allow_html=True)
