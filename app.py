import streamlit as st

# ==========================================
# 1. CONFIGURATION & DESIGN HEDIAYOUB ELITE
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - PREDATOR", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        
        /* SIGNATURE HEADER */
        .hedi-header {
            text-align: center;
            color: #FFFFFF;
            letter-spacing: 5px;
            font-size: 14px;
            font-weight: 300;
            margin-top: -50px;
            padding-bottom: 10px;
            border-bottom: 1px solid #111;
        }
        
        .main-title {
            color: #FF3131;
            text-transform: uppercase;
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            text-shadow: 0 0 20px #FF3131;
            margin-top: 10px;
        }

        /* BOITES ET BOUTONS */
        [data-testid="stExpander"] { background-color: #050505 !important; border: 1px solid #FF3131 !important; }
        label { color: #FF3131 !important; font-weight: bold !important; }
        [data-testid="stFileUploadDropzone"] { background-color: #0A0A0A !important; border: 2px dashed #FF3131 !important; }
        
        /* Bouton Scan Style HediAyoub */
        [data-testid="stFileUploadDropzone"] button {
            background-color: #FF3131 !important;
            color: #000000 !important;
            font-weight: bold !important;
            box-shadow: 0 0 10px #FF3131;
        }

        /* MATRICE */
        .status-cell { text-align: center; padding: 10px; border-radius: 5px; font-weight: bold; }
        .ready { background-color: #00FF00; color: #000000; box-shadow: 0 0 10px #00FF00; }
        .missing { background-color: #111; color: #333; border: 1px solid #222; }
        
        /* VERDICT SIGNÉ */
        .verdict-box {
            border: 2px solid #00FF00;
            padding: 25px;
            border-radius: 20px;
            background: linear-gradient(180deg, #010801 0%, #000000 100%);
            text-align: center;
            box-shadow: 0 0 30px rgba(0, 255, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE & SÉCURITÉ
# ==========================================
if "auth" not in st.session_state: st.session_state.auth = False
if 'scans' not in st.session_state:
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in assets}

# --- LOGIN SCREEN ---
if not st.session_state.auth:
    st.markdown("<h1 class='main-title'>THE PREDATOR</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white; letter-spacing:3px;'>BY HEDIAYOUB</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        key = st.text_input("ALPHA KEY", type="password")
        if st.button("INITIALISER"):
            if key == "PREDATOR2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- TERMINAL ACTIF ---
    st.markdown("<div class='hedi-header'>HEDIAYOUB STRATEGIC TERMINAL</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>THE PREDATOR AI</h1>", unsafe_allow_html=True)

    # ALARMES
    st.markdown("""
        <div style='border: 1px solid #333; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 20px;'>
            <p style='color:#FF3131; margin:0; font-size:10px;'>HEDIAYOUB ALGO CLOCK</p>
            <p style='font-size:16px; color:white;'>08:55 | 14:25 | 19:55</p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("🎯 CAPTURE HAUTE RÉSOLUTION", expanded=True):
        active_asset = st.selectbox("CIBLE", list(st.session_state.scans.keys()))
        active_tf = st.selectbox("UNITÉ DE TEMPS", ["1D", "1H", "15M"])
        img_file = st.file_uploader("OUVRIR CAMÉRA IPHONE", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast(f"HediaAyoub Analysis: {active_asset} OK")

    st.divider()

    # MATRICE ET VERDICT
    col_m, col_v = st.columns([1.5, 1])

    with col_m:
        st.markdown("<p style='font-size:12px;color:#FF3131;font-weight:bold;'>📊 FLUX INSTITUTIONNELS</p>", unsafe_allow_html=True)
        for asset, tfs in st.session_state.scans.items():
            r = st.columns([1.5, 1, 1, 1])
            r[0].write(f"<small style='color:white;'>{asset}</small>", unsafe_allow_html=True)
            for i, tf in enumerate(["1D", "1H", "15M"]):
                if tfs[tf]: r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else: r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    with col_v:
        st.markdown("<p style='font-size:12px;color:#FF3131;font-weight:bold;'>🤖 HEDIAYOUB AI VERDICT</p>", unsafe_allow_html=True)
        ready_assets = [a for a, v in st.session_state.scans.items() if all(v.values())]

        if ready_assets:
            st.markdown(f"""
                <div class="verdict-box">
                    <p style="color:#555; font-size:10px; margin:0; letter-spacing:2px;">OFFICIAL ANALYSIS BY</p>
                    <h2 style="color:white; margin:0; letter-spacing:3px;">HEDIAYOUB</h2>
                    <hr style="border-color:#111; margin:10px 0;">
                    <h1 style="color:#00FF00; margin:0; font-size:30px;">{ready_assets[0]}</h1>
                    <h2 style="color:#00FF00; margin:0;">SIGNAL A+</h2>
                    <p style="color:white; font-size:14px; margin-top:10px;">SL: Low 15M | TP: High 1H</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("RESET"):
                st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.info("HediaAyoub AI en attente de données...")
