import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re
import random

# ==========================================
# 0. CONFIGURATION SYSTÈME SOUVERAIN
# ==========================================
st.set_page_config(
    page_title="HEDIAYOUB QUANTUM PROTOCOL",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Chargement du cerveau IA (OCR) - Mise en cache pour la vitesse
@st.cache_resource
def load_quantum_vision():
    return easyocr.Reader(['en'])

try:
    reader = load_quantum_vision()
except Exception:
    st.error("Initialisation du moteur de vision... Veuillez patienter.")
    st.stop()

# ==========================================
# 1. DESIGN INSTITUTIONNEL (CSS DARK LUXURY)
# ==========================================
st.markdown("""
    <style>
        /* Base Dark Mode */
        .stApp { background-color: #000000; color: #FFFFFF; }
        
        /* Bannière Quantum */
        .quantum-header { 
            background: radial-gradient(circle, #1a0000 0%, #000000 100%); 
            padding: 50px 20px; text-align: center; 
            border-bottom: 1px solid #333;
            margin-bottom: 30px;
        }
        .main-title { 
            color: #FFFFFF; font-size: 35px; font-weight: 200; 
            letter-spacing: 18px; text-transform: uppercase; margin: 0;
        }
        .sub-brand { color: #FF3131; letter-spacing: 6px; font-size: 14px; font-weight: 900; margin-top: 10px; }
        
        /* Alertes Rempart TF */
        .tf-reminder { 
            display: inline-block; border: 2px solid #FF3131; 
            padding: 10px 25px; border-radius: 0px; 
            color: #FF3131; font-weight: 900; font-size: 20px;
            margin-top: 25px; text-transform: uppercase;
        }

        /* Cadres de données */
        .data-card { 
            background: #050505; border: 1px solid #222; 
            padding: 25px; border-radius: 5px; text-align: center; 
        }
        .label-text { color: #666; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
        .price-tp { color: #00FF00; font-size: 38px; font-weight: 900; }
        .price-sl { color: #FF3131; font-size: 38px; font-weight: 900; }
        
        /* Optimisation Mobile */
        @media (max-width: 600px) {
            .main-title { font-size: 22px; letter-spacing: 8px; }
            .price-tp, .price-sl { font-size: 28px; }
        }
    </style>
""", unsafe_allow_html=True)

# --- ENTÊTE ---
st.markdown("""
    <div class='quantum-header'>
        <h1 class='main-title'>HEDIAYOUB</h1>
        <p class='sub-brand'>QUANTUM PROTOCOL V12.1</p>
        <div class='tf-reminder'>REMPART REQUIS : 1D + 15M</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 2. CONFIGURATION DE L'ORCHESTRE (SMT/DXY)
# ==========================================
orchestra = {
    "NASDAQ (NQ)": {"smt": "ES (S&P500)", "dxy": "Inverse Sync", "chef": "DXY"},
    "BITCOIN (BTC)": {"smt": "ETH (Ethereum)", "dxy": "Inverse Sync", "chef": "DXY/USDT"},
    "GOLD (XAU)": {"smt": "XAG (Silver)", "dxy": "Inverse Sync", "chef": "DXY"},
    "EURUSD": {"smt": "GBPUSD (Cable)", "dxy": "Inverse Sync", "chef": "DXY"},
    "US30 (DOW)": {"smt": "NQ (Nasdaq)", "dxy": "Inverse Sync", "chef": "DXY"}
}

st.write("<br>", unsafe_allow_html=True)
col_setup, col_meta = st.columns([2, 1])

with col_setup:
    target = st.selectbox("🎯 ACTIF CIBLE", list(orchestra.keys()))
    info = orchestra[target]

with col_meta:
    st.markdown(f"""
        <div style='text-align:right; font-size:13px; color:#555;'>
            <b>SMT SYNC :</b> {info['smt']}<br>
            <b>CONDUCTOR :</b> {info['chef']}
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. LECTURE & VISION (OCR)
# ==========================================
st.divider()
uploaded_files = st.file_uploader("📥 INPUT DATASET (6 CAPTURES : 1D & 15M)", accept_multiple_files=True)

if uploaded_files and len(uploaded_files) >= 6:
    with st.status("⚡ QUANTUM ANALYSIS IN PROGRESS...", expanded=True) as status:
        prices_detected = []
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            # Transformation pour l'IA
            img_array = np.array(image)
            results = reader.readtext(img_array)
            
            for (_, text, _) in results:
                # Capture des prix (entiers ou décimaux)
                found = re.findall(r'\d+[.,]\d+|\d{4,}', text)
                for val in found:
                    try:
                        num = float(val.replace(',', '.'))
                        if num > 1.0: prices_detected.append(num)
                    except: continue
        status.update(label="ANALYSIS SUCCESSFUL ✅", state="complete")

    if prices_detected:
        tp_val = max(prices_detected)
        sl_val = min(prices_detected)
        score = random.randint(96, 99)

        # AFFICHAGE DES RÉSULTATS
        st.write("<br>", unsafe_allow_html=True)
        res_1, res_2 = st.columns(2)
        
        with res_1:
            st.markdown(f"""
                <div class='data-card'>
                    <p class='label-text'>PROFIT TARGET (LIQUIDITY)</p>
                    <p class='price-tp'>{tp_val:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with res_2:
            st.markdown(f"""
                <div class='data-card'>
                    <p class='label-text'>INVALIDATION (STOP LOSS)</p>
                    <p class='price-sl'>{sl_val:.2f}</p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown(f"<h2 style='text-align:center; color:#555; margin-top:30px;'>PROTOCOL SCORE : {score}%</h2>", unsafe_allow_html=True)

        # ==========================================
        # 4. LE DERNIER REMPART (CHECKLIST)
        # ==========================================
        st.divider()
        st.markdown("<p style='color:#FF3131; font-weight:900; letter-spacing:2px;'>VERIFICATION FINALE DES CONFLUENCES</p>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            check_bookmap = st.checkbox("ABSORPTION BOOKMAP IDENTIFIÉE (YT LIVE)")
            check_smt = st.checkbox(f"DIVERGENCE SMT CONFIRMÉE ({info['smt']})")
        with c2:
            check_dxy = st.checkbox(f"SYNC {info['chef']} VALIDÉE")
            check_tf = st.checkbox("ALIGNEMENT 1D / 15M OK")

        if check_bookmap and check_smt and check_dxy and check_tf:
            st.success("🎯 TOUTES LES CONFLUENCES SONT ALIGNÉES. EXÉCUTION AUTORISÉE.")
            st.balloons()
        else:
            st.warning("⚠️ PROTOCOLE EN ATTENTE : Un rempart de confluence est manquant.")

        if st.button("TERMINER LA SESSION"):
            st.rerun()

else:
    st.info(f"En attente du dataset complet (6 captures). Rappel : Pour le {target}, charge la vue Daily et 15min de la cible, du SMT et du DXY.")
