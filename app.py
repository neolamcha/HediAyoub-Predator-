import streamlit as st

# ==========================================
# 1. CONFIGURATION & HACK CSS RADICAL
# ==========================================
st.set_page_config(page_title="THE PREDATOR", layout="wide")

st.markdown("""
    <style>
        /* 1. FORCE LE NOIR SUR TOUTES LES COUCHES SYSTEME */
        html, body, [data-testid="stAppViewContainer"], .stApp {
            background-color: #000000 !important;
            color: #FFFFFF !important;
        }

        /* 2. TUER LE BLANC DE L'EXPANDER (L'en-tête et le contour) */
        [data-testid="stExpander"] {
            background-color: #000000 !important;
            border: 1px solid #FF3131 !important;
            border-radius: 10px !important;
        }
        [data-testid="stExpander"] summary {
            background-color: #000000 !important;
            color: #FF3131 !important;
        }
        [data-testid="stExpander"] svg {
            fill: #FF3131 !important;
        }

        /* 3. TUER LE BLANC DE LA ZONE D'UPLOAD (Le carré et son contenu) */
        [data-testid="stFileUploadDropzone"] {
            background-color: #000000 !important;
            border: 2px dashed #FF3131 !important;
            color: #FFFFFF !important;
        }
        
        /* Cacher le texte gris clair 'Drag and drop' qui fait 'tache' */
        [data-testid="stFileUploadDropzone"] div div {
            color: #000000 !important; /* Le rend invisible sur fond noir */
        }
        
        /* Forcer le bouton 'Browse files' en Rouge Predator */
        [data-testid="stFileUploadDropzone"] button {
            background-color: #FF3131 !important;
            color: #000000 !important;
            border-radius: 5px !important;
            font-weight: bold !important;
        }

        /* 4. FIX DES MENUS DÉROULANTS (NASDAQ, 15M...) */
        div[data-baseweb="select"] > div {
            background-color: #000000 !important;
            border: 1px solid #FF3131 !important;
        }
        div[role="listbox"] {
            background-color: #000000 !important;
            color: white !important;
        }

        /* 5. CACHER LE HEADER STREAMLIT ET LA LIGNE BLANCHE EN HAUT */
        header {visibility: hidden !important;}
        [data-testid="stHeader"] {background-color: rgba(0,0,0,0) !important;}
        footer {visibility: hidden !important;}

        /* Titre Néon */
        .main-title {
            color: #FF3131;
            text-transform: uppercase;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            text-shadow: 0 0 15px #FF3131;
            margin-bottom: 20px;
        }
        
        /* Matrice */
        .status-cell { text-align: center; padding: 10px; border-radius: 5px; font-weight: bold; font-size: 12px; }
        .ready { background-color: #00FF00; color: black; box-shadow: 0 0 10px #00FF00; }
        .missing { background-color: #050505; color: #222; border: 1px solid #111; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE SESSION
# ==========================================
if "auth" not in st.session_state: st.session_state.auth = False
if 'scans' not in st.session_state:
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in assets}

# --- LOGIN SCREEN ---
if not st.session_state.auth:
    st.markdown("<br><br><h1 class='main-title'>THE PREDATOR</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        key = st.text_input("ALPHA KEY", type="password")
        if st.button("EXECUTE"):
            if key == "PREDATOR2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- TERMINAL ---
    st.markdown("<h1 class='main-title'>THE PREDATOR AI</h1>", unsafe_allow_html=True)

    with st.expander("🎯 CAPTURE HAUTE RÉSOLUTION", expanded=True):
        active_asset = st.selectbox("ACTIF", list(st.session_state.scans.keys()))
        active_tf = st.selectbox("TIMEFRAME", ["1D", "1H", "15M"])
        
        img_file = st.file_uploader("CLIQUEZ ICI POUR SCANNER", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast(f"{active_asset} LOADED")

    st.divider()

    # Matrice
    for asset, tfs in st.session_state.scans.items():
        r = st.columns([1.5, 1, 1, 1])
        r[0].write(f"<small>{asset}</small>", unsafe_allow_html=True)
        for i, tf in enumerate(["1D", "1H", "15M"]):
            if tfs[tf]: r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
            else: r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    # Verdict
    ready = [a for a, v in st.session_state.scans.items() if all(v.values())]
    if ready:
        st.markdown(f"<div style='border:2px solid #00FF00;padding:20px;border-radius:10px;text-align:center;background:#010801;margin-top:20px;'><h3>{ready[0]}</h3><h2 style='color:#00FF00;'>SIGNAL A+</h2></div>", unsafe_allow_html=True)
        if st.button("RESET"):
            st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
            st.rerun()
