import streamlit as st

# ==========================================
# 1. CONFIGURATION SYSTEME & DESIGN DARK
# ==========================================
st.set_page_config(
    page_title="HediAyoub - PREDATOR",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# STYLE RADICAL NOIR & NEON (Suppression du blanc)
st.markdown("""
    <style>
        /* Fond global et texte */
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
        
        /* Suppression des fonds blancs sur les inputs, selectbox et boutons */
        div[data-baseweb="select"] > div { background-color: #0A0A0A !important; border: 1px solid #333 !important; color: white !important; }
        div[data-baseweb="base-input"] { background-color: #0A0A0A !important; border: 1px solid #333 !important; color: white !important; }
        input { background-color: #0A0A0A !important; color: white !important; }
        
        /* Style des boutons */
        .stButton>button { background-color: #1A1A1A; color: #FF3131; border: 1px solid #FF3131; width: 100%; border-radius: 5px; transition: 0.3s; }
        .stButton>button:hover { background-color: #FF3131; color: black; }

        /* Style de la caméra et upload */
        .stCameraInput { border: 2px solid #FF3131 !important; border-radius: 10px; background-color: #050505 !important; }
        section[data-testid="stFileUploadDropzone"] { background-color: #0A0A0A !important; border: 1px dashed #333 !important; }

        /* Matrice de confluences */
        .status-cell { text-align: center; padding: 10px; border-radius: 6px; font-weight: bold; font-size: 12px; }
        .ready { background-color: #002200; color: #00FF00; border: 1px solid #00FF00; }
        .missing { background-color: #110000; color: #444444; border: 1px solid #222; }
        
        /* Carte de Verdict Final */
        .verdict-card { border: 2px solid #00FF00; padding: 30px; border-radius: 15px; background: #020A02; text-align: center; box-shadow: 0 0 15px rgba(0,255,0,0.1); }
        
        /* Titres */
        .brand-header { color: #555555; text-transform: uppercase; font-size: 12px; letter-spacing: 5px; text-align: center; }
        .app-title { color: #FF3131; text-transform: uppercase; font-size: 28px; font-weight: bold; text-align: center; text-shadow: 0 0 8px #FF3131; }
        
        /* Sidebar et Expander */
        .streamlit-expanderHeader { background-color: #0A0A0A !important; color: white !important; border: 1px solid #222 !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE SECURITE & MEMOIRE
# ==========================================
if "auth" not in st.session_state:
    st.session_state.auth = False
if 'scans' not in st.session_state:
    assets_list = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {asset: {"1D": None, "1H": None, "15M": None} for asset in assets_list}

# --- ÉCRAN DE CONNEXION ---
if not st.session_state.auth:
    st.markdown("<br><br><p class='brand-header'>HediAyoub presents</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='app-title'>The Predator</h1>", unsafe_allow_html=True)
    with st.container():
        col_l, col_c, col_r = st.columns([1, 1.5, 1])
        with col_c:
            pw = st.text_input("ALPHA_KEY", type="password")
            if st.button("EXECUTE"):
                if pw == "PREDATOR2026":
                    st.session_state.auth = True
                    st.rerun()
else:
    # --- HEADER PRINCIPAL ---
    st.markdown("<p class='brand-header'>HediAyoub presents</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='app-title'>The Predator AI</h1>", unsafe_allow_html=True)

    # ==========================================
    # 3. INTERFACE DE SCAN
    # ==========================================
    with st.expander("📸 SCANNER DATA STREAM", expanded=True):
        c1, c2, c3 = st.columns([1.5, 1, 2])
        with c1:
            active_asset = st.selectbox("TARGET", list(st.session_state.scans.keys()))
        with c2:
            active_tf = st.selectbox("TIMEFRAME", ["1D", "1H", "15M"])
        with c3:
            img = st.camera_input("SCAN")
            if img:
                st.session_state.scans[active_asset][active_tf] = img
                st.toast(f"DATA {active_asset} LOADED")

    st.divider()

    # ==========================================
    # 4. MATRICE DE DECISION
    # ==========================================
    col_table, col_verdict = st.columns([1.8, 1])

    with col_table:
        st.markdown("<p style='letter-spacing:2px; font-size:14px;'>📊 MATRIX MONITORING</p>", unsafe_allow_html=True)
        h1, h2, h3, h4 = st.columns([1.5, 1, 1, 1])
        h1.write("SYMBOLE")
        h2.write("1D")
        h3.write("1H")
        h4.write("15M")

        for asset, tfs in st.session_state.scans.items():
            r1, r2, r3, r4 = st.columns([1.5, 1, 1, 1])
            r1.write(f"**{asset}**")
            for tf, r_col in zip(["1D", "1H", "15M"], [r2, r3, r4]):
                if tfs[tf]:
                    r_col.markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else:
                    r_col.markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    with col_verdict:
        st.markdown("<p style='letter-spacing:2px; font-size:14px;'>🤖 AI ENGINE</p>", unsafe_allow_html=True)
        completed_assets = [a for a, tfs in st.session_state.scans.items() if all(tfs.values())]
        
        if completed_assets:
            target = completed_assets[0]
            st.markdown(f"""
                <div class="verdict-card">
                    <p style="color:#555; font-size:10px;">HEDIAYOUB - THE PREDATOR</p>
                    <h2 style="color:#00FF00; margin:0;">SIGNAL A+</h2>
                    <h1 style="color:white; margin:0; font-size:35px;">{target}</h1>
                    <hr style="border-color:#111;">
                    <p style="font-size:18px; color:#00FF00;">BUY / LONG</p>
                    <p style="font-size:14px;">SL: STRUCTURE | TP: LIQUIDITY</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("RESET MATRIX"):
                st.session_state.scans = {asset: {"1D": None, "1H": None, "15M": None} for asset in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.info("MATRICE INCOMPLETE")

    # Footer sidebar ultra-sombre
    st.sidebar.markdown("### 📡 ACTIVE STREAMS")
    st.sidebar.caption("NQ: jc1Ds-Uz6gE")
    st.sidebar.caption("GOLD: kvhRserj8ME")
