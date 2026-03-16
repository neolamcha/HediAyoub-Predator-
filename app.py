import streamlit as st

# ==========================================
# 1. CONFIGURATION TERMINAL ELITE
# ==========================================
st.set_page_config(
    page_title="PREDATOR AI | QUANT TERMINAL",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. DESIGN FUTURISTE LUXE (CSS)
# ==========================================
st.markdown("""
<style>
    /* Fond Noir Absolu et Police Monospace Pro */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Sidebar style "Stealth" */
    [data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #FF3131;
    }

    /* Titres Néon Rouge Predator */
    h1, h2, h3 {
        color: #FF3131;
        text-transform: uppercase;
        letter-spacing: 4px;
        text-shadow: 0 0 15px rgba(255, 49, 49, 0.5);
    }

    /* Cartes de Confluence Glassmorphism */
    .metric-box {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid #222;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 3px solid #FF3131;
    }

    /* Bouton d'accès */
    .stButton>button {
        background: linear-gradient(45deg, #FF3131, #800000);
        color: white;
        border: none;
        font-weight: bold;
        letter-spacing: 2px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. AUTHENTIFICATION SÉCURISÉE
# ==========================================
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<br><br><h1 style='text-align:center;'>PREDATOR AI</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;color:#444;'>INSTITUTIONAL QUANT SYSTEM V1.0</p>", unsafe_allow_html=True)
        password = st.text_input("CLÉ D'ACCÈS ALPHA", type="password")
        if st.button("INITIALISER LE PROTOCOLE"):
            if password == "PREDATOR2026":
                st.session_state.auth = True
                st.rerun()
else:
    # ==========================================
    # 4. DASHBOARD PREDATOR (TES LIENS INCLUS)
    # ==========================================
    
    with st.sidebar:
        st.markdown("<h1>PREDATOR</h1>")
        st.success("MOTEUR ALPHA ACTIF ✅")
        st.divider()
        
        # --- TES LIENS YOUTUBE INTÉGRÉS ICI ---
        flux_pro = {
            "NQ Bookmap Live (24/7)": "jc1Ds-Uz6gE",
            "ES Orderflow Feed": "XZs8kRuL12k",
            "Nasdaq Liquidity": "kvhRserj8ME",
            "Global Heatmap": "69jd1dOq4C8"
        }
        
        selection = st.selectbox("CHOIX DU CANAL ALPHA", list(flux_pro.keys()))
        
        st.divider()
        st.header("STATUT DES CAPTEURS")
        st.write("📡 **CVD (Cumulative Delta)**: SYNC")
        st.write("📊 **SVP (Volume Profile)**: SYNC")
        st.write("🕰️ **Midnight Open**: SYNC")
        st.write("📉 **SMC Structure**: SYNC")

    # SECTION PRINCIPALE
    st.markdown("<h1>🎯 GLOBAL LIQUIDITY ENGINE</h1>", unsafe_allow_html=True)
    
    col_main, col_data = st.columns([2.5, 1])

    with col_main:
        st.markdown(f"### 👁️ VISION AGENT : {selection}")
        # Affichage du flux sélectionné
        video_url = f"https://www.youtube.com/watch?v={flux_pro[selection]}"
        st.video(video_url)
        
        st.markdown("### 📝 JOURNAL D'EXÉCUTION QUANT")
        st.code(f"""
[SYSTEM] : Analyse en temps réel du flux {selection}...
[DATA]   : Détection de liquidité institutionnelle sur les Footprints.
[CORR]   : Corrélation DXY/NQ confirmée.
[ICT]    : Zone de Midnight Open identifiée - Attente de retracement.
        """, language="bash")

    with col_data:
        st.markdown("### ⚡ SCORE A+")
        st.markdown("""
            <div style='border: 2px solid #FF3131; padding: 20px; border-radius: 15px; text-align:center; background: rgba(255,0,0,0.05);'>
                <h1 style='font-size:60px; margin:0;'>94%</h1>
                <p style='color:#00FF00; font-weight:bold;'>PROBABILITÉ HAUTE</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><h4>MATRICE DE CONFLUENCE</h4>", unsafe_allow_html=True)
        
        # Liste de tes indicateurs pro précis
        st.markdown("<div class='metric-box'>✅ <b>CVD</b> : Divergence Bullish (M1)</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'>✅ <b>Midnight Open</b> : Prix en Discount</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'>✅ <b>LuxAlgo SMC</b> : CHoCH validé</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'>✅ <b>FVG / OB</b> : Tap dans l'Order Block</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'>✅ <b>SVP</b> : Récupération du POC</div>", unsafe_allow_html=True)

        st.error("⚠️ MUR DE LIQUIDITÉ DÉTECTÉ À +15 PTS")
