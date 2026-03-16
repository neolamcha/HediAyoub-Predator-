import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="HediAyoub - Predator Execution", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS CUSTOM (Intégration des styles d'ordres)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    .stApp { background-color: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    .block-container { padding: 1.5rem 3rem !important; }
    
    /* Order Cards */
    .order-row {
        background: #050505; border: 1px solid #111;
        padding: 10px 20px; border-left: 3px solid #ff0000;
        display: flex; justify-content: space-between; align-items: center;
        margin-bottom: 5px; font-size: 12px;
    }
    .tp-text { color: #00ff41; font-weight: bold; }
    .sl-text { color: #ff4b4b; font-weight: bold; }
    .pnl-positive { color: #00ff41; font-family: 'Orbitron'; font-size: 18px; }
    
    .label-min { color: #444; font-size: 9px; text-transform: uppercase; letter-spacing: 2px; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    # (Ecran de login identique...)
    st.session_state.auth = True # Bypass pour le test
    st.rerun()
else:
    # --- HEADER ---
    st.markdown("<h2 style='font-family:Orbitron; letter-spacing:5px;'>HEDI AYOUB // <span style='color:red;'>EXECUTION_UNIT</span></h2>", unsafe_allow_html=True)
    st.markdown("<div style='height:1px; background:#111; margin-bottom:20px;'></div>", unsafe_allow_html=True)

    col_main, col_side = st.columns([2.8, 1.2])

    with col_main:
        # ZONE DE FOCUS AVEC TP/SL VISIBLES
        st.markdown(f"""
            <div style='background:#050505; padding:25px; border:1px solid #111; margin-bottom:20px;'>
                <div style='display:flex; justify-content:space-between; align-items:start;'>
                    <div>
                        <p class='label-min'>Target Locked</p>
                        <h1 style='font-family:Orbitron; margin:0;'>NASDAQ-100</h1>
                    </div>
                    <div style='text-align:right;'>
                        <p class='label-min'>Live PnL</p>
                        <p class='pnl-positive'>+$1,240.50</p>
                    </div>
                </div>
                <div style='display:grid; grid-template-columns: repeat(4, 1fr); gap:20px; margin-top:20px; border-top:1px solid #111; padding-top:20px;'>
                    <div><p class='label-min'>Entry</p><p style='font-size:18px;'>18245.25</p></div>
                    <div><p class='label-min'>Current</p><p style='font-size:18px;'>18302.10</p></div>
                    <div><p class='label-min' style='color:#00ff41;'>Take Profit</p><p class='tp-text' style='font-size:18px;'>18420.00</p></div>
                    <div><p class='label-min' style='color:#ff4b4b;'>Stop Loss</p><p class='sl-text' style='font-size:18px;'>18190.50</p></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # GRAPHIQUE
        st.area_chart(pd.DataFrame(np.random.randn(30, 1)), height=250)

        # --- MODULE DES ORDRES ---
        st.markdown("<p class='label-min' style='margin-top:30px;'>Active Positions & Pending Orders</p>", unsafe_allow_html=True)
        
        # Exemple d'ordre actif
        st.markdown("""
            <div class='order-row'>
                <div style='width:100px;'><b>NQ1!</b> <br><span style='color:red; font-size:9px;'>BUY MARKET</span></div>
                <div><span class='label-min'>Lots</span><br>5.00</div>
                <div><span class='label-min'>Entry</span><br>18245.25</div>
                <div><span class='label-min'>TP / SL</span><br><span class='tp-text'>18420</span> / <span class='sl-text'>18190</span></div>
                <div class='pnl-positive'>+$1,240</div>
            </div>
        """, unsafe_allow_html=True)

        # Exemple d'ordre différé (Limit)
        st.markdown("""
            <div class='order-row' style='border-left: 3px solid #444; opacity: 0.6;'>
                <div style='width:100px;'><b>EURUSD</b> <br><span style='color:#444; font-size:9px;'>BUY LIMIT</span></div>
                <div><span class='label-min'>Lots</span><br>10.00</div>
                <div><span class='label-min'>Price</span><br>1.08420</div>
                <div><span class='label-min'>Status</span><br>PENDING</div>
                <div style='font-family:Orbitron; font-size:14px; color:#444;'>WAITING</div>
            </div>
        """, unsafe_allow_html=True)

    with col_side:
        # CALCULATEUR (Inchangé mais vital)
        st.markdown("<div style='background:#050505; padding:20px; border:1px solid #111;'>", unsafe_allow_html=True)
        st.markdown("<p class='label-min'>Order Executor</p>", unsafe_allow_html=True)
        bal = st.number_input("Capital", value=100000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        st.button("PLACE BUY ORDER")
        st.button("PLACE SELL ORDER")
        st.markdown("</div>", unsafe_allow_html=True)

        # CHRONO SANS FLICKER
        components.html("""
            <div style="font-family:'Orbitron'; color:red; font-size:35px; font-weight:900; text-align:center; background:#000; padding:20px; border:1px solid #111; margin-top:20px;" id="timer">00:00</div>
            <script>
                var sec = 300;
                function count() {
                    var m=Math.floor(sec/60); var s=sec%60;
                    document.getElementById('timer').innerHTML = (m<10?'0':'')+m+':'+(s<10?'0':'')+s;
                    if(sec>0) sec--; else sec=300;
                }
                setInterval(count, 1000);
            </script>
        """, height=100)

    st.code("> SYSTEM: Executing orders... TP/SL levels synced with Neural Core.", language="bash")
