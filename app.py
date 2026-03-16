import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. SETUP
st.set_page_config(page_title="Predator V33 - MTF Fusion", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS AVANCÉ (Scanner & Fusion)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    
    .card { background: #080808; border: 1px solid #1a1a1a; border-left: 4px solid #ff0000; padding: 20px; margin-bottom: 15px; }
    .label-mini { color: #555; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; font-weight: 800; }
    
    /* MTF SCANNER STYLING */
    .mtf-badge { padding: 4px 8px; border-radius: 3px; font-size: 10px; font-weight: bold; margin-bottom: 5px; text-align: center;}
    .bullish { background: rgba(0, 255, 65, 0.1); color: #00ff41; border: 1px solid #00ff41; }
    .bearish { background: rgba(255, 0, 0, 0.1); color: #ff0000; border: 1px solid #ff0000; }
    
    /* A+ FUSION INDICATOR */
    .fusion-active { color: #ff0000; font-family: 'Orbitron'; font-weight: 900; animation: blink 1s infinite; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
</style>
""", unsafe_allow_html=True)

# 3. HEADER
st.markdown(f"<div style='padding: 10px 20px; background: #050505; border-bottom: 1px solid #111; color:red; font-family:Orbitron; font-weight:900;'>PREDATOR_V33 // MTF ALGORITHMIC FUSION</div><br>", unsafe_allow_html=True)

col_scan, col_main, col_risk = st.columns([0.6, 2.4, 1])

with col_scan:
    # --- SCANNER MTF ---
    st.markdown("<p class='label-mini'>MTF Scanner</p>", unsafe_allow_html=True)
    
    def mtf_row(label, bias):
        cls = "bullish" if bias == "BULL" else "bearish"
        return f"<div style='display:flex; justify-content:space-between; margin-bottom:10px;'><span style='font-size:12px;'>{label}</span><span class='mtf-badge {cls}'>{bias}</span></div>"
    
    st.markdown(f"""
        <div class='card' style='padding:15px;'>
            {mtf_row("1D DAILY", "BULL")}
            {mtf_row("1H H4/H1", "BULL")}
            {mtf_row("15M ITF", "BULL")}
            {mtf_row("5M LTF", "BULL")}
            <hr style='border: 0.5px solid #222;'>
            <p style='font-size:9px; color:#444;'>FUSION STATUS</p>
            <p class='fusion-active' style='font-size:14px;'>A+ SYNCED</p>
        </div>
    """, unsafe_allow_html=True)

with col_risk:
    # --- RISK & CALCULATOR ---
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Risk Unit</p>", unsafe_allow_html=True)
    cap = st.number_input("ACCOUNT ($)", value=100000)
    r_pct = st.slider("RISK (%)", 0.1, 5.0, 1.0)
    l_size = round((cap * (r_pct / 100)) / 350, 2)
    st.markdown(f"<p style='font-family:Orbitron; font-size:40px; text-align:center; margin:0;'>{l_size}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # TIMER (DYNAMIQUE)
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
    # --- CHART MULTI-TF ---
    st.markdown("<div class='card' style='padding:5px;'>", unsafe_allow_html=True)
    components.html("""
        <div id="tv_chart" style="height:450px;"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true, "symbol": "CME_MINI:NQ1!", "interval": "15", "theme": "dark", 
          "style": "1", "locale": "fr", "container_id": "tv_chart", "backgroundColor": "#000000",
          "withdateranges": true, "hide_side_toolbar": false, "details": true, "hotlist": true,
          "studies": ["STD;Fair_Value_Gap", "STD;Stochastic_RSI"]
        });
        </script>
    """, height=450)
    st.markdown("</div>", unsafe_allow_html=True)

# --- EXECUTION TABLE WITH TP/SL ---
st.markdown("<p class='label-mini' style='padding-left:10px;'>A+ Execution Protocol</p>", unsafe_allow_html=True)
st.markdown(f"""
    <table style='width:100%; border-collapse: collapse; background:#050505;'>
        <tr style='border-bottom: 2px solid #111;'>
            <th style='text-align:left; padding:12px; font-size:10px; color:#444;'>ASSET</th>
            <th style='text-align:left; padding:12px; font-size:10px; color:#444;'>FUSION BIAS</th>
            <th style='text-align:left; padding:12px; font-size:10px; color:#444;'>ENTRY</th>
            <th style='text-align:left; padding:12px; font-size:10px; color:#00ff41;'>TP (4R)</th>
            <th style='text-align:left; padding:12px; font-size:10px; color:#ff0000;'>SL</th>
            <th style='text-align:left; padding:12px; font-size:10px; color:#444;'>PROJECTION</th>
        </tr>
        <tr>
            <td style='padding:15px;'><b>NQ1!</b></td>
            <td style='padding:15px; color:#00ff41;'>FULL BULL SYNC</td>
            <td style='padding:15px;'>18245.25</td>
            <td style='padding:15px; color:#00ff41; font-weight:bold;'>18420.00</td>
            <td style='padding:15px; color:#ff0000; font-weight:bold;'>18190.00</td>
            <td style='padding:15px; font-family:Orbitron; color:#00ff41;'>+${(l_size * 248):,.2f}</td>
        </tr>
    </table>
""", unsafe_allow_html=True)

# --- GLOBAL MATRIX (10 ASSETS) ---
st.markdown("<br><p class='label-mini' style='padding-left:10px;'>Global Neural Matrix - MTF Scanning</p>", unsafe_allow_html=True)
assets = [("NQ1!", 99), ("ES1!", 88), ("XAUUSD", 94), ("EURUSD", 96), ("GBPUSD", 82),
          ("BTCUSD", 91), ("USDJPY", 74), ("AUDUSD", 79), ("USDCAD", 85), ("ETHUSD", 68)]
m_cols = st.columns(5)
for i, (name, score) in enumerate(assets):
    with m_cols[i % 5]:
        st.markdown(f"<div style='background:#080808; border:1px solid #1a1a1a; padding:15px; text-align:center; border-bottom:3px solid {'red' if score > 90 else '#333'};'><p style='font-family:Orbitron; font-size:14px; margin:0;'>{name}</p><p style='color:{'red' if score > 90 else 'white'}; font-weight:bold; margin:0;'>{score}%</p></div>", unsafe_allow_html=True)
