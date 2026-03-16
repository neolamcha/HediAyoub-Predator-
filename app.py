import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. CONFIGURATION SYSTÈME 
st.set_page_config(
    page_title="HediAyoub - Predator V20", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. DESIGN QUANTUM (CSS FINAL)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    .stApp { background-color: #000000 !important; color: #ffffff !important; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .block-container { padding: 1rem 2rem !important; }

    /* Suppression des éléments visuels natifs encombrants */
    div[data-testid="stMetric"], div[data-testid="stMetricValue"] { display: none; }
    .stNumberInput input, .stSlider [data-baseweb="slider"] { background-color: #000 !important; }

    /* Cartes Furtives */
    .stealth-card {
        background: #050505; border: 1px solid #111;
        border-left: 3px solid #ff0000; padding: 20px; margin-bottom: 20px;
    }

    /* Typography */
    .label-mini { color: #444; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; }
    .value-main { font-family: 'Orbitron'; font-size: 32px; font-weight: 900; color: #fff; margin: 0; }
    .value-red { color: #ff0000 !important; }

    /* Tableau d'exécution style Terminal */
    .exec-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .exec-table th { color: #333; text-align: left; font-size: 9px; letter-spacing: 2px; padding: 10px; border-bottom: 1px solid #111; }
    .exec-table td { padding: 12px 10px; font-size: 12px; border-bottom: 1px solid #080808; }

    /* Matrix Grid */
    .matrix-box { background: #030303; border: 1px solid #111; padding: 12px; text-align: center; border-bottom: 2px solid #111; }
    .matrix-active { border-bottom: 2px solid #ff0000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. AUTHENTICATION
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown("<br><br><h1 style='font-family:Orbitron; font-size:50px; text-align:center;'>HEDI<br><span style='color:red;'>AYOUB</span></h1>", unsafe_allow_html=True)
        pw = st.text_input("QUANTUM ACCESS KEY", type="password")
        if st.button("EXECUTE"):
            if pw == "PREDATOR2026": 
                st.session_state.auth = True
                st.rerun()
else:
    # --- HEADER NAVIGATION ---
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(f"<p class='label-mini'>System Status: <span style='color:#00ff41;'>Active_Hunting</span></p>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<p style='text-align:right; color:#444; font-size:11px;'>PREDATOR_V20 // {datetime.now().strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='height:1px; background:linear-gradient(90deg, #ff0000, transparent); margin-bottom:20px;'></div>", unsafe_allow_html=True)

    # --- CORPS PRINCIPAL ---
    col_left, col_right = st.columns([2.8, 1.2])

    with col_left:
        # FOCUS PANEL (TARGET)
        st.markdown(f"""
            <div class='stealth-card'>
                <p class='label-mini'>Target Identified</p>
                <h1 style='font-family:Orbitron; font-size:45px; margin-bottom:15px;'>NASDAQ-100 (NQ1!)</h1>
                <div style='display:flex; gap:40px;'>
                    <div><p class='label-mini'>Confluence</p><p class='value-main value-red'>99.2%</p></div>
                    <div><p class='label-mini'>Bias</p><p class='value-main'>BULLISH</p></div>
                    <div><p class='label-mini'>Session</p><p class='value-main' style='color:#444;'>NY_OPEN</p></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # VISUALISATION DE FLUX (Bar Chart - Pression Acheteuse/Vendeuse)
        st.markdown("<p class='label-mini'>Neural Order Flow Simulation</p>", unsafe_allow_html=True)
        chart_data = pd.DataFrame(np.random.randint(5, 100, size=(25, 2)), columns=['Institutional', 'Retail'])
        st.bar_chart(chart_data, height=220, color=["#ff0000", "#151515"])

        # TABLEAU DES ORDRES
        st.markdown("<p class='label-mini' style='margin-top:25px;'>Execution Logs // Active Positions</p>", unsafe_allow_html=True)
        st.markdown("""
            <table class='exec-table'>
                <tr><th>ASSET</th><th>TYPE</th><th>LOTS</th><th>ENTRY</th><th>TP / SL</th><th>LIVE PNL</th></tr>
                <tr>
                    <td><b>NQ1!</b></td><td style='color:red;'>BUY MARKET</td><td>5.00</td><td>18245.25</td>
                    <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                    <td style='color:#00ff41; font-family:Orbitron; font-size:16px;'>+$1,240.50</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

    with col_right:
        # --- CALCULATEUR DE RISQUE INTERACTIF ---
        st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
        st.markdown("<p class='label-mini'>Risk Unit Controller</p>", unsafe_allow_html=True)
        
        # Logique de calcul interactive
        bal = st.number_input("Account Balance ($)", value=100000, step=1000)
        risk_p = st.slider("Risk Exposure (%)", 0.1, 5.0, 0.5, step=0.1)
        
        # Calculs instantanés
        risk_cash = bal * (risk_p / 100)
        lots_final = round(risk_cash / 350, 2) # Formule adaptée au NQ
        
        st.markdown(f"""
            <div style='text-align:center; margin-top:20px; padding-top:20px; border-top:1px solid #111;'>
                <p class='label-mini'>Recommended Size</p>
                <p style='font-family:Orbitron; font-size:50px; margin:0;'>{lots_final}</p>
                <p style='color:red; font-size:11px; font-weight:bold;'>MAX RISK: ${risk_cash:,.2f}</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # KILLZONE CHRONO
        st.markdown("<div class='stealth-card' style='text-align:center;'>", unsafe_allow_html=True)
        components.html("""
            <div style="font-family:'Orbitron'; color:red; font-size:40px; font-weight:900; text-align:center;" id="timer">00:00</div>
            <script>
                var s=300; setInterval(function(){
                    var m=Math.floor(s/60); var sec=s%60;
                    document.getElementById('timer').innerHTML=(m<10?'0':'')+m+':'+(sec<10?'0':'')+sec;
                    if(s>0)s--;else s=300;
                },1000);
            </script>
        """, height=60)
        st.markdown("<p class='label-mini'>Macro Impact Timer</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- GLOBAL MATRIX SCAN (10 ASSETS) ---
    st.markdown("<p class='label-mini' style='margin-top:20px;'>Global Neural Matrix</p>", unsafe_allow_html=True)
    matrix_assets = [
        ("NQ", 99.2), ("ES", 85.1), ("XAU", 72.4), ("EURUSD", 96.0), ("GBPUSD", 84.1),
        ("BTC", 91.5), ("USDJPY", 84.8), ("AUDUSD", 78.0), ("USDCAD", 81.3), ("USDCHF", 65.9)
    ]
    m_cols = st.columns(5)
    for i, (name, score) in enumerate(matrix_assets):
        with m_cols[i % 5]:
            is_active = "matrix-active" if score > 90 else ""
            color = "red" if score > 90 else "white"
            st.markdown(f"""
                <div class='matrix-box {is_active}'>
                    <p style='color:#444; font-size:9px; margin:0;'>{name}</p>
                    <p style='font-family:Orbitron; font-size:18px; color:{color}; margin:0;'>{score}%</p>
                </div>
            """, unsafe_allow_html=True)

    st.code(f"> HediAyoub_SYSTEM: Matrix V20 Online. Calculateur synchronisé. \n> TARGET: NQ1! showing peak confluence.", language="bash")
