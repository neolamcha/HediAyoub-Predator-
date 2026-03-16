import streamlit as st
import pandas as pd
import numpy as np

# 1. INITIALISATION
st.set_page_config(page_title="HediAyoub Predator V27", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE STABILISATION (Noir total, inputs clairs)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    
    /* On force la visibilité des blocs de saisie */
    .stNumberInput, .stSlider {
        background-color: #080808 !important;
        padding: 10px !important;
        border-radius: 5px !important;
        border: 1px solid #1a1a1a !important;
    }
    
    /* Cartes */
    .stealth-card { 
        background: #080808; 
        border: 1px solid #1a1a1a; 
        border-left: 4px solid #ff0000; 
        padding: 20px; 
        margin-bottom: 20px; 
    }
    
    .label-mini { color: #555; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px; }
    
    /* Tableau */
    .trading-table { width: 100%; border-collapse: collapse; background: #050505; }
    .trading-table th { color: #444; text-align: left; font-size: 10px; padding: 10px; border-bottom: 1px solid #222; }
    .trading-table td { padding: 15px 10px; font-size: 14px; border-bottom: 1px solid #0a0a0a; }

    /* Matrix */
    .matrix-item {
        background: #080808; border: 1px solid #1a1a1a;
        padding: 15px; text-align: center; border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# 3. HEADER
st.markdown("<h2 style='font-family:Orbitron; letter-spacing:3px;'>HEDI AYOUB // <span style='color:red;'>PREDATOR V27</span></h2>", unsafe_allow_html=True)
st.markdown("<div style='height:2px; background:linear-gradient(90deg, #ff0000, transparent); margin-bottom:20px;'></div>", unsafe_allow_html=True)

# 4. CONTENU PRINCIPAL
col_main, col_risk = st.columns([2.5, 1.5])

with col_risk:
    st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Risk Unit Settings</p>", unsafe_allow_html=True)
    
    # CALCULS DYNAMIQUES (Variables locales)
    capital = st.number_input("ACCOUNT CAPITAL ($)", value=100000, step=1000)
    risk_percent = st.slider("RISK PERCENTAGE (%)", 0.1, 5.0, 1.0, step=0.1)
    
    risk_amount = capital * (risk_percent / 100)
    lots_calc = round(risk_amount / 350, 2) # Formule NQ
    
    st.markdown(f"""
        <div style='text-align:center; margin-top:20px; border-top:1px solid #1a1a1a; padding-top:15px;'>
            <p class='label-mini'>Calculated Lot Size</p>
            <p style='font-family:Orbitron; font-size:55px; color:white; margin:0;'>{lots_calc}</p>
            <p style='color:red; font-weight:bold; font-size:14px;'>-$ {risk_amount:,.2f}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Timer Statique pour éviter les bugs JS
    st.markdown(f"""
        <div class='stealth-card' style='text-align:center; padding:10px;'>
            <p class='label-mini'>Macro Window</p>
            <p style='font-family:Orbitron; font-size:35px; color:red; margin:0;'>08:14</p>
        </div>
    """, unsafe_allow_html=True)

with col_main:
    # FOCUS PANEL
    st.markdown(f"""
        <div class='stealth-card'>
            <p class='label-mini'>Target Identification</p>
            <h1 style='font-family:Orbitron; font-size:45px; margin:0;'>NASDAQ <span style='color:red;'>NQ1!</span></h1>
            <div style='display:flex; gap:50px; margin-top:15px;'>
                <div><p class='label-mini'>Confluence</p><p style='font-family:Orbitron; font-size:28px; color:red;'>99.2%</p></div>
                <div><p class='label-mini'>Bias</p><p style='font-family:Orbitron; font-size:28px;'>BULLISH</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # TABLEAU D'EXÉCUTION
    st.markdown("<p class='label-mini'>Active Execution Tracker</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='trading-table'>
            <tr><th>SYMBOL</th><th>TYPE</th><th>LOTS</th><th>TP / SL</th><th>PNL</th></tr>
            <tr>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td><b style='font-family:Orbitron; font-size:18px;'>{lots_calc}</b></td>
                <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                <td style='color:#00ff41; font-family:Orbitron; font-size:18px;'>+${(lots_calc * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

# 5. MATRIX (LES 10 PAIRES)
st.markdown("<br><p class='label-mini'>Market Intelligence Matrix</p>", unsafe_allow_html=True)
m_assets = [
    ("NQ1!", 99.2), ("ES1!", 85.4), ("XAUUSD", 72.1), ("EURUSD", 96.5), ("GBPUSD", 88.3),
    ("BTCUSD", 91.0), ("USDJPY", 84.2), ("AUDUSD", 79.5), ("USDCAD", 82.7), ("ETHUSD", 65.4)
]

cols = st.columns(5)
for i, (name, score) in enumerate(m_assets):
    with cols[i % 5]:
        status_color = "red" if score > 90 else "#333"
        st.markdown(f"""
            <div class='matrix-item' style='border-bottom: 3px solid {status_color}; margin-bottom:10px;'>
                <p style='font-family:Orbitron; font-size:16px; margin:0;'>{name}</p>
                <p style='color:{status_color}; font-weight:bold; margin:0;'>{score}%</p>
            </div>
        """, unsafe_allow_html=True)

st.code("> SYSTEM_V27: Stable Mode Active. All UI elements locked.", language="bash")
