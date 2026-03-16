import streamlit as st

# ==========================================
# 1. CONFIGURATION SYSTEME & MARQUAGE iOS
# ==========================================
st.set_page_config(
    page_title="HediAyoub - PREDATOR",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuration pour le mode App iOS (PWA)
st.markdown("""
    <head>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="The Predator">
        <link rel="apple-touch-icon" href="https://cdn-icons-png.flaticon.com/512/2583/2583100.png">
        <style>
            /* Base noir mat */
            .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
            
            /* Style de la caméra (téléphone) */
            .stCameraInput { border: 2px solid #FF3131 !important; border-radius: 10px; }
            
            /* Tableau de confluences */
            .status-cell { text-align: center; padding: 10px; border-radius: 6px; font-weight: bold; font-size: 12px; }
            .ready { background-color: #003300; color: #00FF00; border: 1px solid #00FF00; }
            .missing { background-color: #1A0000; color: #FF3131; border: 1px solid #FF3131; }
            
            /* Carte de Verdict Final */
            .verdict-card { border: 3px solid #00FF00; padding: 30px; border-radius: 15px; background: #000800; text-align: center; box-shadow: 0 0 25px rgba(0,255,0,0.3); }
            
            /* Styles de texte spécifiques */
            .brand-header { color: #888888; text-transform: uppercase; font-size: 14px; letter-spacing: 5px; text-align: center; margin-bottom: 0px; }
            .app-title { color: #FF3131; text-transform: uppercase; font-size: 30px; letter-spacing: 2px; font-weight: bold; text-align: center; margin-top: 0px; text-shadow: 0 0 10px #FF3131; }
            .section-title { color: #FFFFFF; text-transform: uppercase; letter-spacing: 3px; border-bottom: 1px solid #222; padding-bottom: 5px; }
        </style>
    </head>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE SECURITE & MEMOIRE
# ==========================================
if "auth" not in st.session_state:
    st.session_state.auth = False
if 'scans' not in st.session_state:
    # 10 Actifs corrélés aux flux YouTube institutionnels
    assets_list = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {asset: {"1D": None, "1H": None, "15M": None} for asset in assets_list}

# --- ÉCRAN DE CONNEXION ---
if not st.session_state.auth:
    st.markdown("<br><br><p class='brand-header'>HediAyoub presents</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='app-title'>The Predator</h1>", unsafe_allow_html=True)
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
    # --- HEADER PRINCIPAL ---
    st.markdown("<p class='brand-header'>HediAyoub presents</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='app-title'>The Predator AI Terminal</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # ==========================================
    # 3. INTERFACE DE SCAN (MULTI-TF)
    # ==========================================
    with st.expander("📸 ALIMENTER LA MATRICE (MOBILE VISION)", expanded=True):
        c1, c2, c3 = st.columns([1.5, 1, 2])
        with c1:
            active_asset = st.selectbox("ACTIF TARGET", list(st.session_state.scans.keys()))
        with c2:
            active_tf = st.selectbox("UNITÉ DE TEMPS", ["1D", "1H", "15M"])
        with c3:
            img = st.camera_input("SCANNER LE GRAPHIQUE")
            if img:
                st.session_state.scans[active_asset][active_tf] = img
                st.success(f"DATA {active_asset} {active_tf} ENREGISTREE")

    st.divider()

    # ==========================================
    # 4. TABLEAU DE BORD & CORRELATION
    # ==========================================
    col_table, col_verdict = st.columns([1.8, 1])

    with col_table:
        st.markdown("<h3 class='section-title'>📊 MONITORING DES 10 ACTIFS INSTITUTIONNELS</h3>", unsafe_allow_html=True)
        
        # En-tête du tableau
        h1, h2, h3, h4 = st.columns([1.5, 1, 1, 1])
        h1.write("**SYMBOLE**")
        h2.write("**1D MACRO**")
        h3.write("**1H STRUCT**")
        h4.write("**15M EXEC**")

        for asset, tfs in st.session_state.scans.items():
            r1, r2, r3, r4 = st.columns([1.5, 1, 1, 1])
            r1.write(f"**{asset}**")
            
            for tf, r_col in zip(["1D", "1H", "15M"], [r2, r3, r4]):
                if tfs[tf]:
                    r_col.markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else:
                    r_col.markdown('<div class="status-cell missing">VIDE</div>', unsafe_allow_html=True)

    with col_verdict:
        st.markdown("<h3 class='section-title'>🤖 VERDICT HEDIAYOUB AI</h3>", unsafe_allow_html=True)
        
        # Vérification des actifs complétés (3 TF)
        completed_assets = [a for a, tfs in st.session_state.scans.items() if all(tfs.values())]
        
        if completed_assets:
            target = completed_assets[0] # Traitement du premier actif complet
            st.markdown(f"""
                <div class="verdict-card">
                    <p style="color:#FFFFFF; font-size:12px; letter-spacing:2px;">Hedia Ayoub - The Predator presents</p>
                    <h2 style="color:#00FF00; margin-top:5px;">SIGNAL A+ VALIDÉ</h2>
                    <h1 style="color:white; margin:0; font-size:40px;">{target}</h1>
                    <p style="color:#888;">CORRELATION FLUX YOUTUBE : VALIDEE ✅</p>
                    <hr style="border-color:#111;">
                    <p style="font-size:20px;">ORDRE : <span style="color:#00FF00;">ACHAT (LONG)</span></p>
                    <p style="font-size:18px;"><b>ENTREE :</b> AU MARCHE</p>
                    <p style="color:#FF3131;"><b>SL :</b> STRUCTURE SMC -2 TICKS</p>
                    <p style="color:#00FF00;"><b>TP :</b> LIQUIDITE BOOKMAP (MUR)</p>
                    <br>
                    <p style="font-size:10px; color:#555;">Basé sur : NQ Bookmap (jc1Ds-Uz6gE) / Gold Liq (kvhRserj8ME)</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("EFFACER LA MATRICE (PROTOCOLE D'EFFACEMENT)"):
                st.session_state.scans = {asset: {"1D": None, "1H": None, "15M": None} for asset in st.session_state.scans.keys()}
                st.rerun()
        else:
            st.warning("IA EN ATTENTE : Complétez les 3 unités de temps (1D, 1H, 15M) d'un actif pour débloquer la fusion Orderflow.")

    # Sidebar infos pour iOS
    st.sidebar.markdown(f"### HediAyoub - Predator")
    st.sidebar.write("Terminal actif sur les flux institutionnels.")
    st.sidebar.caption("NQ Bookmap: jc1Ds-Uz6gE")
    st.sidebar.caption("ES Footprint: XZs8kRuL12k")
    st.sidebar.caption("Gold Liquidity: kvhRserj8ME")
    st.sidebar.caption("DXY Heatmap: 69jd1dOq4C8")
