import streamlit as st

# ==========================================
# 1. CONFIGURATION & DESIGN TOTAL BLACK
# ==========================================
st.set_page_config(page_title="THE PREDATOR", layout="wide")

st.markdown("""
    <style>
        /* Fond global noir absolu */
        .stApp, [data-testid="stAppViewContainer"] { 
            background-color: #000000 !important; 
            color: #FFFFFF !important; 
        }

        /* 1. FIX EXPANDER (Le titre "Capture Haute Résolution" qui était blanc) */
        .streamlit-expanderHeader {
            background-color: #000000 !important;
            color: #FF3131 !important;
            border: 1px solid #222 !important;
        }
        .streamlit-expanderContent {
            background-color: #000000 !important;
            border: 1px solid #222 !important;
        }

        /* 2. FIX UPLOADER (Le gros carré Drag & Drop) */
        [data-testid="stFileUploadDropzone"] {
            background-color: #050505 !important;
            border: 2px dashed #FF3131 !important;
        }
        [data-testid="stFileUploadDropzone"] p, [data-testid="stFileUploadDropzone"] small {
            color: #444 !important; /* Rend le texte "Limit 200MB" presque invisible */
        }

        /* 3. FIX BOUTON INTERNE (Le bouton "Browse files") */
        [data-testid="stFileUploadDropzone"] button {
            background-color: #FF3131 !important;
            color: black !important;
            border: none !important;
        }

        /* 4. FIX INPUTS (Cases NASDAQ, 15M, etc.) */
        div[data-baseweb="select"] > div { 
            background-color: #0A0A0A !important; 
            border: 1px solid #FF3131 !important; 
            color: white !important; 
        }
        
        /* Titres & Branding */
        .main-title { 
            color: #FF3131; 
            text-transform: uppercase; 
            font-size: 28px; 
            font-weight: bold; 
            text-align: center; 
            text-shadow: 0 0 15px #FF3131; 
            margin-bottom: 20px;
        }

        /* Matrice de confluences */
        .status-cell { text-align: center; padding: 10px; border-radius: 5px; font-weight: bold; font-size: 12px; }
        .ready { background-color: #00FF00; color: black; box-shadow: 0 0 10px #00FF00; }
        .missing { background-color: #0A0A0A; color: #333; border: 1px solid #222; }

        /* Cacher les éléments Streamlit inutiles */
        #MainMenu, footer, header {visibility: hidden;}
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
        c1, c2 = st.columns(2)
        with c1: active_asset = st.selectbox("ACTIF", list(st.session_state.scans.keys()))
        with c2: active_tf = st.selectbox("TIMEFRAME", ["1D", "1H", "15M"])
        
        img_file = st.file_uploader("CLIQUEZ ICI POUR SCANNER", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast(f"{active_asset} LOADED")

    st.divider()

    # Matrice de flux
    st.markdown("<p style='font-size:12px;color:#555;letter-spacing:2px;'>📊 MATRICE DES FLUX</p>", unsafe_allow_html=True)
    for asset, tfs in st.session_state.scans.items():
        r = st.columns([1.5, 1, 1, 1])
        r[0].write(f"<small>{asset}</small>", unsafe_allow_html=True)
        for i, tf in enumerate(["1D", "1H", "15M"]):
            if tfs[tf]: r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
            else: r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    # Verdict
    ready = [a for a, v in st.session_state.scans.items() if all(v.values())]
    if ready:
        st.markdown(f"""
            <div style='border:2px solid #00FF00;padding:20px;border-radius:10px;text-align:center;background:#010801;margin-top:20px;'>
                <h3 style='margin:0;'>{ready[0]}</h3>
                <h2 style='color:#00FF00;margin:0;'>SIGNAL A+ DÉTECTÉ</h2>
            </div>
        """, unsafe_allow_html=True)
        if st.button("RESET"):
            st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
            st.rerun()
