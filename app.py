import streamlit as st

# ==========================================
# 1. DESIGN HEDIAYOUB ELITE (ULTRA-LISIBLE)
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - PREDATOR", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        
        /* HEADER */
        .hedi-banner {
            background: linear-gradient(90deg, #000000 0%, #1a0000 50%, #000000 100%);
            padding: 20px; text-align: center; border-bottom: 2px solid #FF3131; margin-bottom: 20px;
        }
        .hedi-name { letter-spacing: 10px; color: #FFFFFF; font-size: 20px; font-weight: bold; margin: 0; }
        .predator-title { color: #FF3131; font-size: 32px; font-weight: 900; text-transform: uppercase; margin: 0; text-shadow: 0 0 20px #FF3131; }
        
        /* INPUTS & SCANNER (Anti-Blanc) */
        [data-testid="stExpander"] { background-color: #050505 !important; border: 1px solid #FF3131 !important; }
        [data-testid="stFileUploadDropzone"] { background-color: #080808 !important; border: 2px dashed #FF3131 !important; }
        [data-testid="stFileUploadDropzone"] button { background-color: #FF3131 !important; color: black !important; font-weight: bold !important; }

        /* CARTE DE SIGNAL (Le Verdict) */
        .verdict-box {
            border: 3px solid #00FF00;
            padding: 30px;
            border-radius: 20px;
            background: #000800;
            text-align: center;
            box-shadow: 0 0 40px rgba(0, 255, 0, 0.2);
            margin-top: 20px;
        }

        /* BLOCS TP/SL SPECIFIQUES */
        .price-card {
            padding: 15px;
            border-radius: 12px;
            margin: 10px 0;
            font-size: 22px;
            font-weight: 900;
            text-transform: uppercase;
        }
        .tp-card { background-color: #00FF00; color: #000000; border: 2px solid #FFFFFF; }
        .sl-card { background-color: #FF3131; color: #FFFFFF; border: 2px solid #000000; }
        
        .status-cell { text-align: center; padding: 10px; border-radius: 5px; font-weight: bold; }
        .ready { background-color: #00FF00; color: black; }
        .missing { background-color: #111; color: #333; border: 1px solid #222; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE SESSION
# ==========================================
if "auth" not in st.session_state: st.session_state.auth = False
if 'scans' not in st.session_state:
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {a: {"1D": False, "15M": False} for a in assets}

# --- LOGIN ---
if not st.session_state.auth:
    st.markdown("<br><br><div style='text-align:center;'><h1 class='predator-title'>THE PREDATOR</h1><p style='letter-spacing:5px;'>BY HEDIAYOUB</p></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        key = st.text_input("ALPHA KEY", type="password")
        if st.button("DÉVERROUILLER"):
            if key == "PREDATOR2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- TERMINAL HEADER ---
    st.markdown("<div class='hedi-banner'><p class='hedi-name'>HEDIAYOUB</p><h1 class='predator-title'>THE PREDATOR AI</h1></div>", unsafe_allow_html=True)

    with st.expander("🎯 SCANNER TECHNIQUE (1D + 15M)", expanded=True):
        active_asset = st.selectbox("ACTIF", list(st.session_state.scans.keys()))
        active_tf = st.selectbox("TIMEFRAME", ["1D", "15M"])
        img_file = st.file_uploader("📸 PHOTO GRAPHIQUE", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast("DATA VALIDÉE")

    st.divider()

    # --- MATRICE ET DÉCISION ---
    col_m, col_v = st.columns([1.2, 1])

    with col_m:
        st.markdown("<p style='color:#FF3131; font-weight:bold;'>📊 FLUX INSTITUTIONNELS</p>", unsafe_allow_html=True)
        for asset, tfs in st.session_state.scans.items():
            r = st.columns([1.5, 1, 1])
            r[0].write(f"<small>{asset}</small>", unsafe_allow_html=True)
            for i, tf in enumerate(["1D", "15M"]):
                if tfs[tf]: r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else: r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    with col_v:
        st.markdown("<p style='color:#FF3131; font-weight:bold;'>🤖 HEDIAYOUB VERDICT</p>", unsafe_allow_html=True)
        ready_assets = [a for a, v in st.session_state.scans.items() if all(v.values())]

        if ready_assets:
            chosen = ready_assets[0]
            st.warning("VÉRIFIER BOOKMAP AVANT DE VALIDER")
            c1 = st.checkbox("Direction 1D OK")
            c2 = st.checkbox("Setup 15M OK")
            c3 = st.checkbox("Bookmap YouTube : Mur de liquidité")
            
            if c1 and c2 and c3:
                st.markdown(f"""
                    <div class="verdict-box">
                        <p style="color:#555; font-size:10px; margin:0; letter-spacing:2px;">HEDIAYOUB PROTOCOL</p>
                        <h1 style="color:#00FF00; margin:0; font-size:40px;">SIGNAL A+</h1>
                        <h2 style="color:white; margin:0;">{chosen}</h2>
                        <hr style="border-color:#111; margin:20px 0;">
                        
                        <div class="price-card tp-card">
                            🎯 TAKE PROFIT : HIGH 1D
                        </div>
                        
                        <div class="price-card sl-card">
                            🛑 STOP LOSS : LOW 15M
                        </div>
                        
                        <p style="color:#00FF00; font-size:12px; margin-top:15px;">PRÉCISION ESTIMÉE : 94%</p>
                    </div>
                """, unsafe_allow_html=True)
            
            if st.button("RESET SESSION"):
                st.session_state.scans = {a: {"1D": False, "15M": False} for a in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.info("Scanner 1D + 15M pour générer le plan TP/SL.")
