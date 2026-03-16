import streamlit as st

# ==========================================
# 1. CONFIGURATION & DESIGN READABLE DARK
# ==========================================
st.set_page_config(page_title="THE PREDATOR", layout="wide")

st.markdown("""
    <style>
        /* Fond global noir */
        .stApp { background-color: #000000; color: #FFFFFF; }

        /* Rendre l'expander lisible (Cadre rouge, Fond noir) */
        [data-testid="stExpander"] {
            background-color: #050505 !important;
            border: 1px solid #FF3131 !important;
            border-radius: 10px !important;
        }
        [data-testid="stHeader"] { background-color: rgba(0,0,0,0); }
        
        /* Textes des labels (Actif, Timeframe) */
        label { color: #FF3131 !important; font-weight: bold !important; font-family: 'Courier New'; }

        /* Zone d'upload (Noir avec bordure rouge) */
        [data-testid="stFileUploadDropzone"] {
            background-color: #0A0A0A !important;
            border: 2px dashed #FF3131 !important;
            color: #FFFFFF !important;
            padding: 20px !important;
        }

        /* Bouton de scan (Bien visible en rouge) */
        [data-testid="stFileUploadDropzone"] button {
            background-color: #FF3131 !important;
            color: #000000 !important;
            font-weight: bold !important;
            border: none !important;
            width: 100% !important;
        }

        /* Liste déroulante (Contraste blanc sur noir) */
        div[data-baseweb="select"] > div {
            background-color: #111111 !important;
            border: 1px solid #FF3131 !important;
            color: #FFFFFF !important;
        }
        
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

        /* Matrice des flux (Lisibilité maximum) */
        .status-cell { text-align: center; padding: 10px; border-radius: 5px; font-weight: bold; }
        .ready { background-color: #00FF00; color: #000000; }
        .missing { background-color: #1A1A1A; color: #444444; border: 1px solid #333; }
        
        small { color: #FFFFFF !important; font-size: 14px !important; }
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
    # --- TERMINAL ACTIF ---
    st.markdown("<h1 class='main-title'>THE PREDATOR AI</h1>", unsafe_allow_html=True)

    with st.expander("🎯 CAPTURE HAUTE RÉSOLUTION", expanded=True):
        active_asset = st.selectbox("CIBLE", list(st.session_state.scans.keys()))
        active_tf = st.selectbox("UNITÉ DE TEMPS", ["1D", "1H", "15M"])
        
        img_file = st.file_uploader("CLIQUEZ ICI POUR SCANNER", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast(f"{active_asset} ANALYSÉ")

    st.divider()

    # Matrice de flux (Header blanc pour lisibilité)
    st.markdown("<p style='font-size:14px;color:#FF3131;letter-spacing:2px;font-weight:bold;'>📊 MATRICE DES FLUX</p>", unsafe_allow_html=True)
    
    for asset, tfs in st.session_state.scans.items():
        r = st.columns([1.5, 1, 1, 1])
        r[0].write(f"<small>{asset}</small>", unsafe_allow_html=True)
        for i, tf in enumerate(["1D", "1H", "15M"]):
            if tfs[tf]: 
                r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
            else: 
                r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    # Verdict Final
    ready = [a for a, v in st.session_state.scans.items() if all(v.values())]
    if ready:
        st.markdown(f"""
            <div style='border:2px solid #00FF00;padding:20px;border-radius:10px;text-align:center;background:#010801;margin-top:20px;'>
                <h2 style='color:#FFFFFF;margin:0;'>{ready[0]}</h2>
                <h1 style='color:#00FF00;margin:0;font-size:40px;'>SIGNAL A+</h1>
            </div>
        """, unsafe_allow_html=True)
        if st.button("RESET TOUT"):
            st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
            st.rerun()
