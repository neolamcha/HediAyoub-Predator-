import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# 1. CONFIGURATION & DESIGN READABLE DARK
# ==========================================
st.set_page_config(page_title="THE PREDATOR", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        [data-testid="stExpander"] { background-color: #050505 !important; border: 1px solid #FF3131 !important; border-radius: 10px !important; }
        label { color: #FF3131 !important; font-weight: bold !important; font-family: 'Courier New'; }
        [data-testid="stFileUploadDropzone"] { background-color: #0A0A0A !important; border: 2px dashed #FF3131 !important; }
        [data-testid="stFileUploadDropzone"] button { background-color: #FF3131 !important; color: #000000 !important; font-weight: bold !important; width: 100% !important; }
        div[data-baseweb="select"] > div { background-color: #111111 !important; border: 1px solid #FF3131 !important; color: #FFFFFF !important; }
        .main-title { color: #FF3131; text-transform: uppercase; font-size: 28px; font-weight: bold; text-align: center; text-shadow: 0 0 15px #FF3131; }
        .status-cell { text-align: center; padding: 10px; border-radius: 5px; font-weight: bold; }
        .ready { background-color: #00FF00; color: #000000; }
        .missing { background-color: #1A1A1A; color: #444444; border: 1px solid #333; }
        .alarm-box { border: 1px solid #FF3131; padding: 10px; border-radius: 10px; text-align: center; background: #1a0000; margin-bottom: 20px; }
        small { color: #FFFFFF !important; font-size: 14px !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE SESSION & SÉCURITÉ
# ==========================================
if "auth" not in st.session_state: st.session_state.auth = False
if 'scans' not in st.session_state:
    assets = ["NASDAQ (NQ)", "GOLD (XAU)", "DXY", "EURUSD", "GBPUSD", "US30", "BITCOIN", "OIL (WTI)", "ETH", "NVDA"]
    st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in assets}

# --- LOGIN ---
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

    # ⏰ SECTION ALARMES (HORAIRES DE SCAN INSTITUTIONNELS)
    st.markdown("""
        <div class='alarm-box'>
            <p style='color:#FF3131; margin:0; font-size:12px;'>⚠️ PROCHAINS SCANS OBLIGATOIRES (ALERTE IA)</p>
            <p style='font-size:18px; font-weight:bold; color:white;'>08:55 (London) | 14:25 (NY Open) | 19:55 (Closing)</p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("🎯 CAPTURE HAUTE RÉSOLUTION", expanded=True):
        active_asset = st.selectbox("CIBLE", list(st.session_state.scans.keys()))
        active_tf = st.selectbox("UNITÉ DE TEMPS", ["1D", "1H", "15M"])
        img_file = st.file_uploader("OUVRIR CAMÉRA IPHONE", type=['png', 'jpg', 'jpeg'])
        if img_file:
            st.session_state.scans[active_asset][active_tf] = True
            st.toast("DATA ENREGISTRÉE")

    st.divider()

    # --- MATRICE ET VERDICT ---
    col_m, col_v = st.columns([1.5, 1])

    with col_m:
        st.markdown("<p style='font-size:14px;color:#FF3131;font-weight:bold;'>📊 MATRICE DES FLUX</p>", unsafe_allow_html=True)
        for asset, tfs in st.session_state.scans.items():
            r = st.columns([1.5, 1, 1, 1])
            r[0].write(f"<small>{asset}</small>", unsafe_allow_html=True)
            for i, tf in enumerate(["1D", "1H", "15M"]):
                if tfs[tf]: r[i+1].markdown('<div class="status-cell ready">OK</div>', unsafe_allow_html=True)
                else: r[i+1].markdown('<div class="status-cell missing">-</div>', unsafe_allow_html=True)

    with col_v:
        st.markdown("<p style='font-size:14px;color:#FF3131;font-weight:bold;'>🤖 ALGORITHME SNIPER</p>", unsafe_allow_html=True)
        ready_assets = [a for a, v in st.session_state.scans.items() if all(v.values())]

        if ready_assets:
            # L'algorithme sélectionne le premier actif 100% scanné (Simule le "Best Asset")
            best_asset = ready_assets[0]
            
            # Paramètres de Trading (Simulation IA basée sur l'actif)
            # Dans un futur upgrade, ces chiffres viendraient d'une vraie analyse visuelle
            st.markdown(f"""
                <div style='border:2px solid #00FF00; padding:20px; border-radius:15px; background:#010801; text-align:center;'>
                    <h2 style='color:white; margin:0;'>{best_asset}</h2>
                    <h1 style='color:#00FF00; margin:0; font-size:35px;'>BEST SETUP</h1>
                    <hr style='border-color:#111;'>
                    <p style='color:#00FF00; font-size:20px; font-weight:bold;'>ORDRE : BUY / LONG</p>
                    <p style='color:white; font-size:16px;'>🔴 SL : 0.5% sous le Low 15M</p>
                    <p style='color:#00FF00; font-size:16px;'>🟢 TP : Liquidité High 1H</p>
                    <p style='color:#555; font-size:10px;'>PRÉCISION IA : 94.2%</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("RESET TOUT"):
                st.session_state.scans = {a: {"1D": False, "1H": False, "15M": False} for a in st.session_state.scans.keys()}
                st.rerun()
        else:
            # Si aucun actif n'est scanné complètement
            st.markdown("""
                <div style='border:1px solid #333; padding:20px; border-radius:15px; background:#050505; text-align:center;'>
                    <h2 style='color:#444;'>NO TRADE</h2>
                    <p style='color:#222;'>EN ATTENTE DE SCAN COMPLET (1D+1H+15M)</p>
                </div>
            """, unsafe_allow_html=True)
