import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# 1. CORE ENGINE CONFIGURATION
st.set_page_config(page_title="HediAyoub - The Predator", layout="wide", initial_sidebar_state="collapsed")

# 2. DESIGN : NEURAL BLACK-OPS (Ultra-HD Professional)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500;700&display=swap');
    
    .stApp { background: #000; color: #eee; font-family: 'JetBrains Mono', monospace; }
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 1.5rem 4rem;}

    .p-card {
        background: linear-gradient(145deg, #050505 0%, #010101 100%);
        border: 1px solid rgba(255, 255, 255, 0.02);
        border-radius: 4px; padding: 25px; box-shadow: 0 20px 50px rgba(0,0,0,0.9);
        margin-bottom: 25px; position: relative;
    }

    .focus-border {
        position: absolute; top: 0; left: 0; width: 3px; height: 100%;
        background: #ff0000; box-shadow: 0 0 10px #ff0000;
    }

    .label-alpha { color: #444; font-size: 10px; text-transform: uppercase; letter-spacing: 4px; font-weight: 700; }
    .value-alpha { color: #fff; font-size: 24px; font-family: 'Orbitron', sans-serif; letter-spacing: 1px; }
    .scan-text { color: #ff0000; font-size: 11px; font-family: 'Orbitron', sans-serif; letter-spacing: 2px; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown("<br><br><div style='text-align:center;'><h1 style='font-family:Orbitron; color:white; letter-spacing:10px;'>HediAyoub</h1><p style='color:red; letter-spacing:6px; font-size:12px;'>THE PREDATOR SYSTEM</p></div>", unsafe_allow_html=True)
        pw = st.text_input("NEURAL ACCESS KEY", type="password")
        if st.button("EXECUTE"):
            if pw == "PREDATOR2026": st.session_state.auth = True; st.rerun()
else:
    # --- HEADER ---
    st.markdown("""
        <div style='display:flex; justify-content:space-between; align-items:end;'>
            <div>
                <span style='font-family:Orbitron; font-size:26px; color:white;'>HediAyoub</span>
                <span style='font-family:Orbitron; font-size:26px; color:red; margin-left:10px;'>THE PREDATOR</span>
            </div>
            <div style='font-family:JetBrains Mono; font-size:10px; color:#444; letter-spacing:2px;'>TOTAL_MARKET_SCANNER_V12 // ALL_ASSETS_MONITORED</div>
        </div>
        <div style='height:1px; background:linear-gradient(90deg, #ff0000, transparent); margin:20px 0;'></div>
    """, unsafe_allow_html=True)

    # --- ALGORITHME DE SCAN GLOBAL (SMC/ICT FOCUS) ---
    # Cette base de données simule l'analyse de tous les actifs demandés.
    scan_results = {
        "NASDAQ (NQ)": {"score": 94.2, "reason": "Midnight Open Rejection + FVG M15.", "entry": "24655.25", "sl": "24640.25"},
        "S&P 500 (ES)": {"score": 88.1, "reason": "Following NQ momentum, waiting for SMT.", "entry": "5215.00", "sl": "5208.00"},
        "EUR/USD": {"score": 97.8, "reason": "London Liquidity Sweep + Displacement.", "entry": "1.08450", "sl": "1.08380"},
        "GBP/USD": {"score": 82.5, "reason": "Choppy price action near PDH.", "entry": "1.26550", "sl": "1.26420"},
        "BTC/USD": {"score": 91.0, "reason": "Asia Low Sweep + Bullish OrderBlock.", "entry": "68450", "sl": "68100"},
        "GOLD (XAU)": {"score": 75.4, "reason": "Consolidation within Equilibrium.", "entry": "2155.20", "sl": "2148.00"},
        "USD/JPY": {"score": 85.9, "reason": "Rejection of H4 Breaker Block.", "entry": "149.200", "sl": "149.050"},
        "AUD/USD": {"score": 79.2, "reason": "Retesting New Week Opening Gap.", "entry": "0.65400", "sl": "0.65320"},
        "USD/CAD": {"score": 81.4, "reason": "Liquidity Grab at Daily High.", "entry": "1.35200", "sl": "1.35350"},
        "USD/CHF": {"score": 70.8, "reason": "Low Volatility. Avoid until Killzone.", "entry": "0.88400", "sl": "0.88550"}
    }
    
    # Sélection automatique de la "Proie" la plus propre (Highest Score)
    best_pair = max(scan_results, key=lambda x: scan_results[x]['score'])
    data = scan_results[best_pair]

    col_main, col_side = st.columns([2.5, 1.2])

    with col_main:
        # ZONE DE FOCUS (TARGET LOCKED)
        st.markdown(f"""
            <div class='p-card'>
                <div class='focus-border'></div>
                <div style='display:flex; justify-content:space-between;'>
                    <span class='scan-text'>● NEURAL SCANNER ACTIVE</span>
                    <span style='color:#555; font-size:10px;'>WATCHLIST_SIZE: 10 ASSETS</span>
                </div>
                <h2 style='margin:15px 0; font-family:Orbitron; color:white;'>{best_pair} <span style='color:red;'>BEST_ALPHA_SETUP</span></h2>
                <div style='display:grid; grid-template-columns: 1fr 1fr 1fr; gap:20px; margin-top:20px;'>
                    <div><p class='label-alpha'>Neural Confluence</p><p class='value-alpha' style='color:red;'>{data['score']}%</p></div>
                    <div><p class='label-alpha'>Setup Quality</p><p class='value-alpha'>A+ CLASS</p></div>
                    <div><p class='label-alpha'>Killzone Status</p><p class='value-alpha'>ACTIVE</p></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # GRAPHIQUE DE LIQUIDITÉ
        st.markdown("<div class='p-card' style='padding:10px;'>", unsafe_allow_html=True)
        chart_data = pd.DataFrame(np.random.randn(50, 1), columns=['Liquidity_Flow'])
        st.area_chart(chart_data, height=350, use_container_width=True)
        st.markdown(f"<p style='font-family:JetBrains Mono; font-size:11px; color:#444; padding:10px;'>INSTITUTIONAL_LOG: {data['reason']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_side:
        # RISK MANAGEMENT (Adapté au capital)
        st.markdown("<div class='p-card'>", unsafe_allow_html=True)
        st.markdown("<p class='label-alpha' style='margin-bottom:15px;'>Execution & Risk</p>", unsafe_allow_html=True)
        
        balance = st.number_input("ACCOUNT_BALANCE ($)", value=100000, step=1000)
        risk_pct = st.slider("RISK_PER_TRADE (%)", 0.25, 2.0, 0.5)
        
        risk_money = balance * (risk_pct/100)
        # Ratio de calcul de lots (ajustable)
        lots = round(risk_money / 300, 2)
        
        st.markdown(f"""
            <div style='background:#000; border:1px solid #111; padding:20px; margin:20px 0;'>
                <p class='label-alpha'>Precision Lots</p>
                <p style='font-size:42px; font-family:Orbitron; color:white; margin:0;'>{lots}</p>
                <p style='color:red; font-size:10px; font-weight:bold;'>MAX RISK: ${risk_money}</p>
            </div>
            <div style='font-family:JetBrains Mono; font-size:12px;'>
                <span style='color:#444;'>ENTRY_TARGET:</span> {data['entry']}<br>
                <span style='color:#444;'>STOP_PROTECT:</span> <span style='color:red;'>{data['sl']}</span><br>
                <span style='color:#444;'>RR_RATIO:</span> 1:3.2
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # CHRONO SANS CLIGNOTEMENT (JS)
        st.markdown("<div class='p-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<p class='label-alpha'>Time to Collision</p>", unsafe_allow_html=True)
        components.html("""
            <div id="chrono" style="color: #ff0000; font-family: 'Orbitron', sans-serif; font-size: 50px; font-weight: 700; text-shadow: 0 0 15px rgba(255,0,0,0.4); text-align:center;">00:00</div>
            <script>
                var sec = 285;
                function timer(){
                    var m = Math.floor(sec/60); var s = sec%60;
                    document.getElementById('chrono').innerHTML = (m<10?'0':'')+m+':'+(s<10?'0':'')+s;
                    if(sec>0) sec--; else sec=285;
                }
                setInterval(timer, 1000);
            </script>
        """, height=100)
        st.markdown("</div>", unsafe_allow_html=True)

    # TERMINAL LOGS
    st.code(f"> HEDI_AYOUB_PREDATOR: 10 Assets Scan Complete. \n> TARGET_LOCKED: {best_pair} showing highest SMC confluence ({data['score']}%). \n> DATA_READY: System stable.", language="bash")
