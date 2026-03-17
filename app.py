import streamlit as st
import time
import random

# 1. SETUP & HIDING OVERLAYS
st.set_page_config(page_title="HEDI AYOUB", layout="centered")

st.markdown("""
    <style>
        /* Masquage complet des éléments techniques */
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        .stDeployButton {display:none !important;}
        div[data-testid="stToolbar"] {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;900&display=swap');
        
        .stApp { 
            background: radial-gradient(circle at top right, #0a0f14, #030608); 
            color: #FFFFFF; 
            font-family: 'Inter', sans-serif; 
        }
        
        .block-container { padding-top: 30px !important; max-width: 380px; padding-bottom: 120px; }

        /* HEADER PREMIUM */
        .identity-header { text-align: center; margin-bottom: 50px; }
        .name-hedi { font-size: 42px; font-weight: 100; letter-spacing: 22px; margin-bottom: -10px; opacity: 0.95; }
        .name-ayoub { font-size: 42px; font-weight: 100; letter-spacing: 22px; opacity: 0.95; }
        .sub-tag { color: #FF3131; font-size: 10px; font-weight: 900; letter-spacing: 5px; margin-top: 20px; opacity: 0.8; }

        /* GLASS CARD DESIGN */
        .glass-card {
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 25px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        /* SCORE RADIAL SIMULATION */
        .score-display {
            font-size: 60px; font-weight: 100; color: #00FF66;
            text-shadow: 0 0 20px rgba(0, 255, 102, 0.3);
            margin: 10px 0;
        }

        /* TYPOGRAPHIE */
        .label-mini { font-size: 9px; color: #555; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; }
        .val-main { font-size: 24px; font-weight: 200; letter-spacing: 1px; }
        .val-red { color: #FF3131; font-weight: 400; }
        .val-green { color: #00FF66; font-weight: 400; }

        /* NAV BAR GLASS */
        .nav-bar {
            position: fixed; bottom: 35px; left: 50%; transform: translateX(-50%);
            width: 240px; display: flex; justify-content: space-around;
            background: rgba(20, 20, 20, 0.7); backdrop-filter: blur(20px);
            padding: 18px; border-radius: 40px; border: 1px solid rgba(255,255,255,0.05);
            z-index: 9999;
        }

        /* BOUTON ÉLÉGANT */
        .stButton > button {
            background: transparent !important;
            color: #FF3131 !important;
            border: 1px solid #FF3131 !important;
            border-radius: 50px !important;
            font-weight: 100 !important;
            letter-spacing: 3px !important;
            transition: 0.3s;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class='identity-header'>
        <div class='name-hedi'>HEDI</div>
        <div class='name-ayoub'>AYOUB</div>
        <div class='sub-tag'>QUANTUM TERMINAL V21.0</div>
    </div>
""", unsafe_allow_html=True)

# --- SELECTION ACTIF ---
assets = {
    "US30": 38450.0, "NASDAQ": 17820.5, "GOLD": 2155.20, "EURUSD": 1.0852, "BITCOIN": 64200.0
}
target = st.selectbox("", list(assets.keys()), label_visibility="collapsed")

# --- UPLOAD ZONE ---
uploaded = st.file_uploader("", accept_multiple_files=True, label_visibility="collapsed")

if uploaded and len(uploaded) >= 6:
    if st.button("EXECUTE QUANTUM SCAN"):
        with st.status("📡 INITIALIZING DATA EXTRACTION...", expanded=False):
            time.sleep(1.5)
        
        # Simulation Data
        score = random.randint(91, 99)
        order = random.choice(["BUY MARKET", "SELL MARKET", "BUY LIMIT", "SELL LIMIT"])
        price = assets[target]
        tp = price + (price * 0.012) if "BUY" in order else price - (price * 0.012)
        sl = price - (price * 0.004) if "BUY" in order else price + (price * 0.004)

        # AFFICHAGE GLASSMOPHISM
        st.markdown(f"""
            <div class='glass-card' style='text-align: center;'>
                <div class='label-mini'>Probability Accuracy</div>
                <div class='score-display'>{score}%</div>
            </div>

            <div class='glass-card'>
                <div class='label-mini'>Market Execution</div>
                <div class='val-main val-red'>{order}</div>
                <div style='margin-top:15px; border-top:1px solid rgba(255,255,255,0.05); padding-top:15px;'>
                    <div style='display: flex; justify-content: space-between;'>
                        <div><div class='label-mini'>Entry Price</div><div class='val-main'>{price}</div></div>
                        <div style='text-align:right;'><div class='label-mini'>Asset</div><div class='val-main'>{target}</div></div>
                    </div>
                </div>
            </div>

            <div class='glass-card' style='border-bottom: 2px solid #FF3131;'>
                <div style='display: flex; justify-content: space-between;'>
                    <div><div class='label-mini'>Take Profit</div><div class='val-main val-green'>{tp:.2f if target != "EURUSD" else f"{tp:.4f}"}</div></div>
                    <div style='text-align:right;'><div class='label-mini'>Stop Loss</div><div class='val-main'>{sl:.2f if target != "EURUSD" else f"{sl:.4f}"}</div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div style='height: 200px; display: flex; flex-direction: column; align-items: center; justify-content: center; border: 1px dashed rgba(255,49,49,0.1); border-radius: 30px; margin-top: 20px;'>
            <div style='font-size: 30px; margin-bottom: 10px; opacity: 0.2;'>📡</div>
            <div style='font-size: 8px; letter-spacing: 3px; color: #444; font-weight: 900;'>WAITING FOR 6 DATASETS</div>
        </div>
    """, unsafe_allow_html=True)

# --- NAV BAR ---
st.markdown("""
    <div class='nav-bar'>
        <div style='font-size: 20px; opacity: 0.2;'>🌍</div>
        <div style='font-size: 20px; opacity: 0.2;'>🧭</div>
        <div style='font-size: 20px; color: #FF3131; filter: drop-shadow(0 0 8px #FF3131);'>👑</div>
    </div>
""", unsafe_allow_html=True)
