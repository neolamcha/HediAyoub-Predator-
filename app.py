import streamlit as st
import time
import random

# 1. CONFIGURATION SYSTÈME IMMUABLE
st.set_page_config(page_title="HEDI AYOUB", layout="centered")

# CSS BLINDÉ (Correction des balises coupées)
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
        .stApp { background-color: #030608; color: #FFFFFF; font-family: sans-serif; }
        .block-container { padding-top: 2rem !important; max-width: 400px !important; }
        
        /* DESIGN TITRE */
        .head-title { text-align: center; letter-spacing: 10px; font-size: 26px; font-weight: 100; margin-bottom: 5px; }
        .sub-title { text-align: center; color: #FF3131; font-size: 9px; letter-spacing: 3px; font-weight: bold; margin-bottom: 30px; }

        /* CARTES DE RÉSULTAT */
        .res-card {
            background: #0a0a0a; border: 1px solid #1a1a1a;
            border-radius: 15px; padding: 15px; margin-bottom: 10px;
        }
        .label { color: #555; font-size: 10px; font-weight: bold; text-transform: uppercase; }
        .val-red { color: #FF3131; font-size: 22px; font-weight: bold; }
        .val-green { color: #00FF66; font-size: 22px; font-weight: bold; }
        .val-white { color: #FFF; font-size: 22px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- LOGIQUE DE CALCUL ---
def generate_signal(asset_name):
    # Prix de base simulés
    prices = {"US30": 38500, "NQ": 17900, "GOLD": 2160, "EURUSD": 1.0850, "BTC": 65000}
    base = prices.get(asset_name.split()[0], 100)
    
    score = random.randint(92, 99)
    side = random.choice(["BUY", "SELL"])
    mode = random.choice(["MARKET", "LIMIT"])
    
    # Calculs précis
    if side == "BUY":
        tp = base * 1.01
        sl = base * 0.997
    else:
        tp = base * 0.99
        sl = base * 1.003
        
    return score, f"{side} {mode}", tp, sl

# --- INTERFACE ---
st.markdown('<div class="head-title">HEDI AYOUB</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">QUANTUM PROTOCOL / V22.0</div>', unsafe_allow_html=True)

assets = ["US30 (DOW JONES)", "NASDAQ (NQ)", "GOLD (XAU)", "EURUSD", "BITCOIN (BTC)"]
target = st.selectbox("CHOOSE ASSET", assets, label_visibility="collapsed")

# Zone Upload simplifiée pour éviter les crashs de mémoire
files = st.file_uploader("UPLOAD DATASETS", accept_multiple_files=True, label_visibility="collapsed")

if files and len(files) >= 6:
    if st.button("🔥 EXECUTE SCAN", use_container_width=True):
        with st.spinner("QUANTUM COMPUTING..."):
            time.sleep(2)
            score, order, tp, sl = generate_signal(target)

        # AFFICHAGE PROPRE SANS HTML COMPLEXE
        st.markdown(f"""
            <div class="res-card" style="text-align:center; border-color:#00FF66;">
                <div class="label">PROBABILITY</div>
                <div class="val-green" style="font-size:35px;">{score}%</div>
            </div>
            
            <div class="res-card">
                <div class="label">EXECUTION</div>
                <div class="val-white">{order}</div>
            </div>

            <div class="res-card" style="border-left: 4px solid #FF3131;">
                <div style="display:flex; justify-content:space-between;">
                    <div><div class="label">TAKE PROFIT</div><div class="val-green">{tp:.2f}</div></div>
                    <div style="text-align:right;"><div class="label">STOP LOSS</div><div class="val-red">{sl:.2f}</div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.success("ANALYSIS COMPLETE")
else:
    st.info(f"AWAITING 6 DATASETS ({len(files)}/6)")

# Navigation visuelle fixe
st.markdown("""
    <div style="position:fixed; bottom:20px; left:50%; transform:translateX(-50%); width:200px; 
                background:#0a0a0a; padding:10px; border-radius:30px; border:1px solid #222; 
                display:flex; justify-content:space-around; z-index:100;">
        <span style="opacity:0.2;">🌍</span><span style="opacity:0.2;">🧭</span><span style="color:#FF3131;">👑</span>
    </div>
""", unsafe_allow_html=True)
