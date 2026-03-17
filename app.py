import streamlit as st
import yfinance as yf
import google.generativeai as genai
import PIL.Image
import json
import re

# --- CONFIGURATION API ---
GENAI_API_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg" 
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURATION UI HAUT DE GAMME ---
st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; color: white; }
        .sub-title { text-align: center; color: #FF3131; font-size: 10px; margin-top: -15px; letter-spacing: 3px; font-weight: bold;}
        .res-box { background: #0a0a0a; padding: 20px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 10px 0; }
        .stButton>button { background-color: #FF3131; color: white; border-radius: 10px; border: none; font-weight: bold; }
        
        /* 🔥 ESTHÉTIQUE DU BOUTON TACTIQUE 🔥 */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #1f1f1f 0%, #a80000 100%);
            border: 2px solid #ff0000;
            color: white;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 5px;
            box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
            transition: all 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            background: linear-gradient(135deg, #a80000 0%, #ff0000 100%);
            box-shadow: 0 4px 25px rgba(255, 0, 0, 0.8);
            transform: translateY(-2px);
        }
    </style>
""", unsafe_allow_html=True)

if 'trade_setup' not in st.session_state:
    st.session_state.trade_setup = None

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>NEURAL PREDATOR V40.0</div>", unsafe_allow_html=True)

# Actifs consolidés
assets = {
    "BITCOIN (BTC)": "BTC-USD",
    "NASDAQ (NQ)": "NQ=F",
    "US30 (DOW)": "YM=F",
    "GOLD (XAU)": "GC=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X"
}

target_label = st.selectbox("CHOISIR L'ACTIF", list(assets.keys()), label_visibility="collapsed")
target_symbol = assets[target_label]

# Zone d'upload pro
uploaded_files = st.file_uploader("CHARGE TES 6 DATASETS", accept_multiple_files=True)

# --- ENGINE DE VISION HYBRIDE (BLINDÉ) ---
def get_safe_ai_analysis(files, asset_name, current_price):
    images = [PIL.Image.open(f) for f in files]
    is_fx = "USD=X" in target_symbol
    format_p = ".5f" if is_fx else ".2f"
    
    prompt = f"""
    En tant qu'expert SMC/OrderFlow, analyse ces graphiques pour {asset_name}. 
    PRIX ACTUEL MARCHE : {current_price:{format_p}}
    1. Identifie la direction (BUY/SELL).
    2. Trouve le Stop Loss logique (Swing High/Low).
    3. Trouve le Take Profit (Zone de liquidité opposée).
    4. Décris la confluence (ex: CHoCH + CVD Absorption).
    
    IMPORTANT : Réponds uniquement dans ce format JSON strict :
    {{"side": "BUY", "confidence": 96, "sl": {current_price:{format_p}}, "tp": {current_price:{format_p}}, "reason": "Détail court ici"}}
    """
    
    try:
        response = model.generate_content([prompt, *images])
        # Nettoyage JSON agressif pour éviter l'échec de l'analyse
        raw_text = response.text.strip().replace('```json', '').replace('```', '')
        # Supprime tout ce qui n'est pas le JSON (texte d'explication de l'IA)
        json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return None
    except Exception as e:
        return {"side": "ERROR", "confidence": 0, "reason": str(e), "sl": 0, "tp": 0}

# --- EXÉCUTION DU SCAN ---
if uploaded_files and len(uploaded_files) >= 1:
    # Le bouton à l'esthétique tactique
    if st.button("EXECUTE NEURAL SCAN", use_container_width=True):
        with st.status("📡 ACQUISITION DES DONNÉES DE MARCHÉ...", expanded=True) as status:
            ticker = yf.Ticker(target_symbol)
            hist = ticker.history(period="1d")
            price = hist['Close'].iloc[-1]
            status.write(f"✅ Prix réel : `{price:.2f}`")
            
            # 2. Analyse Gemini avec prix de référence
            res = get_safe_ai_analysis(uploaded_files, target_label, price)
            
            if res and res['side'] != "ERROR":
                # 3. Sécurité (Failsafe) : Calcul mathématique si l'IA donne 0
                is_fx = "USD=X" in target_symbol
                safe_dist = price * 0.005 if not is_fx else 0.0020 # 0.5% Indices ou 20 pips FX
                
                # Utilise le SL de l'IA s'il est réaliste, sinon calcule le mathématiquement
                final_sl = res['sl'] if (res['sl'] != 0 and abs(price - res['sl']) < price * 0.1) else (price - safe_dist if res['side'] == "BUY" else price + safe_dist)
                # Utilise le TP de l'IA, sinon calcule un RR de 1:3
                final_tp = res['tp'] if (res['tp'] != 0 and abs(price - res['tp']) < price * 0.1) else (price + (safe_dist * 3) if res['side'] == "BUY" else price - (safe_dist * 3))

                st.session_state.trade_setup = {
                    "side": res['side'],
                    "conf": res['confidence'],
                    "entry": price,
                    "tp": final_tp,
                    "sl": final_sl,
                    "reason": res['reason']
                }
                status.update(label="SIGNAL GÉNÉRÉ ✅", state="complete")
            else:
                status.update(label="ÉCHEC DE L'ANALYSE NEURALE ❌", state="error")
                st.error(res['reason'] if res else "Erreur critique de parsing JSON.")

# --- AFFICHAGE ÉLITE ---
if st.session_state.trade_setup:
    t = st.session_state.trade_setup
    st.divider()
    
    st.markdown(f"""
        <div class="res-box">
            <h1 style="text-align:center; color:{'#00FF66' if t['side'] == 'BUY' else '#FF3131'}; font-size:60px; margin:0;">{t['side']}</h1>
            <p style="text-align:center; opacity:0.6; font-size:12px;">Confiance : {t['conf']}% | "{t['reason']}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    is_fx = "USD=X" in target_symbol
    fmt = ".5f" if is_fx else ".2f"
    
    st.metric("PRIX D'ENTRÉE (MARCHÉ)", f"{t['entry']:{fmt}}")
    c1, c2 = st.columns(2)
    c1.success(f"🎯 TARGET (TP)\n\n{t['tp']:{fmt}}")
    c2.error(f"📍 PROTECTION (SL)\n\n{t['sl']:{fmt}}")
    
    if st.button("🔄 NOUVELLE ANALYSE"):
        st.session_state.trade_setup = None
        st.rerun()

st.markdown("<br><div style='text-align:center; opacity:0.1;'>🌍 | 🧭 | 👑</div>", unsafe_allow_html=True)
