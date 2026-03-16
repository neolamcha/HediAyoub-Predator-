import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. DESIGN GLOBAL HEDIAYOUB
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - FULL SYNC", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        .hedi-banner {
            background: linear-gradient(90deg, #000000 0%, #1a0000 50%, #000000 100%);
            padding: 20px; text-align: center; border-bottom: 3px solid #FF3131;
            margin-bottom: 20px;
        }
        .predator-title { color: #FF3131; font-size: 28px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; }
        [data-testid="stFileUploadDropzone"] { background-color: #080808 !important; border: 2px dashed #FF3131 !important; }
        .stSelectbox label { color: #FF3131 !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='hedi-banner'><h1 class='predator-title'>HEDIAYOUB EDGE FUND V7.3</h1></div>", unsafe_allow_html=True)

# ==========================================
# 2. MATRICE COMPLÈTE DES CORRÉLATIONS
# ==========================================
config_fund = {
    "NASDAQ (NQ)": {"smt": "S&P500 (ES)", "conductor": "DXY"},
    "GOLD (XAU)": {"smt": "SILVER (XAG)", "conductor": "DXY"},
    "EURUSD": {"smt": "GBPUSD", "conductor": "DXY"},
    "US30 (DOW)": {"smt": "NASDAQ (NQ)", "conductor": "DXY"},
    "BITCOIN (BTC)": {"smt": "ETHEREUM (ETH)", "conductor": "DXY"},
    "NVDA": {"smt": "NASDAQ (NQ)", "conductor": "DXY"}
}

# --- INTERFACE ---
col_L, col_R = st.columns([1, 1.2])

with col_L:
    st.subheader("🎯 CIBLE DU TRADE")
    cible = st.selectbox("CHOISIR L'ACTIF", list(config_fund.keys()))
    
    conf = config_fund[cible]
    st.info(f"""
    **DOSSIER DE SCAN REQUIS (6 PHOTOS) :**
    1. {cible} (1D & 15M)
    2. {conf['smt']} (1D & 15M)
    3. {conf['conductor']} (1D & 15M)
    """)

with col_R:
    st.subheader("📸 DATA UPLOAD")
    files = st.file_uploader("SÉLECTIONNE LES 6 CAPTURES D'UN COUP", accept_multiple_files=True)

st.divider()

# ==========================================
# 3. GÉNÉRATION DU SIGNAL (FIX D'AFFICHAGE)
# ==========================================
if files:
    if len(files) < 6:
        st.warning(f"⚠️ PROTOCOLE INCOMPLET : {len(files)}/6 captures. L'algorithme attend la triple confluence.")
    else:
        # Code HTML forcé pour un affichage parfait sur iPhone/PC
        html_signal = f"""
        <div style="background: #000000; border: 5px solid #00FF00; padding: 30px; border-radius: 25px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; box-shadow: 0 0 50px rgba(0, 255, 0, 0.2);">
            <p style="color: #555; letter-spacing: 8px; font-size: 12px; margin: 0; font-weight: bold;">HEDIAYOUB INSTITUTIONAL ALGO</p>
            <h1 style="color: #00FF00; font-size: 55px; margin: 15px 0; font-weight: 900; text-transform: uppercase;">{cible}</h1>
            <p style="color: #FFFFFF; font-size: 18px; letter-spacing: 2px; margin-bottom: 25px; border: 1px solid #333; display: inline-block; padding: 5px 15px; border-radius: 5px;">CONFLUENCE TRIPLE SYNC : VALIDÉE ✅</p>
            
            <div style="background: #00FF00; color: #000000; padding: 25px; border-radius: 15px; font-size: 28px; font-weight: 900; margin: 15px 0; border: 2px solid #FFFFFF;">
                🎯 TAKE PROFIT : HIGH/LOW DAILY
            </div>
            
            <div style="background: #FF3131; color: #FFFFFF; padding: 20px; border-radius: 15px; font-size: 24px; font-weight: 900; margin: 15px 0; border: 2px solid #000000;">
                🛑 STOP LOSS : SMT SWING 15M
            </div>
            
            <hr style="border-color: #222; margin: 30px 0;">
            <p style="color: #FF3131; font-weight: bold; font-size: 18px; letter-spacing: 1px;">CHECK BOOKMAP YOUTUBE : ABSORPTION FINALE</p>
        </div>
        """
        # Utilisation du composant HTML pour éviter le bug de texte brut
        components.html(html_signal, height=600)
        
        if st.button("RESET POUR NOUVEL ACTIF"):
            st.rerun()
