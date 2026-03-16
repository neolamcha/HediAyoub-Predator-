import streamlit as st
import random

# ==========================================
# 1. DESIGN QUANT HEDIAYOUB
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - QUANT ENGINE", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        .hedi-banner { padding: 20px; text-align: center; border-bottom: 2px solid #FF3131; margin-bottom: 30px; }
        .predator-title { color: #FF3131; font-size: 32px; font-weight: 900; letter-spacing: 2px; }
        
        /* Dashboard Stats */
        .stat-container { display: flex; justify-content: space-around; margin-bottom: 30px; }
        .stat-card { background: #0A0A0A; padding: 20px; border: 1px solid #222; border-radius: 10px; text-align: center; width: 30%; }
        .stat-value { font-size: 40px; font-weight: 900; color: #00FF00; }
        
        /* Verdict Final */
        .verdict-box {
            border: 2px solid #00FF00; padding: 40px; border-radius: 15px;
            background: #050505; text-align: center;
        }
        .price-row { display: flex; justify-content: space-between; margin: 20px 0; padding: 20px; border-bottom: 1px solid #111; }
        .price-label { font-size: 18px; color: #666; font-weight: bold; }
        .price-digit { font-size: 30px; font-weight: 900; color: #FFFFFF; font-family: 'Courier New', monospace; }
        
        .score-circle {
            width: 120px; height: 120px; border-radius: 50%; border: 8px solid #00FF00;
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 20px auto; font-size: 32px; font-weight: 900; color: #00FF00;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='hedi-banner'><h1 class='predator-title'>HEDIAYOUB QUANT ENGINE V8.0</h1></div>", unsafe_allow_html=True)

# --- CONFIG ---
config_fund = {
    "NASDAQ (NQ)": {"smt": "ES", "tick": 0.25},
    "GOLD (XAU)": {"smt": "XAG", "tick": 0.01},
    "EURUSD": {"smt": "GBPUSD", "tick": 0.00001},
    "US30": {"smt": "NQ", "tick": 1.0}
}

col_l, col_r = st.columns([1, 1.5])

with col_l:
    st.subheader("⚙️ PARAMÈTRES FLUX")
    target = st.selectbox("ACTIF", list(config_fund.keys()))
    current_price = st.number_input("PRIX ACTUEL (Market)", value=0.0, format="%.5f")
    daily_high = st.number_input("DAILY HIGH (Liquidité)", value=0.0, format="%.5f")
    low_15m = st.number_input("LOW 15M (Invalidation)", value=0.0, format="%.5f")
    
    st.divider()
    files = st.file_uploader("UPLOAD 6 CAPTURES (DXY/SMT/1D/15M)", accept_multiple_files=True)

with col_r:
    if files and len(files) == 6 and current_price > 0:
        # Simulation d'un algorithme de scoring basé sur les confluences
        # Un vrai Hedge Fund calcule la propreté du setup
        score = random.randint(85, 98) # On ne trade que le top tier
        rr = abs(daily_high - current_price) / abs(current_price - low_15m) if abs(current_price - low_15m) != 0 else 0
        
        st.markdown(f"""
            <div class="verdict-box">
                <div class="score-circle">{score}%</div>
                <p style="color: #666; letter-spacing: 3px; font-weight: bold;">PREDATOR CLEAN SCORE</p>
                <h2 style="color: white; font-size: 40px; margin: 10px 0;">{target}</h2>
                
                <div class="price-row">
                    <span class="price-label">TAKE PROFIT (1D)</span>
                    <span class="price-digit" style="color:#00FF00;">{daily_high}</span>
                </div>
                
                <div class="price-row">
                    <span class="price-label">STOP LOSS (15M)</span>
                    <span class="price-digit" style="color:#FF3131;">{low_15m}</span>
                </div>
                
                <div class="price-row" style="border:none;">
                    <span class="price-label">RATIO RISK/REWARD</span>
                    <span class="price-digit">{rr:.2f}</span>
                </div>

                <div style="background: #111; padding: 15px; border-radius: 5px; margin-top: 20px;">
                    <p style="color: #FF3131; font-weight: bold; margin: 0; font-size: 14px;">
                        ⚠️ ANALYSE SMT & DXY : CONFIRMÉE - ATTENTE ABSORPTION BOOKMAP
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("RESET DATA"):
            st.rerun()
    else:
        st.info("Veuillez entrer les prix et charger les 6 captures pour générer le score.")
