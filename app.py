import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="HediAyoub - Predator V19", layout="wide", initial_sidebar_state="collapsed")

# CSS FINAL (Nettoyage total des graphiques)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    .stApp { background-color: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    
    /* Supprime les bordures et les axes inutiles des graphiques Streamlit */
    [data-testid="stMetric"], [data-testid="stMetricValue"] { display: none; }
    
    .stealth-card {
        background: #050505; border: 1px solid #111;
        border-left: 3px solid #ff0000; padding: 25px; margin-bottom: 20px;
    }
    .label-mini { color: #444; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; }
    .value-main { font-family: 'Orbitron'; font-size: 35px; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.session_state.auth = True # Bypass pour accès direct
    st.rerun()
else:
    # --- HEADER ---
    st.markdown("<h2 style='font-family:Orbitron; letter-spacing:5px;'>HEDI AYOUB // <span style='color:red;'>PREDATOR V19</span></h2>", unsafe_allow_html=True)
    st.markdown("<div style='height:1px; background:#111; margin-bottom:20px;'></div>", unsafe_allow_html=True)

    col_main, col_side = st.columns([2.8, 1.2])

    with col_main:
        # ZONE DE FOCUS
        st.markdown(f"""
            <div class='stealth-card'>
                <p class='label-mini'>Liquidity Engine Active</p>
                <h1 style='font-family:Orbitron; font-size:45px; margin:10px 0;'>NASDAQ-100 (NQ1!)</h1>
                <div style='display:flex; gap:60px; margin-top:20px;'>
                    <div><p class='label-mini'>Institutional Bias</p><p class='value-main' style='color:#ff0000;'>BULLISH</p></div>
                    <div><p class='label-mini'>Setup Confidence</p><p class='value-main'>99.2%</p></div>
                    <div><p class='label-mini'>Volatility</p><p class='value-main'>HIGH</p></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # NOUVEAU GRAPHIQUE : ON REMPLACE LA COURBE BLEUE PAR UNE VISUALISATION DE FLUX
        st.markdown("<p class='label-mini'>Neural Order Flow Simulation</p>", unsafe_allow_html=True)
        
        # On crée un graphique plus "pro" qui ressemble à un scanner de volume
        chart_data = pd.DataFrame(
            np.random.randint(10, 100, size=(20, 2)),
            columns=['Buy Pressure', 'Sell Pressure']
        )
        # Utilisation d'un bar_chart qui est bien plus lisible pour la liquidité
        st.bar_chart(chart_data, height=250, color=["#ff0000", "#111111"])

        # TABLE DES ORDRES
        st.markdown("<p class='label-mini' style='margin-top:30px;'>Active Operations</p>", unsafe_allow_html=True)
        st.markdown("""
            <table style='width: 100%; border-collapse: collapse; font-size: 12px;'>
                <tr style='color:#444; border-bottom:1px solid #111; text-align:left;'>
                    <th style='padding:10px;'>ASSET</th><th>TYPE</th><th>LOTS</th><th>TP / SL</th><th>PNL</th>
                </tr>
                <tr>
                    <td style='padding:15px 10px;'><b>NQ1!</b></td>
                    <td style='color:red;'>BUY MARKET</td>
                    <td>5.00</td>
                    <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                    <td style='color:#00ff41; font-family:Orbitron; font-size:16px;'>+$1,240.50</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

    with col_side:
        # RISK MANAGEMENT
        st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
        st.markdown("<p class='label-mini'>Risk Unit</p>", unsafe_allow_html=True)
        balance = st.number_input("Capital", value=100000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        lots = round((balance * (risk/100)) / 300, 2)
        st.markdown(f"<div style='text-align:center; margin-top:15px;'><p class='label-mini'>Size</p><p style='font-family:Orbitron; font-size:45px;'>{lots}</p></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # TIMER
        st.markdown("<div class='stealth-card' style='text-align:center;'>", unsafe_allow_html=True)
        components.html("""
            <div style="font-family:'Orbitron'; color:red; font-size:40px; font-weight:900; text-align:center;" id="t">00:00</div>
            <script>
                var s=300; setInterval(function(){
                    var m=Math.floor(s/60); var sec=s%60;
                    document.getElementById('t').innerHTML=(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec;
                    if(s>0)s--;else s=300;
                },1000);
            </script>
        """, height=60)
        st.markdown("<p class='label-mini'>Macro Window</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # MATRIX GRID
    st.markdown("<p class='label-mini' style='margin-top:20px;'>Global Matrix Scan</p>", unsafe_allow_html=True)
    m_cols = st.columns(5)
    assets = [("NQ", 99), ("ES", 85), ("XAU", 72), ("EURUSD", 96), ("BTC", 91)]
    for i, (name, score) in enumerate(assets):
        with m_cols[i]:
            st.markdown(f"<div style='background:#050505; border:1px solid #111; padding:15px; text-align:center; border-bottom:2px solid {'red' if score > 90 else '#111'}'><p style='color:#444; font-size:9px; margin:0;'>{name}</p><p style='font-family:Orbitron; font-size:18px; color:{'red' if score > 90 else '#fff'}; margin:0;'>{score}%</p></div>", unsafe_allow_html=True)
