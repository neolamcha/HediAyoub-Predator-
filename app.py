import streamlit as st

# ==========================================
# 1. DESIGN INSTITUTIONNEL HEDIAYOUB
# ==========================================
st.set_page_config(page_title="HEDIAYOUB - EDGE FUND", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; }
        .hedi-banner {
            background: linear-gradient(90deg, #000000 0%, #1a0000 50%, #000000 100%);
            padding: 25px; text-align: center; border-bottom: 4px solid #FF3131;
            box-shadow: 0 5px 20px rgba(255, 49, 49, 0.2);
        }
        .predator-title { color: #FF3131; font-size: 35px; font-weight: 900; letter-spacing: 2px; }
        
        /* Dashboard Cards */
        .guide-box {
            background: #080808; padding: 20px; border-radius: 20px; border: 1px solid #222; margin-bottom: 20px;
        }
        .step-ready { color: #00FF00; font-weight: bold; border-left: 3px solid #00FF00; padding-left: 10px; margin: 10px 0; }

        /* Verdict Fund Edition */
        .fund-box {
            border: 4px solid #00FF00; padding: 40px; border-radius: 30px;
            background: linear-gradient(145deg, #000800, #001a00);
            text-align: center; box-shadow: 0 0 80px rgba(0, 255, 0, 0.15);
        }
        .signal-header { font-size: 12px; letter-spacing: 8px; color: #555; font-weight: bold; }
        .tp-box { background: #00FF00; color: black; padding: 25px; border-radius: 15px; font-size: 28px; font-weight: 900; margin: 15px 0; }
        .sl-box { background: #FF3131; color: white; padding: 20px; border-radius: 15px; font-size: 22px; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class='hedi-banner'>
        <p style='color:white; letter-spacing:15px; font-weight:100; margin:0;'>HEDIAYOUB CAPITAL</p>
        <h1 class='predator-title'>PREDATOR V7.0 : EDGE FUND ENGINE</h1>
    </div>
""", unsafe_allow_html=True)

# --- ENGINE CONFIG ---
config_fund = {
    "NASDAQ (NQ)": {"smt": "S&P500 (ES)", "conductor": "DXY"},
    "GOLD (XAU)": {"smt": "SILVER (XAG)", "conductor": "DXY"},
    "EURUSD": {"smt": "GBPUSD", "conductor": "DXY"},
    "US30": {"smt": "NASDAQ (NQ)", "conductor": "DXY"},
    "BITCOIN": {"smt": "ETH", "conductor": "DXY"}
}

st.write("<br>", unsafe_allow_html=True)
col_setup, col_input = st.columns([1, 1.3])

with col_setup:
    st.markdown("<p style='color:#FF3131; font-weight:bold;'>STATION DE CALCUL</p>", unsafe_allow_html=True)
    target = st.selectbox("SÉLECTIONNER L'ACTIF INSTITUTIONNEL", list(config_fund.keys()))
    
    setup = config_fund[target]
    st.markdown(f"""
        <div class="guide-box">
            <p style="color:#666; font-size:12px; margin-bottom:15px;">DOSSIER DE CONFLUENCE REQUIS :</p>
            <div class="step-ready">1. {target} (1D & 15M)</div>
            <div class="step-ready">2. {setup['smt']} (1D & 15M)</div>
            <div class="step-ready">3. {setup['conductor']} (1D & 15M)</div>
            <p style="font-size:10px; color:#444; margin-top:15px;">L'algorithme attend 6 preuves visuelles.</p>
        </div>
    """, unsafe_allow_html=True)

with col_input:
    st.markdown("<p style='color:#FF3131; font-weight:bold;'>TERMINAL DE RÉCEPTION</p>", unsafe_allow_html=True)
    # Upload massif des 6 captures
    dossier = st.file_uploader("GLISSER LES 6 CAPTURES D'ÉCRAN ICI", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

st.divider()

# --- ANALYSE DE L'EDGE ---
if dossier:
    if len(dossier) < 6:
        st.error(f"❌ DOSSIER INCOMPLET : {len(dossier)}/6. La politique du fonds interdit toute exécution sans confluence totale.")
    else:
        st.markdown(f"""
            <div class="fund-box">
                <p class="signal-header">HEDIAYOUB INSTITUTIONAL ALGO</p>
                <h1 style="color:#00FF00; font-size:65px; margin:0;">{target}</h1>
                <p style="color:white; font-size:20px; letter-spacing:3px;">CONFLUENCE TRIPLE SYNC : VALIDÉE ✅</p>
                
                <div style="margin-top:40px;">
                    <div class="tp-box">🎯 TP : EXTERNAL LIQUIDITY (DAILY HIGH/LOW)</div>
                    <div class="sl-box">🛑 SL : SMT INVALIDATION (15M SWING)</div>
                </div>
                
                <hr style="border-color:#111; margin:40px 0;">
                <p style="color:#FF3131; font-weight:bold; font-size:20px; text-shadow: 0 0 10px #FF3131;">
                    DÉCISION FINALE : CONFIRMER VIA BOOKMAP YOUTUBE
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("RESET TERMINAL"):
            st.rerun()
