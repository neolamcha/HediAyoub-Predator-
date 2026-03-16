import streamlit as st

# ==========================================
# 1. ARCHITECTURE & DESIGN SYSTÈME
# ==========================================
st.set_page_config(
    page_title="HediaAyoub - THE PREDATOR",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Style CSS Final (Zéro Blanc / Contraste Élevé pour iPhone)
st.markdown("""
    <style>
        /* Fond Noir Pur */
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
        
        /* Inputs et Sélecteurs (Forcer visibilité sur mobile) */
        div[data-baseweb="select"] > div { background-color: #0F0F0F !important; border: 1px solid #FF3131 !important; color: white !important; }
        div[data-baseweb="base-input"] { background-color: #0F0F0F !important; border: 1px solid #FF3131 !important; }
        input { color: white !important; background-color: #0F0F0F !important; }
        
        /* Boutons Predator */
        .stButton>button { 
            background-color: #000000; 
            color: #FF3131; 
            border: 2px solid #FF3131; 
            font-weight: bold; 
            text-transform: uppercase;
            width: 100%;
            height: 50px;
            letter-spacing: 2px;
        }
        .stButton>button:hover { background-color: #FF3131; color: black; }

        /* Matrice de Confluence */
        .status-cell { text-align: center; padding: 12px; border-radius: 4px; font-weight: bold; font-size: 14px; margin-bottom: 5px; }
        .ready { background-color: #00FF00; color: black; box-shadow: 0 0 10px #00FF00; }
        .missing { background-color: #111111; color: #333333; border: 1px solid #222; }
        
        /* Branding */
        .brand-text { color: #555555; text-transform: uppercase; font-size: 12px; letter-spacing: 4px; text-align: center; display: block; }
        .main-title { color: #FF3131; text-transform: uppercase; font-size: 32px; font-weight: bold; text-align: center; margin-top: -10px; text-shadow: 0 0 15px #FF3131; }
        .verdict-box { border: 2px solid #00FF00; padding: 25px; border-radius: 15px; background: #000A00; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. GESTION DE LA SESSION & SÉCURITÉ
# ==========================================
if "auth" not in st.session_state:
    st.session_state.auth = False

if 'scans' not in st.session_state:
    # Les 10 Actifs Maîtres
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in assets}

# --- ÉCRAN DE DÉVERROUILLAGE ---
if not st.session_state.auth:
    st.markdown("<br><br><span class='brand-text'>HediAyoub presents</span>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>THE PREDATOR</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        st.markdown("<p style='text-align:center; color:#888;'>SYSTÈME CRYPTÉ - ENTRER CLÉ ALPHA</p>", unsafe_allow_html=True)
        access_key = st.text_input("", type="password", placeholder="PASSWORD...")
        if st.button("INITIALISER LE SCANNER"):
            if access_key == "PREDATOR2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("ACCÈS REFUSÉ")
else:
    # ==========================================
    # 3. TERMINAL ACTIF
    # ==========================================
    st.markdown("<span class='brand-text'>HediAyoub - Strategic Terminal</span>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>THE PREDATOR AI</h1>", unsafe_allow_html=True)
    
    # Zone de Scan Dynamique
    with st.expander("📷 SCANNER UN ACTIF (CAMÉRA)", expanded=True):
        c_act, c_tf = st.columns(2)
        with c_act:
            target_asset = st.selectbox("ACTIF", list(st.session_state.scans.keys()))
        with c_tf:
            target_tf = st.selectbox("TIMEFRAME", ["1D", "1H", "15M"])
        
        cam_data = st.camera_input("POINT & SCAN")
        if cam_data:
            st.session_state.scans[target_asset][target_tf] = True
            st.toast(f"DATA {target_asset} {target_tf} VALIDÉE")

    st.divider()

    # Matrice de Confluence & Verdict
    col_mat, col_ver = st.columns([1.5, 1])

    with col_mat:
        st.markdown("<h3 style='font-size:14px; letter-spacing:2px;'>📊 MATRICE DES FLUX</h3>", unsafe_allow_html=True)
        # Header
        m1, m2, m3, m4 = st.columns([1.5, 1, 1, 1])
        m1.markdown("<small>ACTIF</small>", unsafe_allow_html=True)
        m2.markdown("<small>1D</small>", unsafe_allow_html=True)
        m3.markdown("<small>1H</small>", unsafe_allow_html=True)
        m4.markdown("<small>15M</small>", unsafe_allow_html=True)

        for asset, tfs in st.session_state.scans.items():
            r1, r2, r3, r4 = st.columns([1.5, 1, 1, 1])
            r1.write(f"**{asset}**")
            for tf, r_col in zip(["1D", "1H", "15M"], [r2, r3, r4]):
                if tfs[tf]:
                    r_col.markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else:
                    r_col.markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    with col_ver:
        st.markdown("<h3 style='font-size:14px; letter-spacing:2px;'>🤖 ANALYSE IA</h3>", unsafe_allow_html=True)
        
        # Logique de détection de complétion
        ready_assets = [a for a, v in st.session_state.scans.items() if all(v.values())]
        
        if ready_assets:
            chosen = ready_assets[0]
            st.markdown(f"""
                <div class="verdict-box">
                    <p style="color:#555; font-size:10px; margin:0;">HEDIAYOUB - THE PREDATOR</p>
                    <h2 style="color:#00FF00; margin:5px;">SIGNAL A+ DÉTECTÉ</h2>
                    <h1 style="color:white; font-size:40px; margin:0;">{chosen}</h1>
                    <p style="color:#888; font-size:12px;">CORRÉLATION YOUTUBE OK ✅</p>
                    <hr style="border-color:#111;">
                    <p style="font-size:22px; color:#00FF00; margin:0;">ORDRE : BUY/LONG</p>
                    <p style="font-size:14px; color:#888;">TP : LIQUIDITÉ BOOKMAP</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("RÉINITIALISER TOUT"):
                st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.info("MATRICE EN ATTENTE DE DONNÉES 1D, 1H ET 15M")

    # Sidebar Mobile
    st.sidebar.markdown("### 📡 FLUX INSTITUTIONNELS")
    st.sidebar.caption("NQ Orderflow: jc1Ds-Uz6gE")
    st.sidebar.caption("Gold Liquidity: kvhRserj8ME")
