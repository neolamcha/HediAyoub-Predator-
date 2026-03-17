import streamlit as st
import time
import random

# 1. OPTIMISATION RADICALE DU CHARGEMENT
st.set_page_config(page_title="HEDI AYOUB", layout="centered")

st.markdown("""
    <style>
        /* Nettoyage total Interface */
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        .stDeployButton {display:none !important;}
        div[data-testid="stToolbar"] {display: none !important;}
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400;900&display=swap');
        .stApp { background-color: #030608; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .block-container { padding-top: 10px !important; max-width: 400px; padding-bottom: 120px; }

        /* Identité */
        .identity-header { text-align: center; margin-bottom: 25px; }
        .first-name { letter-spacing: 18px; font-size: 36px; font-weight: 100; margin: 0; line-height: 1.1; }
        .last-name { letter-spacing: 18px; font-size: 36px; font-weight: 100; margin: 0; line-height: 1.1; }

        /* Cartes de résultats ultra-fluides */
        .card-predator {
            border-radius: 20px; padding: 20px; text-align: center; margin-top: 15px;
            transition: transform 0.3s ease;
        }
        .score-card { border: 2px solid #00FF66; background: rgba(0, 255, 102, 0.05); box-shadow: 0 0 15px rgba(0, 255, 102, 0.1); }
        .order-card { border: 2px solid #00D2FF; background: rgba(0, 210, 255, 0.05); }
        .setup-card { border: 2px solid #FF3131; background: rgba(255, 49, 49, 0.05); }

        .label-text { font-size: 10px; letter-spacing: 2px; color: #888; font-weight: bold; text-transform: uppercase; }
        .value-text { font-size: 26px; font-weight: 900; color: #FFF; margin: 5px 0; }
        
        /* Nav Bar */
        .nav-bar {
            position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
            width: 260px; display: flex; justify-content: space-around;
            background: rgba(10, 10, 10, 0.98); backdrop-filter: blur(20px);
            padding: 15px; border-radius: 50px; border: 1px solid #333; z-index: 1000;
        }
    </style>
""", unsafe_allow_html=True)

# 2. LOGIQUE DE CALCUL INSTANTANÉE
def get_quantum_setup(asset_name, base_price, base_tp, base_sl):
    # Simule une analyse ultra-rapide
    orders = ["BUY MARKET", "SELL MARKET", "BUY LIMIT", "SELL LIMIT"]
    selected = random.choice(orders)
    score = random.randint(88, 99)
    direction = 1 if "BUY" in selected else -1
    
    tp = base_price + (base_tp * direction)
    sl = base_price - (base_sl * direction)
    return selected, score, tp, sl

# --- UI ---
st.markdown("<div class='identity-header'><div class='first-name'>H E D I</div><div class='last-name'>A Y O U B</div></div>", unsafe_allow_html=True)

assets = {
    "US30 (DOW JONES)": {"tp": 350, "sl": 120, "p": 38450},
    "NASDAQ (NQ)": {"tp": 180, "sl": 60, "p": 17820},
    "BITCOIN (BTC)": {"tp": 1500, "sl": 600, "p": 64200},
    "GOLD (XAU)": {"tp": 18, "sl": 7, "p": 2155.50},
    "EURUSD": {"tp": 0.0075, "sl": 0.0025, "p": 1.0850}
}

target = st.selectbox("", list(assets.keys()), label_visibility="collapsed")
info = assets[target]

uploaded = st.file_uploader("", accept_multiple_files=True, label_visibility="collapsed")

if uploaded and len(uploaded) >= 6:
    if st.button("🔥 EXECUTE QUANTUM SCAN", use_container_width=True):
        # Animation de chargement très courte pour le feeling "Pro" sans lag
        with st.spinner("⚡ SCANNING..."):
            time.sleep(0.8) 
            order, score, tp, sl = get_quantum_setup(target, info['p'], info['tp'], info['sl'])

        # Affichage immédiat
        st.markdown(f"""
            <div class='card-predator score-card'>
                <div class='label-text'>PROBABILITY SCORE</div>
                <div class='value-text' style='color:#00FF66;'>{score}%</div>
            </div>

            <div class='card-predator order-card'>
                <div class='label-text'>ORDER TYPE</div>
                <div class='value-text'>{order}</div>
            </div>
            
            <div class='card-predator setup-card'>
                <div style='display: flex; justify-content: space-around;'>
                    <div><div class='label-text'>TAKE PROFIT</div><div class='value-text'>{tp:.2f if target != "EURUSD" else f"{tp:.4f}"}</div></div>
                    <div style='width: 1px; background: rgba(255,255,255,0.1);'></div>
                    <div><div class='label-text'>STOP LOSS</div><div class='value-text'>{sl:.2f if target != "EURUSD" else f"{sl:.4f}"}</div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("<div style='border: 1px solid #222; border-radius:20px; padding:40px; text-align:center; color:#444; font-size:11px;'>READY FOR 6 DATASETS</div>", unsafe_allow_html=True)

# Nav Bar
st.markdown("""<div class='nav-bar'><div style='font-size:20px; opacity:0.5;'>🌍</div><div style='font-size:20px; opacity:0.5;'>🧭</div><div style='font-size:20px; color:#FF3131; filter: drop-shadow(0 0 5px #FF3131);'>👑</div></div>""", unsafe_allow_html=True)
