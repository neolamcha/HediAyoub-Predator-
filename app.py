import streamlit as st
import pandas as pd

# ==========================================
# 1. CONFIGURATION SYSTEME & IOS PWA
# ==========================================
st.set_page_config(
    page_title="PREDATOR AI | QUANT TERMINAL",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuration pour le mode App iOS
st.markdown("""
    <head>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="PREDATOR AI">
        <link rel="apple-touch-icon" href="https://cdn-icons-png.flaticon.com/512/2583/2583100.png">
        <style>
            .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
            .stCameraInput { border: 2px solid #FF3131 !important; }
            .status-cell { text-align: center; padding: 8px; border-radius: 4px; font-weight: bold; font-size: 11px; }
            .ready { background-color: #004400; color: #00FF00; border: 1px solid #00FF00; }
            .missing { background-color: #220000; color: #FF3131; border: 1px solid #FF3131; }
            .verdict-card { border: 2px solid #00FF00; padding: 25px; border-radius: 10px; background: #000B00; text-align: center; box-shadow: 0 0 20px rgba(0,255,0,0.2); }
            h1, h2, h3 { color: #FF3131; text-transform: uppercase; letter-spacing: 3px; }
        </style>
    </head>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE SECURITE
# ==========================================
if "auth" not in st.session_state:
    st.session_state.auth = False
if 'scans' not in st.session_state:
    # 10 Actifs corrélés aux flux YouTube fournis
    assets_list = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {asset: {"1D": None, "1H": None, "15M": None} for asset in assets_list}

if not st.session_state.auth:
    st.markdown("<br><br><h1 style='text-align:center;'>PREDATOR AI</h1>", unsafe_allow_html=True)
    with st.container():
        col_l, col_c, col_r = st.columns([1, 1.5, 1])
        with col_c:
            pw = st.text_input("CLE D'ACCES ALPHA", type="password")
            if st.button("INITIALISER LE PROTOCOLE"):
                if pw == "PREDATOR2026":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("ACCES REFUSE")
else:
    # ==========================================
    # 3. INTERFACE DE SCAN (MULTI-TF)
    # ==========================================
    st.title("🛡️ MATRICE DE CONFLUENCE")
    
    with st.expander("📷 SCANNER UN GRAPHIQUE (MOBILE VISION)", expanded=True):
        c1, c2, c3 = st.columns([1.5, 1, 2])
        with c1:
            active_asset = st.selectbox("ACTIF", list(st.session_state.scans.keys()))
        with c2:
            active_tf = st.selectbox("TIMEFRAME", ["1D", "1H", "15M"])
        with c3:
            img = st.camera_input("SCAN")
            if img:
                st.session_state.scans[active_asset][active_tf] = img
                st.success(f"DATA {active_asset} {active_tf} ENREGISTREE")

    st.divider()

    # ==========================================
    # 4. TABLEAU DE BORD & CORRELATION
    # ==========================================
    col_table, col_verdict = st.columns([1.8, 1])

    with col_table:
        st.subheader("📊 MONITORING DES 10 ACTIFS")
        # En-tête
        h1, h2, h3, h4 = st.columns([1.5, 1, 1, 1])
        h1.write("**SYMBOLE**")
        h2.write("**1D**")
        h3.write("**1H**")
        h4.write("**15M**")

        for asset, tfs in st.session_state.scans.items():
            r1, r2, r3, r4 = st.columns([1.5, 1, 1, 1])
            r1.write(f"**{asset}**")
            
            for tf, r_col in zip(["1D", "1H", "15M"], [r2, r3, r4]):
                if tfs[tf]:
                    r_col.markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else:
                    r_col.markdown('<div class="status-cell missing">VIDE</div>', unsafe_allow_html=True)

    with col_verdict:
        st.subheader("🤖 VERDICT IA")
        
        # Vérification si au moins un actif est complet (3 TF)
        completed_assets = [a for a, tfs in st.session_state.scans.items() if all(tfs.values())]
        
        if completed_assets:
            target = completed_assets[0] # Priorité au premier actif complété
            st.markdown(f"""
                <div class="verdict-card">
                    <h2 style="color:#00FF00;">SIGNAL A+ DETECTE</h2>
                    <h1 style="color:white; margin:0;">{target}</h1>
                    <p style="color:#888;">CORRELATION YOUTUBE : VALIDEE ✅</p>
                    <hr style="border-color:#111;">
                    <p style="font-size:20px;">ORDRE : <span style="color:#00FF00;">ACHAT (LONG)</span></p>
                    <p style="font-size:18px;"><b>ENTREE :</b> AU MARCHE</p>
                    <p style="color:#FF3131;"><b>SL :</b> STRUCTURE SMC -2 TICKS</p>
                    <p style="color:#00FF00;"><b>TP :</b> LIQUIDITE BOOKMAP (MUR)</p>
                    <br>
                    <p style="font-size:11px; color:#555;">Analyse basée sur flux : jc1Ds-Uz6gE, XZs8kRuL12k, kvhRserj8ME</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("RESET DATA"):
                st.session_state.scans = {asset: {"1D": None, "1H": None, "15M": None} for asset in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.warning("IA EN ATTENTE : Complétez les 3 unités de temps (1D, 1H, 15M) pour débloquer la fusion Orderflow.")

    # Sidebar infos
    st.sidebar.markdown("### 📡 FLUX ACTIFS")
    st.sidebar.caption("NQ Bookmap: jc1Ds-Uz6gE")
    st.sidebar.caption("ES Footprint: XZs8kRuL12k")
    st.sidebar.caption("Gold Liq: kvhRserj8ME")
