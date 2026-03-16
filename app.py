import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime

# 1. INITIALISATION DU SYSTÈME
st.set_page_config(
    page_title="HediAyoub - The Predator", 
    page_icon="🎯",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. DESIGN QUANTUM (CSS INJECTION)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400;800&display=swap');
    
    /* Reset Global */
    .stApp { background-color: #000000 !important; color: #ffffff !important; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .block-container { padding: 1rem 3rem !important; }

    /* Suppression des éléments Streamlit polluants */
    div[data-testid="stMetric"], div[data-testid="stMetricValue"] { display: none; }
    iframe { border-radius: 4px; border: 1px solid #111; }

    /* Cartes Furtives */
    .stealth-card {
        background: #050505;
        border: 1px solid #111;
        border-left: 3px solid #ff0000;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* Typography */
    .label-mini { color: #444; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 5px; }
    .value-main { font-family: 'Orbitron'; font-size: 32px; font-weight: 900; color: #fff; margin: 0; }
    .value-red { color: #ff0000 !important; }

    /* Tableau d'exécution */
    .exec-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .exec-table th { color: #333; text-align: left; font-size: 9px; letter-spacing: 2px; padding: 10px; border-bottom: 1px solid #111; }
    .exec-table td { padding: 12px 10px; font-size: 12px; border-bottom: 1px solid #080808; }

    /* Matrix Grid */
    .matrix-box { background: #030303; border: 1px solid #111; padding: 15px; text-align: center; }
    .matrix-name { color: #444; font-size: 9px; margin: 0; }
    .matrix-val { font-family: 'Orbitron'; font-size: 16px; margin: 0; }
</style>
""", unsafe_allow_html=True)

# 3. GESTION DE L'ACCÈS
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("<br><br><br><br><h1 style='font-family:Orbitron; font-size:60px; text-align:center; line-height:0.8;'>HEDI<br><span style='color:red;'>AYOUB</span></h1>", unsafe_allow_html=True)
        pw = st.text_input("NEURAL ACCESS KEY", type="password", placeholder="Enter encrypted key...")
        if st.button("INITIALIZE"):
            if pw == "PREDATOR2026": 
                st.session_state.auth = True
                st.rerun()
else:
    # --- TOP INTERFACE ---
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(f"<p class='label-mini'>System Status: <span style='color:#00ff41;'>Hunting</span> // Target: <span style='color:white;'>Multiple</span></p>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<p style='text-align:right; color:#444; font-size:11px;'>NY_TIME: {datetime.now().strftime('%H:%M:%S')} // PREDATOR_V18</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='height:1px; background:linear-gradient(90deg, #ff0000, transparent); margin-bottom:20px;'></div>", unsafe_allow_html=True)

    # --- MAIN VIEW ---
    col_left, col_right = st.columns([2.8, 1.2])

    with col_left:
        # FOCUS PANEL
        st.markdown(f"""
            <div class='stealth-card'>
                <p class='label-mini'>Setup du plus clean (Neural Lock)</p>
                <h1 style='font-family:Orbitron; font-size:48px; margin-bottom:20px;'>NASDAQ-100 <span style='color:red;'>NQ1!</span></h1>
                <div style='display:flex; gap:50px;'>
                    <div><p class='label-mini'>Confluence</p><p class='value-main value-red'>99.2%</p></div>
                    <div><p class='label-mini'>TP Level</p><p class='value-main' style='color:#00ff41;'>18420.00</p></div>
                    <div><p class='label-mini'>SL Level</p><p class='value-main'>18190.50</p></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # CHART AREA
        st.area_chart(pd.DataFrame(np.random.randn(40, 1)), height=300)

        # ACTIVE ORDERS TABLE
        st.markdown("<p class='label-mini' style='margin-top:30px;'>Order Execution // Open Positions</p>", unsafe_allow_html=True)
        st.markdown("""
            <table class='exec-table'>
                <tr><th>SYMBOL</th><th>TYPE</th><th>LOTS</th><th>ENTRY</th><th>TP / SL</th><th>REAL-TIME PNL</th></tr>
                <tr>
                    <td><b>NQ1!</b></td>
                    <td style='color:red;'>BUY MARKET</td>
                    <td>5.00</td>
                    <td>18245.25</td>
                    <td><span style='color:#00ff41;'>18420</span> / <span style='color:red;'>18190</span></td>
                    <td style='color:#00ff41; font-family:Orbitron; font-size:16px;'>+$1,240.50</td>
                </tr>
                <tr style='opacity:0.4;'>
                    <td><b>EURUSD</b></td>
                    <td>BUY LIMIT</td>
                    <td>10.00</td>
                    <td>1.08420</td>
                    <td>1.09100 / 1.08200</td>
                    <td>PENDING</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

    with col_right:
        # RISK MANAGEMENT
        st.markdown("<div class='stealth-card'>", unsafe_allow_html=True)
        st.markdown("<p class='label-mini'>Risk Unit</p>", unsafe_allow_html=True)
        balance = st.number_input("Capital ($)", value=100000, step=1000)
        risk = st.slider("Risk %", 0.1, 2.0, 0.5)
        
        risk_money = balance * (risk/100)
        lots = round(risk_money / 300, 2)
        
        st.markdown(f"""
            <div style='text-align:center; padding-top:20px; border-top:1px solid #111; margin-top:15px;'>
                <p class='label-mini'>Position Size</p>
                <p style='font-family:Orbitron; font-size:45px; margin:0;'>{lots}</p>
                <p style='color:red; font-size:10px;'>LOSS CAP: ${risk_money}</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # KILLZONE TIMER
        st.markdown("<div class='stealth-card' style='text-align:center;'>", unsafe_allow_html=True)
        components.html("""
            <div style="font-family:'Orbitron'; color:red; font-size:40px; font-weight:900; text-align:center;" id="timer">00:00</div>
            <script>
                var sec = 480;
                function count() {
                    var m=Math.floor(sec/60); var s=sec%60;
                    document.getElementById('timer').innerHTML = (m<10?'0':'')+m+':'+(s<10?'0':'')+s;
                    if(sec>0) sec--; else sec=480;
                }
                setInterval(count, 1000);
            </script>
        """, height=60)
        st.markdown("<p class='label-mini'>Killzone Collision Window</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- GLOBAL MATRIX GRID (10 Actifs) ---
    st.markdown("<p class='label-mini' style='margin-top:30px;'>Global Neural Scan (Matrix)</p>", unsafe_allow_html=True)
    assets = [
        ("NQ", 99.2), ("ES", 85.1), ("XAU", 72.4), ("EURUSD", 96.0), ("GBPUSD", 84.1),
        ("BTC", 91.5), ("USDJPY", 84.8), ("AUDUSD", 78.0), ("USDCAD", 81.3), ("USDCHF", 65.9)
    ]
    m_cols = st.columns(5)
    for i, (name, score) in enumerate(assets):
        with m_cols[i % 5]:
            color = "red" if score > 90 else "white"
            st.markdown(f"""
                <div class='matrix-box' style='border-bottom: 2px solid {color if score > 90 else "#111"};'>
                    <p class='matrix-name'>{name}</p>
                    <p class='matrix-val' style='color:{color};'>{score}%</p>
                </div>
            """, unsafe_allow_html=True)

    st.code(f"> PREDATOR_CORE: Analyzing {len(assets)} assets... Highest probability found on NQ1! \n> SYSTEM: Matrix sync complete.", language="bash")
