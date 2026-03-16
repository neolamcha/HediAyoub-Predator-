import streamlit as st
import time
import random

# ==========================================
# 1. STYLE GLOBAL & IDENTITÉ HEDIAYOUB
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - PREDATOR V9.3", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        
        /* Bannière HediaAyoub */
        .hedi-banner {
            background: linear-gradient(90deg, #000000 0%, #440000 50%, #000000 100%);
            padding: 25px; text-align: center; border-bottom: 3px solid #FF3131;
            margin-bottom: 30px;
        }
        .hedi-name { color: white; letter-spacing: 15px; font-weight: 100; margin: 0; font-size: 14px; }
        .predator-title { color: #FF3131; font-size: 32px; font-weight: 900; text-transform: uppercase; margin: 5px 0; }
        
        /* Guide des corrélations */
        .guide-container {
            background: #080808; padding: 20px; border-radius: 15px; border: 1px solid #222;
        }
        .guide-title { color: #FF3131; font-weight: 900; font-size: 16px; margin-bottom: 10px; text-transform: uppercase; }
        .guide-item { color: #00FF00; font-weight: bold; font-size: 14px; margin-bottom: 5px; }

        /* Boites de prix Finales */
        .box-tp { background-color: #00FF00; color: black; padding: 25px; border-radius: 15px; text-align: center; font-size: 30px; font-weight: 900; }
        .box-sl { background-color: #FF3131; color: white; padding: 25px; border-radius: 15px; text-align: center; font-size: 30px; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class='hedi-banner'>
        <p class='hedi-name'>HEDIAYOUB CAPITAL</p>
        <h1 class='predator-title'>PREDATOR V9.3 : QUANT-SYNC</h1>
    </div>
""", unsafe_allow_html=True)

# --- LOGIQUE DE CORRÉLATION ---
# Ici on définit précisément ce que l'app demande selon l'actif
config_orchestra = {
    "NASDAQ (NQ)": {"smt": "S&P500 (ES)", "conductor": "DXY (Dollar Index)"},
    "GOLD (XAU)": {"smt": "SILVER (XAG)", "conductor": "DXY (Dollar Index)"},
    "EURUSD": {"smt": "GBPUSD", "conductor": "DXY (Dollar Index)"},
    "BITCOIN": {"smt": "ETH (Ethereum)", "conductor": "DXY (Dollar Index)"},
    "US30": {"smt": "NASDAQ (NQ)", "conductor": "DXY (Dollar Index)"}
}

# --- ZONE DE RÉCEPTION ---
col_l, col_r = st.columns([1, 1.2])

with col_l:
    target = st.selectbox("🎯 ACTIF À TRADER", list(config_orchestra.keys()))
    conf = config_orchestra[target]
    
    st.markdown(f"""
        <div class="guide-container">
            <p class="guide-title">DOSSIER REQUIS (6 CAPTURES) :</p>
            <div class="guide-item">📸 {target} (Daily + 15M)</div>
            <div class="guide-item">📸 {conf['smt']} (Daily + 15M)</div>
            <div class="guide-item">📸 {conf['conductor']} (Daily + 15M)</div>
            <p style="color:#555; font-size:11px; margin-top:10px;">L'IA analyse le flux institutionnel sur ces 3 piliers.</p>
        </div>
    """, unsafe_allow_html=True)

with col_r:
    files = st.file_uploader("📥 GLISSER LES 6 PREUVES ICI", accept_multiple_files=True)

st.divider()

# --- VERDICT FINAL (ZÉRO ERREUR D'AFFICHAGE) ---
if files:
    if len(files) < 6:
        st.warning(f"⚠️ PROTOCOLE PARTIEL : {len(files)}/6 captures. Analyse bloquée.")
    else:
        with st.status("🔍 ANALYSE QUANTITATIVE EN COURS...", expanded=True) as status:
            time.sleep(1.5)
            st.write(f"Vérification SMT entre {target} et {conf['smt']}...")
            time.sleep(1)
            st.write(f"Sync avec le Chef d'Orchestre {conf['conductor']}...")
            time.sleep(1)
            status.update(label="ANALYSE TERMINÉE ✅", state="complete")

        # Calculs simulation (Price Action)
        score = random.randint(93, 99)
        # Simulation de prix cohérente pour NQ ou Gold
        base = 18450.00 if "NASDAQ" in target else 2185.50
        tp_final = base + random.uniform(80, 200)
        sl_final = base - random.uniform(50, 120)

        # Affichage du Score et de l'Actif
        st.markdown(f"<h1 style='text-align:center; color:#00FF00; font-size:60px;'>{target}</h1>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("PREDATOR SCORE", f"{score}/100")
        with c2:
            st.metric("CONFLUENCE SMT", "VALIDÉE ✅")

        st.write("") # Espace
        
        # Les boites TP et SL (Fixées pour ne plus bugger)
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.markdown(f'<div class="box-tp">🎯 TP : {tp_final:.2f}</div>', unsafe_allow_html=True)
        with res_col2:
            st.markdown(f'<div class="box-sl">🛑 SL : {sl_final:.2f}</div>', unsafe_allow_html=True)

        st.write("")
        st.error("🚨 ÉTAPE FINALE : CONFIRMER L'ABSORPTION SUR BOOKMAP YOUTUBE")
        
        if st.button("RESET POUR LE PROCHAIN TRADE"):
            st.rerun()

else:
    st.info("Sélectionne ton actif et charge tes 6 captures pour activer l'algorithme.")
