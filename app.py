import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. ARCHITECTURE QUANTIQUE
st.set_page_config(page_title="HediAyoub - Singularity", layout="wide", initial_sidebar_state="collapsed")

# 2. DESIGN : "THE SINGULARITY" (L'esthétique du Pouvoir Absolu)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    .stApp { background: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 1rem 3rem;}

    /* Conteneur "Black Hole" */
    .singularity-card {
        background: #000;
        border: 1px solid #111;
        border-left: 5px solid #ff0000;
        padding: 30px;
        margin-bottom: 20px;
        transition: all 0.4s ease;
    }
    .singularity-card:hover { border: 1px solid #ff0000; box-shadow: 0 0 40px rgba(255, 0, 0, 0.1); }

    /* Typographie de Commandement */
    .glitch-title { font-family: 'Orbitron', sans-serif; font-size: 55px; font-weight: 900; letter-spacing: -3px; line-height: 1; margin-bottom: 10px; }
    .label-sub { color: #444; font-size: 10px; letter-spacing: 5px; text-transform: uppercase; }
    
    /* Radar & Indicators */
    .radar-active { color: #ff0000; font-weight: bold; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }
    
    /* Custom Sidebar */
    .stNumberInput input { background: #050505 !important; color: #fff !important; border: 1px solid #111 !important; font-family: 'Orbitron'; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.markdown("<br><br><br><h1 class='glitch-title'>HEDI<br><span style='color:red;'>AYOUB</span></h1><p class='label-sub'>Singularity Core V15</p>", unsafe_allow_html=True)
        pw = st.text_input("ENTER_SYSTEM_CODE", type="password")
        if st.button("OVERRIDE_REALITY"):
            if pw == "PREDATOR2026": st.session_state.auth = True; st.rerun()
else:
    # --- TOP NAVIGATION BAR (Ultra-Thin) ---
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("<p class='label-sub'>SYSTEM OVERVIEW // MULTI-ASSET CORRELATION</p>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<p style='text-align:right; font-family:Orbitron; font-size:12px; color:red;'>LOCKED_ON_NY_SESSION // {datetime.now().strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='height:2px; background:#111; margin-bottom:30px;'></div>", unsafe_allow_html=True)

    # --- CENTRE DE COMMANDEMENT ---
    left_col, right_col = st.columns([3, 1.2])

    with left_col:
        # MAIN SENSOR
        st.markdown("<div class='singularity-card'>", unsafe_allow_html=True)
        st.markdown("<p class='label-sub'>Primary Hunting Asset</p>", unsafe_allow_html=True)
        st.markdown("<h2 class='glitch-title'>NASDAQ-100</h2>", unsafe_allow_html=True)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("CONFLUENCE", "99.1%", "MAX")
        m2.metric("LIQUIDITY", "B-SIDE", "TARGET")
        m3.metric("SMT INDEX", "ALIGNED", "DXY/NQ")
        m4.metric("VOLATILITY", "EXPANDING", "ATR+")
        
        st.markdown("</div>", unsafe_allow_html=True)

        # SPATIAL DATA VISUALIZATION
        st.markdown("<p class='label-sub' style='margin-bottom:15px;'>Neural Liquidity Flow (Spatial View)</p>", unsafe_allow_html=True)
        # Simulation d'un graphique de liquidité avancée
        df = pd.DataFrame(np.random.randn(100, 2), columns=['Institutional', 'Retail'])
        st.area_chart(df, height=350)

    with right_col:
        # EXECUTION UNIT
        st.markdown("<div class='singularity-card'>", unsafe_allow_html=True)
        st.markdown("<p class='label-sub'>Capital Allocator</p>", unsafe_allow_html=True)
        balance = st.number_input("ACCOUNT ($)", value=100000, step=10000)
        risk = st.slider("RISK (%)", 0.1, 2.0, 0.5)
        
        risk_money = balance * (risk/100)
        lots = round(risk_money / 320, 2)
        
        st.markdown(f"""
            <div style='margin-top:20px; border-top:1px solid #111; padding-top:20px;'>
                <p class='label-sub'>Position Size</p>
                <p style='font-size:45px; font-family:Orbitron; color:red; font-weight:900; margin:0;'>{lots}</p>
                <p style='color:#444; font-size:10px;'>LOSS CAP: ${risk_money}</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # TIME-SPACE COLLISION (CHRONO)
        st.markdown("<div class='singularity-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<p class='label-sub'>Macro Collision Window</p>", unsafe_allow_html=True)
        components.html("""
            <div id="chrono" style="color: #fff; font-family: 'Orbitron', sans-serif; font-size: 50px; font-weight: 900; text-shadow: 0 0 20px rgba(255,255,255,0.2); text-align:center; padding:10px 0;">00:00</div>
            <script>
                var sec = 480;
                function timer(){
                    var m = Math.floor(sec/60); var s = sec%60;
                    document.getElementById('chrono').innerHTML = (m<10?'0':'')+m+':'+(s<10?'0':'')+s;
                    if(sec>0) sec--; else sec=480;
                }
                setInterval(timer, 1000);
            </script>
        """, height=100)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- THE GLOBAL MATRIX (Toutes les paires en temps réel) ---
    st.markdown("<p class='label-sub' style='margin-top:40px;'>Global Hunting Matrix</p>", unsafe_allow_html=True)
    matrix = st.columns(5)
    assets = [
        ("NQ", 99.1), ("ES", 82.4), ("XAU", 71.0), ("EURUSD", 95.8), ("GBPUSD", 84.2),
        ("BTC", 90.5), ("USDJPY", 86.0), ("AUDUSD", 78.2), ("USDCAD", 81.1), ("USDCHF", 65.4)
    ]
    
    for i, (name, score) in enumerate(assets):
        with matrix[i % 5]:
            st.markdown(f"""
                <div style='background:#030303; border-bottom:2px solid {"#ff0000" if score > 90 else "#111"}; padding:15px; margin-bottom:10px;'>
                    <p style='font-size:10px; color:#444; margin:0;'>{name}</p>
                    <p style='font-family:Orbitron; font-size:18px; color:{"#fff" if score < 90 else "red"}; margin:0;'>{score}%</p>
                </div>
            """, unsafe_allow_html=True)

    # FOOTER LOGS
    st.code(f"> SINGULARITY_V15: Scanning reality layers... \n> ALIGNEMENT: {assets[0][0]} & {assets[3][0]} show extreme institutional interest. \n> STATUS: Waiting for the Red Pillar.", language="bash")
