import streamlit as st

# ==========================================
# 1. CONFIGURATION ÉCRAN & DESIGN
# ==========================================
st.set_page_config(
    page_title="HediAyoub - PREDATOR",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# STYLE DARK MODE (Zéro Blanc)
st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
        .block-container { padding: 1rem !important; max-width: 100% !important; }
        div[data-baseweb="select"] > div { background-color: #0A0A0A !important; border: 1px solid #FF3131 !important; color: white !important; }
        div[data-baseweb="base-input"] { background-color: #0A0A0A !important; border: 1px solid #FF3131 !important; }
        input { color: white !important; }
        section[data-testid="stFileUploadDropzone"] {
            background-color: #050505 !important;
            border: 2px dashed #FF3131 !important;
            border-radius: 15px !important;
        }
        .stButton>button { 
            background-color: #111; color: #FF3131; border: 2px solid #FF3131; 
            font-weight: bold; width: 100%; height: 50px; text-transform: uppercase;
        }
        .status-cell { text-align: center; padding: 10px; border-radius: 5px; font-weight: bold; font-size: 12px; }
        .ready { background-color: #00FF00; color: black; box-shadow: 0 0 10px #00FF00; }
        .missing { background-color: #111; color: #333; border: 1px solid #222; }
        .main-title { color: #FF3131; text-transform: uppercase; font-size: 26px; font-weight: bold; text-align: center; text-shadow: 0 0 10px #FF3131; }
        .brand-text { color: #444; text-transform: uppercase; font-size: 11px; letter-spacing: 4px; text-align: center; display: block; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SÉCURITÉ & MÉMOIRE
# ==========================================
if "auth" not in st.session_state:
    st.session_state.auth = False

if 'scans' not in st.session_state:
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in assets}

# --- ÉCRAN DE DÉVERROUILLAGE ---
if not st.session_state.auth:
    st.markdown("<br><br><span class='brand-text'>HediAyoub presents</span>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>THE PREDATOR</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        key = st.text_input("ALPHA KEY", type="password", placeholder="ENTREZ LE CODE...")
        if st.button("DÉVERROUILLER"):
            if key == "PREDATOR2026":
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

    with st.expander("🎯 CAPTURE HAUTE RÉSOLUTION", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            active_asset = st.selectbox("ACTIF", list(st.session_state.scans.keys()))
        with c2:
            active_tf = st.selectbox("TIMEFRAME", ["1D", "1H", "15M"])
        
        img_file = st.file_uploader("📸 PRENDRE LA PHOTO (CLIC IPHONE)", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast(f"DATA {active_asset} VALIDÉE ✅")

    st.divider()

    col_mat, col_ver = st.columns([1.6, 1])

    with col_mat:
        st.markdown("<p style='font-size:12px; letter-spacing:2px;'>📊 MATRICE DES FLUX</p>", unsafe_allow_html=True)
        m_head = st.columns([1.5, 1, 1, 1])
        m_head[0].write("ACTIF")
        m_head[1].write("1D")
        m_head[2].write("1H")
        m_head[3].write("15M")

        for asset, tfs in st.session_state.scans.items():
            r = st.columns([1.5, 1, 1, 1])
            r[0].write(f"**{asset}**")
            for i, tf in enumerate(["1D", "1H", "15M"]):
                if tfs[tf]:
                    r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else:
                    r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    with col_ver:
        st.markdown("<p style='font-size:12px; letter-spacing:2px;'>🤖 VERDICT</p>", unsafe_allow_html=True)
        ready_assets = [a for a, v in st.session_state.scans.items() if all(v.values())]
        
        if ready_assets:
            chosen = ready_assets[0]
            st.markdown(f"""
                <div style="border:2px solid #00FF00; padding:20px; border-radius:15px; background:#010801; text-align:center;">
                    <p style="color:#555; font-size:10px; margin:0;">HEDIAYOUB - THE PREDATOR</p>
                    <h2 style="color:#00FF00; margin:5px;">SIGNAL A+ VALIDÉ</h2>
                    <h1 style="color:white; font-size:30px; margin:0;">{chosen}</h1>
                    <p style="color:#00FF00; font-size:18px;">BUY / LONG</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("RESET TOUT"):
                st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.info("MATRICE EN ATTENTE")

    st.sidebar.caption("HediAyoub - Predator Terminal")
