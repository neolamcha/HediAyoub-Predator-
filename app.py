import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. SETUP
st.set_page_config(page_title="HediAyoub Predator V32", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS 
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 4px !important; }
    input { color: #000000 !important; font-weight: 900 !important; }
    
    .card { background: #080808; border: 1px solid #1a1a1a; border-left: 4px solid #ff0000; padding: 20px; margin-bottom: 15px; }
    .label-mini { color: #555; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; font-weight: 800; }
    
    /* TABLE STYLING */
    .exec-table { width: 100%; border-collapse: collapse; margin-top: 10px; background: #050505; }
    .exec-table th { color: #444; text-align: left; font-size: 10px; padding: 12px; border-bottom: 2px solid #111; }
    .exec-table td { padding: 15px 12px; font-size: 15px; border-bottom: 1px solid #0a0a0a; font-family: 'JetBrains Mono'; }
</style>
""", unsafe_allow_html=True)

# 3. HEADER
st.markdown(f"<div style='padding: 10px 20px; background: #050505; border-bottom: 1px solid #111; color:red; font-family:Orbitron; font-weight:900;'>PREDATOR_V32 // LIVE EXECUTION</div><br>", unsafe_allow_html=True)

col_main, col_side = st.columns([3, 1])

with col_side:
    # RISK MODULE
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Account Risk</p>", unsafe_allow_html=True)
    cap = st.number_input("ACCOUNT ($)", value=100000)
    r_pct = st.slider("RISK (%)", 0.1, 5.0, 1.0)
    risk_money = cap * (r_pct / 100)
    l_size = round(risk_money / 350, 2)
    st.markdown(f"<p style='font-family:Orbitron; font-size:40px; text-align:center; margin:0;'>{l_size}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # A+ BADGE & TIMER
    st.markdown(f"""
        <div style='background: linear-gradient(90deg, #1a0000, #000); border: 2px solid #ff0000; padding: 15px; text-align: center; border-radius: 8px; margin-bottom:15px;'>
            <p style='color:red; font-family:Orbitron; font-size:10px; margin:0;'>PREDATOR SETUP</p>
            <h2 style='color:white; font-family:Orbitron; margin:5px 0;'>GRADE A+</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
    components.html("""
        <div id="t" style="font-family:'Orbitron'; color:red; font-size:35px; font-weight:900; text-align:center;">08:14</div>
        <script>
            let s = 494; setInterval(() => {
                let m = Math.floor(s/60); let sec = s%60;
                document.getElementById('t').innerHTML = (m<10?'0':'')+m+":"+(sec<10?'0':'')+sec;
                if(s>0) s--; else document.getElementById('t').innerHTML="OPEN";
            }, 1000);
        </script>
    """, height=40)
    st.markdown("<p class='label-mini'>Macro Window</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_main:
    # CHART
    st.markdown("<div class='card' style='padding:10px;'>", unsafe_allow_html=True)
    components.html("""
        <div id="tv_chart" style="height:400px;"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true, "symbol": "CME_MINI:NQ1!", "interval": "5", "theme": "dark", 
          "style": "1", "locale": "fr", "container_id": "tv_chart", "backgroundColor": "#000000"
        });
        </script>
    """, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- TABLEAU TP / SL RÉINTEGRÉ ---
    st.markdown("<p class='label-mini'>Active Orders & Targets</p>", unsafe_allow_html=True)
    st.markdown(f"""
        <table class='exec-table'>
            <tr>
                <th>ASSET</th>
                <th>TYPE</th>
                <th>ENTRY</th>
                <th style='color:#00ff41;'>TAKE PROFIT</th>
                <th style='color:#ff0000;'>STOP LOSS</th>
                <th>PNL</th>
            </tr>
            <tr>
                <td><b>NQ1!</b></td>
                <td style='color:red;'>BUY MARKET</td>
                <td>18245.25</td>
                <td style='color:#00ff41; font-weight:bold;'>18420.00</td>
                <td style='color:#ff0000; font-weight:bold;'>18190.00</td>
                <td style='color:#00ff41; font-family:Orbitron;'>+${(l_size * 248):,.2f}</td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

# MATRIX 10 ASSETS
st.markdown("<br><p class='label-mini'>Neural Matrix</p>", unsafe_allow_html=True)
assets = [("NQ1!", 99), ("ES1!", 88), ("XAUUSD", 94), ("EURUSD", 96), ("GBPUSD", 82),
          ("BTCUSD", 91), ("USDJPY", 74), ("AUDUSD", 79), ("USDCAD", 85), ("ETHUSD", 68)]
m_cols = st.columns(5)
for i, (name, score) in enumerate(assets):
    with m_cols[i % 5]:
        st.markdown(f"<div style='background:#080808; border:1px solid #1a1a1a; padding:15px; text-align:center; border-bottom:3px solid {'red' if score > 90 else '#333'}; margin-bottom:10px;'><p style='font-family:Orbitron; font-size:14px; margin:0;'>{name}</p><p style='color:{'red' if score > 90 else 'white'}; font-weight:bold; margin:0;'>{score}%</p></div>", unsafe_allow_html=True)
