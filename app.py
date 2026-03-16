import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. FORCAGE DU THEME SOMBRE & MISE EN PAGE
st.set_page_config(
    page_title="HediAyoub - Singularity", 
    page_icon="🎯",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. LE CSS "HORS-NORME" (Correction des lacunes visuelles)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    /* Global Reset */
    .stApp { background-color: #000000 !important; color: #ffffff !important; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .block-container { padding: 1.5rem 3rem !important; }
    
    /* Suppression des bordures blanches Streamlit sur les graphiques */
    [data-testid="stMetricValue"] { font-family: 'Orbitron', sans-serif !important; font-size: 32px !important; color: #ff0000 !important; }
    [data-testid="stMetricDelta"] { display: none; }
    [data-testid="stMetricLabel"] { font-size: 10px !important; letter-spacing: 2px !important; color: #444 !important; text-transform: uppercase !important; }

    /* Cartes Ultra-Sombre */
    .p-card {
        background: #050505;
        border: 1px solid #111;
        border-left: 3px solid #ff0000;
        padding: 25px;
        margin-bottom: 20px;
    }

    /* Boutons Predator */
    .stButton>button {
        background-color: #000 !important;
        color: #ff0000 !important;
        border: 1px solid #ff0000 !important;
        font-family: 'Orbitron' !important;
        width: 100%;
        letter-spacing: 3px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ff0000 !important; color: #000 !important; box-shadow: 0 0 20px #ff0000; }

    /* Correction des inputs */
    input { background-color: #000 !important; color: white !important; border: 1px solid #222 !important; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("<br><br><br><br><h1 style='font-family:Orbitron; font-size:60px; text-align:center; line-height:0.8;'>HEDI<br><span style='color:red;'>AYOUB</span></h1><p style='text-align:center; letter-spacing:10px; color:#333; font-size:10px;'>SINGULARITY CORE</p>", unsafe_allow_html=True)
        pw = st.text_input("ACCESS_CODE", type="password", placeholder="Waiting for key...")
        if st.button("OVERRIDE"):
            if pw == "PREDATOR2026": st.session_state.auth = True; st.rerun()
else:
    # --- HEADER ---
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("<h2 style='font-family:Orbitron; letter-spacing:5px;'>HEDI AYOUB // <span style='color:red;'>THE PREDATOR</span></h2>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<p style='text-align:right; color:#444; font-size:11px; margin-top:15px;'>CORE_V15 // NY_SESSION_ACTIVE // {datetime.now().strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='height:1px; background:#111; margin-bottom:30px;'></div>", unsafe_allow_html=True)

    # --- BODY ---
    col_left, col_right = st.columns([2.8, 1.2])

    with col_left:
        st.markdown("<div class='p-card'><p style='color:#444; font-size:10px; letter-spacing:4px;'>PRIMARY_HUNTING_TARGET</p><h1 style='font-family:Orbitron; font-size:45px;'>NASDAQ-100 (NQ)</h1>", unsafe_allow_html=True)
        
        # Metrics épurées
        m1, m2, m3 = st.columns(3)
        m1.metric("CONFLUENCE", "99.2%")
        m2.metric("LIQUIDITY", "B-SIDE")
        m3.metric("SMT_BIAS", "TRUE")
        
        # Graphique sombre forcé (Area Chart)
        chart_data = pd.DataFrame(np.random.randn(40, 1), columns=['Price'])
        st.area_chart(chart_data, height=300, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        # RISK UNIT
        st.markdown("<div class='p-card'>", unsafe_allow_html=True)
        st.markdown("<p style='color:#444; font-size:10px; letter-spacing:2px;'>RISK_ALLOCATOR</p>", unsafe_allow_html=True)
        balance = st.number_input("CAPITAL ($)", value=100000, step=1000)
        risk_pct = st.slider("RISK (%)", 0.1, 2.0, 0.5)
        
        risk_money = balance * (risk_pct/100)
        lots = round(risk_money / 300, 2) # Calcul simple NQ
        
        st.markdown(f"""
            <div style='text-align:center; padding:20px 0; border-top:1px solid #111; margin-top:15px;'>
                <p style='color:#444; font-size:10px;'>POSITION SIZE</p>
                <p style='font-family:Orbitron; font-size:45px; color:white;'>{lots}</p>
                <p style='color:red; font-size:10px;'>RISK: ${risk_money}</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # CHRONO SANS FLICKER
        st.markdown("<div class='p-card' style='text-align:center;'>", unsafe_allow_html=True)
        components.html("""
            <div style="font-family:'Orbitron'; color:red; font-size:40px; font-weight:900; text-align:center;" id="timer">00:00</div>
            <script>
                var sec = 450;
                function count() {
                    var m=Math.floor(sec/60); var s=sec%60;
                    document.getElementById('timer').innerHTML = (m<10?'0':'')+m+':'+(s<10?'0':'')+s;
                    if(sec>0) sec--; else sec=450;
                }
                setInterval(count, 1000);
            </script>
        """, height=60)
        st.markdown("<p style='color:#444; font-size:9px; letter-spacing:3px;'>MACRO_IMPACT_TIMER</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # MATRIX GRID
    assets = [("NQ", 99), ("ES", 85), ("XAU", 72), ("EURUSD", 96), ("BTC", 91), ("USDJPY", 84)]
    cols = st.columns(6)
    for i, (name, score) in enumerate(assets):
        with cols[i]:
            st.markdown(f"""
                <div style='background:#050505; border:1px solid #111; padding:15px; text-align:center;'>
                    <p style='color:#333; font-size:10px; margin:0;'>{name}</p>
                    <p style='color:{"red" if score > 95 else "white"}; font-family:Orbitron; font-size:18px; margin:0;'>{score}%</p>
                </div>
            """, unsafe_allow_html=True)

    st.code(f"> HediAyoub_PREDATOR: System stabilized. No flicker. Matrix Active.", language="bash")
