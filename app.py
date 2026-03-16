import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# 1. CONFIGURATION RADICALE
st.set_page_config(page_title="HediAyoub Predator V37", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE SURVIE (Noir absolu, visibilité forcée)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=JetBrains+Mono:wght@400;800&display=swap');
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    
    /* Force les inputs en blanc pour ne pas les perdre */
    div[data-baseweb="input"] { background-color: #ffffff !important; border-radius: 4px !important; }
    input { color: #000000 !important; font-weight: 900 !important; }

    .card { background: #080808; border: 1px solid #1a1a1a; border-left: 4px solid #ff0000; padding: 15px; margin-bottom: 10px; }
    .label-mini { color: #555; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; font-weight: 800; }
    
    /* Animation Pulse pour le A+ */
    .aplus-active { color: #ff0000; font-family: 'Orbitron'; animation: blink 1s infinite; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
</style>
""", unsafe_allow_html=True)

# 3. HEADER SIMPLE
st.markdown(f"<div style='padding: 10px; background: #050505; border-bottom: 1px solid #111; color:red; font-family:Orbitron; font-weight:900; font-size:20px;'>PREDATOR_V37 // SYSTEM_RESTORED</div>", unsafe_allow_html=True)

# 4. DASHBOARD
col_left, col_mid, col_right = st.columns([1, 2, 1])

with col_left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>Execution Stats</p>", unsafe_allow_html=True)
    cap = st.number_input("ACCOUNT ($)", value=100000)
    risk = st.slider("RISK %", 0.1, 5.0, 1.0)
    lots = round((cap * (risk/100)) / 350, 2)
    st.markdown(f"<h1 style='font-family:Orbitron; text-align:center; color:white;'>{lots}</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<p class='label-mini'>A+ Fusion Score</p>", unsafe_allow_html=True)
    st.markdown("<h2 class='aplus-active'>99.2%</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:10px; color:#00ff41;'>HTF/MTF/BOOKMAP SYNC</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_mid:
    # GRAPHIQUE CENTRAL
    st.markdown("<div class='card' style='padding:5px;'>", unsafe_allow_html=True)
    components.html("""
        <div id="tv_chart" style="height:400px;"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true, "symbol": "CME_MINI:NQ1!", "interval": "5", "theme": "dark", 
          "style": "1", "container_id": "tv_chart", "backgroundColor": "#000000"
        });
        </script>
    """, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    # BOOKMAP MINI-FEED (YouTube Iframe léger)
    st.markdown("<p class='label-mini'>Live Liquidity</p>", unsafe_allow_html=True)
    st.markdown("<div class='card' style='padding:5px;'>", unsafe_allow_html=True)
    # Remplacer l'ID par un live Bookmap actif si nécessaire
    components.html("""
        <iframe width="100%" height="200" src="https://www.youtube.com/embed/live_stream?channel=UCXXXXXXXXX" frameborder="0" allowfullscreen></iframe>
    """, height=200)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # TIMER
    st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
    components.html("""
        <div id="timer" style="font-family:'Orbitron'; color:red; font-size:30px; font-weight:900;">08:14</div>
        <script>
            let s = 494; setInterval(() => {
                let m = Math.floor(s/60); let sec = s%60;
                document.getElementById('timer').innerHTML = (m<10?'0':'')+m+":"+(sec<10?'0':'')+sec;
                if(s>0) s--; else document.getElementById('timer').innerHTML="OPEN";
            }, 1000);
        </script>
    """, height=40)
    st.markdown("</div>", unsafe_allow_html=True)

# 5. MATRIX (Simplifiée pour la stabilité)
st.markdown("<p class='label-mini' style='margin-left:15px;'>Global Matrix Scan</p>", unsafe_allow_html=True)
m_cols = st.columns(5)
assets = [("NQ1!", 99), ("ES1!", 88), ("XAUUSD", 94), ("EURUSD", 96), ("BTCUSD", 91)]
for i, (name, score) in enumerate(assets):
    with m_cols[i]:
        st.markdown(f"<div style='background:#080808; border:1px solid #1a1a1a; padding:10px; text-align:center; border-bottom:3px solid red;'><b style='font-family:Orbitron;'>{name}</b><br><span style='color:red;'>{score}%</span></div>", unsafe_allow_html=True)
