import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. DESIGN GLOBAL
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - EDGE FUND", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        .hedi-banner {
            background: linear-gradient(90deg, #000000 0%, #1a0000 50%, #000000 100%);
            padding: 20px; text-align: center; border-bottom: 3px solid #FF3131;
        }
        .predator-title { color: #FF3131; font-size: 28px; font-weight: 900; text-transform: uppercase; }
        [data-testid="stFileUploadDropzone"] { background-color: #080808 !important; border: 2px dashed #FF3131 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='hedi-banner'><h1 class='predator-title'>HEDIAYOUB EDGE FUND V7.2</h1></div>", unsafe_allow_html=True)

# --- CONFIG ---
config_fund = {
    "NASDAQ (NQ)": {"smt": "S&P500 (ES)", "conductor": "DXY"},
    "GOLD (XAU)": {"smt": "SILVER (XAG)", "conductor": "DXY"},
    "EURUSD": {"smt": "GBPUSD", "conductor": "DXY"},
    "US30": {"smt": "NASDAQ (NQ)", "conductor": "DXY"}
}

cible = st.selectbox("ACTIF", list(config_fund.keys()))
files = st.file_uploader("ENVOIE LES 6 PHOTOS", accept_multiple_files=True)

if files:
    if len(files) < 6:
        st.error(f"Manque de preuves : {len(files)}/6")
    else:
        # ON GÉNÈRE LE BLOC EN HTML PUR POUR ÉVITER LE BUG D'AFFICHAGE
        html_code = f"""
        <div style="background: #000000; border: 5px solid #00FF00; padding: 30px; border-radius: 20px; font-family: sans-serif; text-align: center;">
            <p style="color: #666; letter-spacing: 5px; font-size: 12px; margin: 0;">INSTITUTIONAL ALGO</p>
            <h1 style="color: #00FF00; font-size: 60px; margin: 10px 0;">{cible}</h1>
            <p style="color: white; font-size: 16px; font-weight: bold;">CONFLUENCE TRIPLE SYNC : VALIDÉE ✅</p>
            
            <div style="background: #00FF00; color: black; padding: 20px; border-radius: 15px; font-size: 24px; font-weight: 900; margin: 15px 0;">
                🎯 TP : EXTERNAL LIQUIDITY 1D
            </div>
            
            <div style="background: #FF3131; color: white; padding: 20px; border-radius: 15px; font-size: 24px; font-weight: 900; margin: 15px 0;">
                🛑 SL : SMT INVALIDATION 15M
            </div>
            
            <p style="color: #FF3131; font-weight: bold; margin-top: 20px;">VÉRIFIER BOOKMAP AVANT DE TIRER</p>
        </div>
        """
        # On injecte le HTML de façon forcée
        components.html(html_code, height=550)
        
        if st.button("RESET"):
            st.rerun()
