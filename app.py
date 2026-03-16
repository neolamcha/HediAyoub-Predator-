import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. SETUP
st.set_page_config(page_title="HediAyoub Predator V26", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE FORCE BRUTE (Noir total, texte lisible, inputs blancs)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    
    /* FIX INPUTS : FOND BLANC TEXTE NOIR */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 4px !important; }
    input { color: #000000 !important; font-weight: 900 !important; }
    label { color: #aaaaaa !important; font-size: 12px !important; }

    /* CARDS */
    .card { background: #080808; border: 1px solid #1a1a1a; border-left: 4px solid #ff0000; padding: 20px; margin-bottom: 20px; }
    .title-small { color: #444; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; }
    
    /* TABLE */
    .trading-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .trading-table th { color: #444; text-align: left; font-size: 10px; padding: 10px; border-bottom: 1px solid #222; }
    .trading-table td { padding: 15px 10px; font-size: 14px; border-bottom: 1px solid #0a0a0a; }

    /* MATRIX (Les 10 paires) */
    .matrix-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
    .matrix-box { 
        flex: 1 1 calc(18% - 10px); min-width: 120px;
        background: #080808; border: 1px solid #1a1a1a; 
        padding: 15px; text-align: center; border-bottom: 2px solid #333;
    }
    .pair-name { font-family: 'Orbitron'; font-size: 16px; font-weight: 700; color: #fff; margin:0; }
    .pair-val { font-size: 13px; font-weight: bold; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER NEWS ---
st.markdown(f"""
    <div style='background: #050505; border: 1px solid #111; padding: 10px; color: red; font-size: 12px; text-align: center; font-weight: bold;'>
        ⚠️ NEWS: FOMC VOLATILITY ALERT • CROSS-ASSET SCANNING ACTIVE • PREDATOR V26 • {datetime.now().strftime('%H:%M:%S')}
    </div><br>
""", unsafe_allow_html=True)

# --- LAYOUT PRINCIPAL ---
col_left, col_right = st.columns([2.8, 1.2])

with col_right:
    # CALCULATEUR
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='title-small'>Risk Management</p>", unsafe_allow_html=True)
    
    account = st.number_input("ACCOUNT ($)", value=100000, step=1000)
    risk_p = st.slider("RISK %", 0.1, 5.0, 1.0, step=0.1)
    
    risk_money = account * (risk_p / 100)
    lots = round(risk_money / 350, 2)
    
    st.markdown(f"""
        <div style='text-align:center; margin-top:20px; border-top:1px solid #1a1a1a; padding-top:15px;'>
            <p class='title-small'>Position Size</p>
            <p style='font-family:Orbitron; font-size:50px; margin:0;'>{lots}</p>
            <p style='color:red; font-weight:bold;'>MAX RISK: ${risk_money:,.2f}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # MACRO TIMER SIMPLE (Sans JS complexe pour éviter l'écran noir)
    st.markdown(f"""
        <div class='card' style='text-align:center;'>
            <p class='title-small'>Macro Collision</p>
            <p style='font-family:Orbitron; font-size:35px; color:red; margin:5px 0;'>07:42</p>
            <p style='color:#333; font-size:9px;'>MINUTES REMAINING</p>
        </div>
    """, unsafe_allow_html=True)

with col_left:
    # FOCUS PAIR
    st.markdown(f"""
        <div class='card'>
            <p class='title-small'>Main Hunter Target</p>
            <h1 style='font-family:Orbitron; font-size:45px; margin:0;'>NASDAQ <span style='color:red;'>NQ1!</span></h1>
            <div style='display:flex; gap:50px; margin-top:15px;'>
                <div><p class='title-small'>Confluence</p><p style='font-family:Orbitron; font-size:30px; color:red;'>99.2%</p></div>
                <div><p class='title-small'>Bias</p><p style='font-family:Orbitron; font-size:30px;'>BULLISH</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ACTIVE TRADES
    st.markdown("<p class='title-small'>Live Execution logs</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='trading-table'>
            <tr style='border-bottom: 2px solid #111;'><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>TP / SL</th><th>PNL</th></tr>
            <tr>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td><b style='font-size:18px;'>{lots}</b></td>
                <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                <td style='color:#00ff41; font-family:Orbitron; font-size:18px;'>+${(lots * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

# --- LES 10 PAIRES EN BAS (FIX TOTAL) ---
st.markdown("<br><p class='title-small'>Global Neural Matrix (10 Assets)</p>", unsafe_allow_html=True)

pairs = [
    ("NQ1!", 99.2), ("ES1!", 85.4), ("XAUUSD", 72.1), ("EURUSD", 96.5), ("GBPUSD", 88.3),
    ("BTCUSD", 91.0), ("USDJPY", 84.2), ("AUDUSD", 79.5), ("USDCAD", 82.7), ("ETHUSD", 65.4)
]

# On crée une structure flexible qui s'adapte à l'écran
html_matrix = "<div class='matrix-grid'>"
for name, score in pairs:
    color = "red" if score > 90 else "#ffffff"
    border = "red" if score > 90 else "#333"
    html_matrix += f"""
        <div class="matrix-box" style="border-bottom: 2px solid {border};">
            <p class="pair-name">{name}</p>
            <p class="pair-val" style="color: {color};">{score}%</p>
        </div>
    """
html_matrix += "</div>"
st.markdown(html_matrix, unsafe_allow_html=True)

st.code("> SYSTEM_V26: All modules visible. Risk Engine Synchronized.", language="bash")
