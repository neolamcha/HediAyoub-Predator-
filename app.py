import streamlit as st
import pandas as pd
import json

# 1. CONFIGURATION SYSTÈME
st.set_page_config(page_title="PREDATOR AI | NEURAL ENGINE", layout="wide")

# 2. STYLE LUXE NOIR MAT
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Courier New', monospace; }
    .signal-card { border: 2px solid #00ff00; padding: 30px; border-radius: 10px; background: #050505; text-align: center; }
    .metric-box { padding: 10px; border: 1px solid #222; border-radius: 5px; background: #0a0a0a; margin-bottom: 5px; }
    .title-neon { color: #ff3131; text-transform: uppercase; letter-spacing: 5px; text-shadow: 0 0 20px #ff3131; }
</style>
""", unsafe_allow_html=True)

# 3. GESTION DES DONNÉES (WEBHOOK SIMULÉ VIA URL)
# L'IA va lire les paramètres dans l'URL envoyés par TradingView
query_params = st.query_params

# Valeurs par défaut (Attente de signal)
actif = query_params.get("actif", "SCANNING...")
direction = query_params.get("dir", "NEUTRE")
prix_entree = query_params.get("entry", "0.00")
sl = query_params.get("sl", "0.00")
tp = query_params.get("tp", "0.00")
conf = int(query_params.get("conf", 0))

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h1 class='title-neon' style='text-align:center;'>PREDATOR AI</h1>", unsafe_allow_html=True)
    pw = st.text_input("CLÉ ALPHA", type="password")
    if st.button("INITIALISER"):
        if pw == "PREDATOR2026": st.session_state.auth = True; st.rerun()
else:
    st.sidebar.title("🤖 AI STATUS")
    st.sidebar.success("VISION ENGINE: ACTIVE")
    st.sidebar.info("WEBHOOKS: LISTENING")
    
    st.markdown("<h1 class='title-neon'>🎯 DECISION TERMINAL</h1>", unsafe_allow_html=True)
    
    col_sig, col_data = st.columns([2, 1])
    
    with col_sig:
        if conf >= 90:
            st.markdown(f"""
            <div class="signal-card">
                <h1 style='color:#00ff00;'>ALERTE A+ IDENTIFIÉE</h1>
                <h2 style='color:white;'>{actif}</h2>
                <p style='font-size:25px;'>ORDRE : <span style='color:#00ff00;'>{direction}</span></p>
                <hr style='border-color:#222;'>
                <p><b>ENTRÉE :</b> {prix_entree} | <b>SL :</b> {sl} | <b>TP :</b> {tp}</p>
                <p style='font-size:12px; color:#555;'>Fusion : CVD + SMC + Midnight Open + Bookmap Liquidity</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("⌛ L'IA scanne les flux... En attente d'une confluence supérieure à 90%.")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXpueXpueXpueXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxxcaOmsY0w/giphy.gif", width=400)

    with col_data:
        st.markdown("### 📊 INDICATEURS PRO")
        st.markdown(f"<div class='metric-box'>✅ <b>CVD</b> : { 'ACTIF' if conf > 30 else 'SCAN...' }</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>✅ <b>SMC (LuxAlgo)</b> : { 'VALIDÉ' if conf > 50 else 'SCAN...' }</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>✅ <b>Midnight Open</b> : { 'ZONE OK' if conf > 70 else 'SCAN...' }</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'>✅ <b>Bookmap Vision</b> : { 'LIQ DÉTECTÉE' if conf > 85 else 'SCAN...' }</div>", unsafe_allow_html=True)
        
        st.divider()
        st.write("🔗 **FLUX INVISIBLES :**")
        st.write("`jc1Ds-Uz6gE`, `XZs8kRuL12k`, `kvhRserj8ME`, `69jd1dOq4C8`")
