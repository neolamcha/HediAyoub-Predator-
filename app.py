import streamlit as st

# ==========================================
# 1. CONFIGURATION & STYLE RADICAL
# ==========================================
st.set_page_config(page_title="THE PREDATOR", layout="wide")

st.markdown("""
    <style>
        /* Fond global noir */
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
        
        /* --- HACK DU CARRÉ BLANC (UPLOADER) --- */
        section[data-testid="stFileUploadDropzone"] {
            background-color: #050505 !important; /* Noir profond */
            border: 2px dashed #FF3131 !important; /* Bordure rouge Predator */
            color: #FFFFFF !important;
        }
        
        /* Cacher le texte gris inutile dans le carré */
        section[data-testid="stFileUploadDropzone"] div div { color: #555 !important; }
        
        /* Bouton à l'intérieur du carré */
        section[data-testid="stFileUploadDropzone"] button {
            background-color: #111 !important;
            color: #FF3131 !important;
            border: 1px solid #FF3131 !important;
        }

        /* Inputs et Selectboxes */
        div[data-baseweb="select"] > div { background-color: #0A0A0A !important; border: 1px solid #333 !important; }
        div[data-baseweb="base-input"] { background-color: #0A0A0A !important; border: 1px solid #333 !important; }
        
        /* Titres */
        .main-title { color: #FF3131; text-transform: uppercase; font-size: 28px; font-weight: bold; text-align: center; text-shadow: 0 0 10px #FF3131; }
        .brand-text { color: #444; text-transform: uppercase; font-size: 10px; letter-spacing: 3px; text-align: center; display: block; }
        
        /* Matrice */
        .status-cell { text-align: center; padding: 8px; border-radius: 4px; font-weight: bold; }
        .ready { background-color: #00FF00; color: black; }
        .missing { background-color: #111; color: #222; border: 1px solid #222; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE SESSION
# ==========================================
if "auth" not in st.session_state: st.session_state.auth = False
if 'scans' not in st.session_state:
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in assets}

# --- LOGIN ---
if not st.session_state.auth:
    st.markdown("<br><br><span class='brand-text'>HediAyoub presents</span><h1 class='main-title'>THE PREDATOR</h1>", unsafe_allow_html=True)
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
        c1, c2 = st.columns(2)
        with c1: active_asset = st.selectbox("ACTIF", list(st.session_state.scans.keys()))
        with c2: active_tf = st.selectbox("TIMEFRAME", ["1D", "1H", "15M"])
        
        # Le bouton qui était blanc est maintenant NOIR
        img_file = st.file_uploader("CLIQUEZ ICI POUR SCANNER", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast("DATA OK")

    st.divider()

    # Matrice
    col_m, col_v = st.columns([1.5, 1])
    with col_m:
        st.markdown("<p style='font-size:12px;color:#555;'>📊 MATRICE DES FLUX</p>", unsafe_allow_html=True)
        for asset, tfs in st.session_state.scans.items():
            r = st.columns([1.5, 1, 1, 1])
            r[0].write(f"<small>{asset}</small>", unsafe_allow_html=True)
            for i, tf in enumerate(["1D", "1H", "15M"]):
                if tfs[tf]: r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else: r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    with col_v:
        st.markdown("<p style='font-size:12px;color:#555;'>🤖 AI VERDICT</p>", unsafe_allow_html=True)
        ready = [a for a, v in st.session_state.scans.items() if all(v.values())]
        if ready:
            st.markdown(f"<div style='border:2px solid #00FF00;padding:20px;border-radius:10px;text-align:center;'><h3>{ready[0]}</h3><h2 style='color:#00FF00;'>SIGNAL A+</h2></div>", unsafe_allow_html=True)
            if st.button("RESET"):
                st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.info("DATA MANQUANTE")
