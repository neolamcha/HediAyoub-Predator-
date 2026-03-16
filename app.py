import streamlit as st

# CONFIGURATION DU TERMINAL PREDATOR
st.set_page_config(page_title="PREDATOR AI | ORGANIZED SCANNER", layout="wide")

# STYLE NOIR MAT & GRILLES DE TRI
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Courier New', monospace; }
    .asset-row { border-bottom: 1px solid #222; padding: 10px 0; }
    .status-cell { text-align: center; padding: 5px; border-radius: 5px; font-size: 12px; }
    .ready { background-color: #004400; color: #00ff00; border: 1px solid #00ff00; }
    .missing { background-color: #220000; color: #ff3131; border: 1px solid #ff3131; }
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ PREDATOR AI ACCESS")
    if st.text_input("ALPHA KEY", type="password") == "PREDATOR2026": 
        st.session_state.auth = True
        st.rerun()
else:
    st.title("🤖 MATRICE DE SCAN QUANTITATIF")
    st.write("Fournissez les 3 Timeframes pour les 10 actifs. L'IA fusionnera ces données avec l'Orderflow YouTube.")

    # 1. LISTE DES 10 ACTIFS SÉLECTIONNÉS
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    timeframes = ["1D (Macro)", "1H (Structure)", "15M (Exécution)"]

    # Initialisation de la mémoire du scan
    if 'scans' not in st.session_state:
        st.session_state.scans = {asset: {tf: None for tf in timeframes} for asset in assets}

    # --- SECTION INPUT (L'APPAREIL PHOTO) ---
    with st.expander("📸 OUVRIR LE SCANNER DE GRAPHIQUES", expanded=True):
        col_a, col_t, col_c = st.columns([1, 1, 2])
        with col_a:
            selected_asset = st.selectbox("Actif à photographier :", assets)
        with col_t:
            selected_tf = st.selectbox("Timeframe :", timeframes)
        with col_c:
            img = st.camera_input("Scanner le graphique")
            if img:
                st.session_state.scans[selected_asset][selected_tf] = img
                st.success(f"Image enregistrée pour {selected_asset} en {selected_tf}")

    st.divider()

    # --- SECTION ORGANISATION (LE TABLEAU DE BORD) ---
    st.subheader("📊 ÉTAT DE LA MATRICE DE CONFLUENCE")
    
    # En-tête du tableau
    h_col1, h_col2, h_col3, h_col4, h_col5 = st.columns([1.5, 1, 1, 1, 1.5])
    h_col1.write("**ACTIF**")
    h_col2.write("**1D MACRO**")
    h_col3.write("**1H STRUCT**")
    h_col4.write("**15M EXEC**")
    h_col5.write("**VERDICT IA**")

    for asset in assets:
        c1, c2, c3, c4, c5 = st.columns([1.5, 1, 1, 1, 1.5])
        c1.write(f"**{asset}**")
        
        # Affichage des statuts pour chaque TF
        for i, (tf, col) in enumerate(zip(timeframes, [c2, c3, c4])):
            if st.session_state.scans[asset][tf]:
                col.markdown('<div class="status-cell ready">COMPLET</div>', unsafe_allow_html=True)
            else:
                col.markdown('<div class="status-cell missing">VIDE</div>', unsafe_allow_html=True)

        # Calcul du verdict pour cet actif
        is_ready = all(st.session_state.scans[asset][tf] for tf in timeframes)
        if is_ready:
            c5.button(f"VOIR SIGNAL {asset}", key=f"btn_{asset}", type="primary")
        else:
            c5.write("⏳ En attente de données...")

    # --- SECTION RÉSULTAT FINAL ---
    st.divider()
    st.sidebar.markdown("### 📡 FLUX YOUTUBE LIVE")
    st.sidebar.write("L'IA analyse les flux en arrière-plan dès qu'un actif est 'COMPLET'.")
    st.sidebar.caption("NQ: jc1Ds-Uz6gE | ES: XZs8kRuL12k")
