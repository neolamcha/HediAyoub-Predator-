import streamlit as st
import time

# 1. SETUP HAUTE PERFORMANCE & BRANDING PERSONNEL
st.set_page_config(
    page_title="HediAyoub - The Predator", 
    page_icon="🎯", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    .stApp { background-color: #000000; color: #00FF41; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #111; }
    
    .hidden-stream { display: none; }
    
    .process-card {
        background: #050505; border: 1px solid #111; border-radius: 4px; padding: 20px;
        box-shadow: inset 0 0 15px #00ff4108; margin-bottom: 15px;
    }
    
    .report-area {
        background: #080808; border-left: 3px solid #00FF41; padding: 15px;
        color: #CCC; font-size: 13px; line-height: 1.6;
    }

    .scanner-line {
        height: 1px; background: #00FF41; width: 100%; position: relative;
        animation: scan 4s linear infinite; opacity: 0.2;
    }
    @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }
    
    .glitch-title { color: #FFF; font-size: 26px; font-weight: bold; letter-spacing: 2px; text-shadow: 2px 2px #ff000033; }
    .brand-subtitle { color: #555; font-size: 10px; letter-spacing: 5px; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_b:
        st.markdown("<br><br><div style='text-align:center;'><span class='glitch-title'>HediAyoub</span><br><span style='color:#ff0000; font-size:20px; font-weight:bold;'>THE PREDATOR</span></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        pw = st.text_input("SCAN BIOMÉTRIQUE", type="password")
        if st.button("ACCÉDER AU CORE"):
            if pw == "PREDATOR2026": st.session_state.auth = True; st.rerun()
else:
    # HEADER AVEC TON NOM
    st.markdown("<div style='text-align:center;'><span class='glitch-title'>HediAyoub - THE PREDATOR</span><br><span class='brand-subtitle'>Institutional Neural Terminal v6.1</span></div>", unsafe_allow_html=True)
    st.divider()

    col_main, col_data = st.columns([2.2, 1.3])

    with col_main:
        # VISUALISATION DES DONNÉES
        st.markdown("<div class='process-card' style='height:480px; position:relative;'>", unsafe_allow_html=True)
        st.markdown("<div class='scanner-line'></div>", unsafe_allow_html=True)
        st.markdown("### 📊 DATA VISUALIZATION")
        
        st.write("---")
        c1, c2, c3 = st.columns(3)
        c1.metric("INSTITUTIONAL DELTA", "+1,890", "BULLISH")
        c2.metric("LIQUIDITY POOL", "24,710.00", "TARGET")
        c3.metric("SMT DIVERGENCE", "NONE", "CONFIRMED")
        
        # ZONE DE RAPPORT
        st.markdown("#### 📄 RAPPORT DE CONFLUENCE ALPHA")
        if st.button("GÉNÉRER LE RAPPORT DÉTAILLÉ"):
            with st.spinner("Analyse des flux HediAyoub en cours..."):
                time.sleep(1.5)
                st.markdown("""
                <div class='report-area'>
                <b>[ANALYSE HediAyoub - THE PREDATOR]</b><br>
                Structure de marché confirmée. Absorption des ordres vendeurs détectée sur le niveau institutionnel.<br><br>
                <b>CONFLUENCES :</b><br>
                1. Midnight Open : Rejet propre.<br>
                2. Footprint : Déséquilibre acheteur majeur identifié.<br>
                3. SMT : Corrélation NQ/ES validée.<br><br>
                <b>ACTION :</b> Préparation d'entrée sur repli FVG.
                </div>
                """, unsafe_allow_html=True)
        
        # FLUX CACHÉS
        st.markdown("<div class='hidden-stream'>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=jc1Ds-Uz6gE")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_data:
        # CALCULATEUR
        st.markdown("<div class='process-card'>", unsafe_allow_html=True)
        balance = st.sidebar.number_input("ACCOUNT_BALANCE ($)", value=100000)
        risk = st.sidebar.slider("RISK (%)", 0.25, 2.0, 0.5)
        
        st.markdown("### ⚔️ EXECUTION")
        sl_points = 18.5
        lots = round((balance * (risk/100)) / (sl_points * 20), 2)
        
        st.write(f"**LOTS :** <span style='font-size:24px; color:#FFF;'>{lots}</span>", unsafe_allow_html=True)
        st.write(f"**ORDRE :** `BUY LIMIT`")
        st.write(f"**ENTRY :** <span style='color:#00FF41;'>24655.25</span>", unsafe_allow_html=True)
        st.write(f"**SL :** <span style='color:#FF4B4B;'>24636.75</span>", unsafe_allow_html=True)
        st.write(f"**TP 1 :** `24705.00` | **TP 2 :** `24780.00`")
        st.markdown("</div>", unsafe_allow_html=True)

        # CHRONO
        st.markdown("<div class='process-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<span style='font-size:10px;'>ESTIMATION COLLISION</span>", unsafe_allow_html=True)
        st.markdown("<h1 style='color:#00FF41; margin:0;'>00:03:47</h1>", unsafe_allow_html=True)
        st.progress(92)
        st.markdown("</div>", unsafe_allow_html=True)

    # LOGS
    st.code(f"> HediAyoub_CORE_ACTIVE... \n> PROCESSING DATA STREAMS... \n> LOT_SIZE: {lots} \n> SYSTEM_READY.", language="bash")
