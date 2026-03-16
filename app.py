import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. ENGINE CONFIG
st.set_page_config(page_title="HediAyoub - Singularity", layout="wide", initial_sidebar_state="collapsed")

# 2. DESIGN : PURE BLACK INJECTION (Zéro cases blanches)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    .stApp { background-color: #000000 !important; color: #ffffff !important; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .block-container { padding: 1rem 3rem !important; }

    /* Remplacement des cases blanches par du texte flottant */
    .data-block {
        border-left: 2px solid #ff0000;
        padding-left: 15px;
        margin-bottom: 20px;
    }
    .data-label { color: #444; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin: 0; }
    .data-value { color: #fff; font-family: 'Orbitron'; font-size: 28px; font-weight: 900; margin: 0; text-shadow: 0 0 10px rgba(255,0,0,0.2); }
    .data-value-red { color: #ff0000; font-family: 'Orbitron'; font-size: 28px; font-weight: 900; margin: 0; }

    /* Cartes sans fond blanc */
    .stealth-card {
        background: rgba(5, 5, 5, 0.5);
        border: 1px solid #111;
        padding: 25px;
        border-radius: 2px;
    }

    /* Table d'ordres épurée */
    .order-table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 12px; }
    .order-table th { color: #444; text-align: left; padding: 10px; border-bottom: 1px solid #111; font-size: 9px; letter-spacing: 2px; }
    .order-table td { padding: 15px 10px; border-bottom: 1px solid #050505; }
    
    /* Cache les éléments natifs de Streamlit qui polluent */
    div[data-testid="stMetric"] { display: none; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    # Ecran de login (simplifié pour le code)
    st.session_state.auth = True 
    st.rerun()
else:
    # --- HEADER ---
    st.markdown(f"""
        <div style='display:flex; justify-content:space-between; align-items:center;'>
            <h1 style='font-family:Orbitron; font-size:22px; letter-spacing:8px;'>HEDI AYOUB <span style='color:red;'>SINGULARITY</span></h1>
            <p style='color:#333; font-size:10px;'>CORE_V17 // UTC+1: {datetime.now().strftime('%H:%M:%S')}</p>
        </div>
        <div style='height:1px; background:linear-gradient(90deg, #ff0000, transparent); margin-bottom:30px;'></div>
    """, unsafe_allow_html=True)

    col_main, col_side = st.columns([2.8, 1.2])

    with col_main:
        # ZONE DE FOCUS (Plus de cases blanches, juste du texte brut et pro)
        st.markdown(f"""
            <div class='stealth-card'>
                <p class='data-label'>Target Identification</p>
                <h2 style='font-family:Orbitron; font-size:40px; margin-bottom:25px;'>NASDAQ 100 <span style='color:red;'>NQ1!</span></h2>
                <div style='display:flex; gap:60px;'>
                    <div class='data-block'><p class='data-label'>Confluence</p><p class='data-value-red'>99.2%</p></div>
                    <div class='data-block'><p class='data-label'>Liquidity Pool</p><p class='data-value'>BUY-SIDE</p></div>
                    <div class='data-block'><p class='data-label'>SMT Index</p><p class='data-value'>ALIGNED</p></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # CHART (Forcé en mode sombre)
        st.area_chart(pd.DataFrame(np.random.randn(35, 1)), height=300)

        # TABLE DES ORDRES (Look Terminal Bloomberg)
        st.markdown("<p class='data-label' style='margin-top:40px;'>Execution Logs // Active Orders</p>", unsafe_allow_html=True)
        st.markdown("""
            <table class='order-table'>
                <tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>ENTRY</th><th>TP / SL</th><th>PNL</th></tr>
                <tr>
                    <td style='font-weight:bold;'>NQ1!</td>
                    <td style='color:red;'>BUY MARKET</td>
                    <td>5.00</td>
                    <td>18245.25</td>
                    <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                    <td style='color:#00ff41; font-family:Orbitron;'>+$1,240.50</td>
                </tr>
                <tr style='opacity:0.4;'>
                    <td style='font-weight:bold;'>EURUSD</td>
                    <td>BUY LIMIT</td>
                    <td>10.00</td>
                    <td>1.08420</td>
                    <td>1.09100 / 1.08200</td>
                    <td>PENDING</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

    with col_side:
        # RISK MANAGEMENT
        st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
        st.markdown("<p class='data-label'>Risk Controller</p>", unsafe_allow_html=True)
        bal = st.number_input("ACCOUNT", value=100000, step=1000)
        risk = st.slider("RISK %", 0.1, 2.0, 0.5)
        
        # Calculateur
        risk_money = bal * (risk/100)
        lots = round(risk_money / 300, 2)
        
        st.markdown(f"""
            <div style='margin-top:25px; padding-top:20px; border-top:1px solid #111; text-align:center;'>
                <p class='data-label'>Position Size</p>
                <p style='font-family:Orbitron; font-size:48px; margin:0;'>{lots}</p>
                <p style='color:red; font-size:10px;'>MAX LOSS: ${risk_money}</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # CHRONO SANS FLICKER
        st.markdown("<div class='stealth-card' style='margin-top:20px; text-align:center;'>", unsafe_allow_html=True)
        components.html("""
            <div style="font-family:'Orbitron'; color:red; font-size:40px; font-weight:900; text-align:center;" id="timer">00:00</div>
            <script>
                var sec = 300;
                function count() {
                    var m=Math.floor(sec/60); var s=sec%60;
                    document.getElementById('timer').innerHTML = (m<10?'0':'')+m+':'+(s<10?'0':'')+s;
                    if(sec>0) sec--; else sec=300;
                }
                setInterval(count, 1000);
            </script>
        """, height=60)
        st.markdown("<p class='data-label'>Macro Impact Timer</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.code("> HediAyoub_PREDATOR: White boxes eliminated. Neural UI Active.", language="bash")
