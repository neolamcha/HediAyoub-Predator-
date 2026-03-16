import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ARCHITECTURE HAUTE PERFORMANCE
st.set_page_config(
    page_title="HediAyoub - The Predator", 
    page_icon="🎯", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. LE MOTEUR DE RENDU "ULTRA-GLOW" (CSS PROPRIÉTAIRE)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;600&family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* Fond Noir Profond & Grain */
    .stApp {
        background: radial-gradient(circle at center, #0a0a0a 0%, #000000 100%);
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }

    /* Masquage des éléments Streamlit parasites */
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 2rem; padding-bottom: 0rem;}

    /* Cartes Glassmorphism */
    .predator-card {
        background: rgba(10, 10, 10, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.03);
        border-radius: 4px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.9);
        backdrop-filter: blur(10px);
        margin-bottom: 15px;
        position: relative;
        overflow: hidden;
    }
    
    .predator-card::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 2px; height: 100%;
        background: #ff0000; /* Ligne d'accent Predator */
    }

    /* Metrics & Data */
    .metric-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(255,255,255,0.2);
    }
    .metric-label {
        font-family: 'Orbitron', sans-serif;
        font-size: 10px;
        letter-spacing: 2px;
        color: #555;
        text-transform: uppercase;
    }

    /* Chrono Cyber-Agressif */
    .chrono-display {
        font-family: 'Orbitron', sans-serif;
        color: #ff0000;
        font-size: 64px;
        font-weight: 700;
        text-align: center;
        letter-spacing: -2px;
        text-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
    }

    /* Input & Sidebar Custom */
    .stNumberInput div div input { background-color: #000 !important; color: white !important; border: 1px solid #222 !important; }
    .stSlider div div { color: #ff0000 !important; }

</style>
""", unsafe_allow_html=True)

# 3. LOGIQUE D'ACCÈS IMMERSIVE
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        st.markdown("""
            <div style='text-align:center;'>
                <h1 style='font-family:Orbitron; letter-spacing:10px; color:white; margin-bottom:0;'>HediAyoub</h1>
                <p style='color:red; letter-spacing:5px; font-weight:bold;'>THE PREDATOR</p>
                <div style='height:1px; background:rgba(255,255,255,0.1); margin:20px 0;'></div>
            </div>
        """, unsafe_allow_html=True)
        pw = st.text_input("IDENTIFICATION BIOMÉTRIQUE", type="password")
        if st.button("AUTHENTIFICATION"):
            if pw == "PREDATOR2026": st.session_state.auth = True; st.rerun()
else:
    # 4. DASHBOARD - STRUCTURE BLACK OPS
    st.markdown("""
        <div style='display:flex; justify-content:space-between; align-items:center;'>
            <div style='font-family:Orbitron; font-size:18px; letter-spacing:2px;'>HediAyoub <span style='color:red;'>THE PREDATOR</span></div>
            <div style='font-family:JetBrains Mono; font-size:10px; color:#444;'>NODE: TUNISIA_CORE_01 // SECURE_LINE_ACTIVE</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:1px; background:linear-gradient(to right, red, transparent); margin:10px 0 25px 0;'></div>", unsafe_allow_html=True)

    col_charts, col_execution = st.columns([2.6, 1.2])

    with col_charts:
        # DATA ENGINE VISUALIZATION
        st.markdown("<div class='predator-card'>", unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>Visual Intelligence Stream</p>", unsafe_allow_html=True)
        
        # Grid de données en temps réel (simulées avec style)
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown("<p class='metric-label'>Volume Delta</p>", unsafe_allow_html=True)
            st.markdown("<p class='metric-value'>+2.482</p>", unsafe_allow_html=True)
        with m2:
            st.markdown("<p class='metric-label'>Net Liquidity</p>", unsafe_allow_html=True)
            st.markdown("<p class='metric-value'>24,705.50</p>", unsafe_allow_html=True)
        with m3:
            st.markdown("<p class='metric-label'>SMT Signal</p>", unsafe_allow_html=True)
            st.markdown("<p class='metric-value' style='color:#00ff41;'>ALIGNED</p>", unsafe_allow_html=True)
        
        # Graphique de Flux Institutionnel
        st.write("---")
        chart_data = pd.DataFrame(np.random.randn(30, 2), columns=['Institutional', 'Retail'])
        st.line_chart(chart_data, height=280)
        st.markdown("</div>", unsafe_allow_html=True)

        # REPORT GENERATOR
        if st.button("GÉNÉRER RAPPORT NEURAL"):
            st.markdown("""
                <div style='background:#050505; border:1px solid #111; padding:20px; font-family:JetBrains Mono; font-size:12px; color:#888;'>
                    <span style='color:red;'>[SYSTEM_REPORT]</span> Analyse HediAyoub terminée.<br>
                    Le prix rejette le Midnight Open. Imbalance détectée sur le carnet d'ordres NQ.<br>
                    Confluence SMC : CHoCH M15 confirmé. Risk: Reward optimal (1:3.2).
                </div>
            """, unsafe_allow_html=True)

    with col_execution:
        # RISK MANAGEMENT MODULE
        st.markdown("<div class='predator-card'>", unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>Strategic Risk Management</p>", unsafe_allow_html=True)
        
        balance = st.number_input("Capital ($)", value=100000, step=1000)
        risk_pct = st.slider("Risque (%)", 0.25, 2.0, 0.5)
        
        st.write("---")
        # Calculateur
        sl_points = 15.0
        risk_amount = balance * (risk_pct/100)
        lots = round(risk_amount / (sl_points * 20), 2)
        
        st.markdown(f"""
            <div style='background:#000; padding:15px; border:1px solid #222; border-radius:4px;'>
                <p style='color:#555; font-size:10px; margin:0;'>LOTS CALCULÉS</p>
                <p style='font-size:32px; font-weight:bold; color:white; margin:0;'>{lots}</p>
                <p style='color:red; font-size:10px;'>EXPOSITION : ${risk_amount}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style='margin-top:15px; font-family:JetBrains Mono; font-size:13px;'>
                <span style='color:#555;'>ENTRY:</span> 24655.25<br>
                <span style='color:#555;'>STOP:</span> <span style='color:red;'>24640.25</span><br>
                <span style='color:#555;'>TP1:</span> 24705.00
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # CHRONO ACTIF (RECODÉ)
        st.markdown("<div class='predator-card'>", unsafe_allow_html=True)
        st.markdown("<p class='metric-label' style='text-align:center;'>Next Setup Window</p>", unsafe_allow_html=True)
        
        if 'timer' not in st.session_state: st.session_state.timer = 455
        st.session_state.timer -= 1
        if st.session_state.timer <= 0: st.session_state.timer = 455
        
        m, s = divmod(st.session_state.timer, 60)
        st.markdown(f"<p class='chrono-display'>{m:02d}:{s:02d}</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Auto-refresh pour le chrono
        time.sleep(1)
        st.rerun()
