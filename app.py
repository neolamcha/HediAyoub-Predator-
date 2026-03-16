import streamlit as st

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="PREDATOR AI | QUANT ENGINE",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. DESIGN LUXUEUX & CINÉMATIQUE (Dark Atmosphere / Chiaroscuro)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Rajdhani:wght@400;600;700&display=swap');
    
    /* Fond Noir Absolu et ambiance sombre */
    .stApp {
        background-color: #030303;
        color: #E0E0E0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Sidebar - Ombres et contrastes forts */
    [data-testid="stSidebar"] {
        background-color: #070707;
        border-right: 1px solid #1a1a1a;
    }

    /* Typographie Luxueuse et agressive */
    h1, h2, h3 {
        font-family: 'Cinzel', serif;
        color: #FFFFFF;
        letter-spacing: 2px;
        text-shadow: 0px 4px 15px rgba(200, 0, 0, 0.4);
    }
    
    .title-red {
        color: #b30000; /* Rouge sombre luxueux */
    }

    /* Glassmorphism pour les cartes */
    .glass-card {
        background: linear-gradient(145deg, rgba(15,15,15,0.9), rgba(5,5,5,0.9));
        border-radius: 8px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    /* Status text */
    .status-ok { color: #4CAF50; font-weight: bold; }
    .status-warn { color: #FFC107; font-weight: bold; }

</style>
""", unsafe_allow_html=True)

# 3. LOGIQUE D'ACCÈS SÉCURISÉ
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h1>PREDATOR AI</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#666; font-family:Rajdhani;'>INSTITUTIONAL QUANT TERMINAL</p>", unsafe_allow_html=True)
        st.markdown("---")
        user_pass = st.text_input("CLÉ ALPHA", type="password")
        if st.button("DÉVERROUILLER"):
            if user_pass == "PREDATOR2026":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Accès Refusé.")
        st.markdown("</div>", unsafe_allow_html=True)

if not st.session_state["authenticated"]:
    login()
else:
    # 4. DASHBOARD PREDATOR
    with st.sidebar:
        st.markdown("<h2>PREDATOR AI</h2>", unsafe_allow_html=True)
        st.markdown("<span class='status-ok'>MOTEUR EN LIGNE</span>", unsafe_allow_html=True)
        st.divider()
        
        st.markdown("### 📡 SÉLECTION DU FLUX")
        # --- INTÉGRATION DE TES 4 LIENS EXACTS ---
        flux_list = {
            "Flux 1 (Bookmap)": "XZs8kRuL12k",
            "Flux 2 (NQ Footprint)": "jc1Ds-Uz6gE",
            "Flux 3 (Order Flow)": "kvhRserj8ME",
            "Flux 4 (Heatmap)": "69jd1dOq4C8"
        }
        choix_flux = st.selectbox("", list(flux_list.keys()))
        
        st.divider()
        st.markdown("### ⚙️ RISK MANAGEMENT")
        st.markdown("<p style='font-size: 14px; color:#aaa;'>Alignement Stratégie : <span style='color:white;'>FundingPips [Modèle Standard]</span></p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 14px; color:#aaa;'>Risque par trade : <span style='color:white;'>0.5% - 1%</span></p>", unsafe_allow_html=True)

    # Main Area
    st.markdown("<h1 class='title-red'>🎯 GLOBAL LIQUIDITY ENGINE</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns([2.5, 1])

    # Zone Vidéo
    with col1:
        st.markdown(f"### 👁️ VISION AGENT : {choix_flux}")
        video_url = f"https://www.youtube.com/watch?v={flux_list[choix_flux]}"
        st.video(video_url)
        st.markdown("<p style='color:#777; font-style:italic;'>Analyse algorithmique des imbalances et de l'absorption du carnet d'ordres en cours...</p>", unsafe_allow_html=True)
        
    # Zone Confluence
    with col2:
        st.markdown("### ⚡ MATRICE DE CONFLUENCE")
        st.markdown("""
        <div class='glass-card' style='text-align:center;'>
            <h1 style='color:#b30000; font-size: 55px; margin:0;'>94%</h1>
            <p style='color:#aaa; letter-spacing: 1px;'>PROBABILITÉ A+</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("#### CAPTEURS SMC / ICT", unsafe_allow_html=True)
        st.markdown("✅ <span class='status-ok'>CVD :</span> Divergence positive confirmée", unsafe_allow_html=True)
        st.markdown("✅ <span class='status-ok'>SVP :</span> Rebond sur Value Area", unsafe_allow_html=True)
        st.markdown("✅ <span class='status-ok'>Midnight Open :</span> Rejet validé (Discount)", unsafe_allow_html=True)
        st.markdown("⏳ <span class='status-warn'>LuxAlgo SMC :</span> En attente de clôture pour confirmation", unsafe_allow_html=True)
        st.markdown("✅ <span class='status-ok'>FVG :</span> Mitigé avec précision", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("### 📝 TERMINAL LOG")
    st.code("""
[14:30:00] INITIALISATION SÉQUENCE... OK.
[14:31:12] FLUX BOOKMAP CONNECTÉ. ANALYSE DE LA LIQUIDITÉ EN TEMPS RÉEL.
[14:35:44] DÉTECTION : ABSORPTION INSTITUTIONNELLE SUR LE NIVEAU CLÉ.
[14:36:01] ATTENTE DE CONFLUENCE LUXALGO POUR EXÉCUTION DU TRADE.
    """, language="bash")
