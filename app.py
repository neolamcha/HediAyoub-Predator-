import streamlit as st
import yfinance as yf
import google.generativeai as genai
import time
import PIL.Image
import json

# --- CONFIGURATION API ---
# Clé intégrée selon ta demande
GENAI_API_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg" 
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURATION UI ---
st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

# CSS stable pour mobile et desktop
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .res-box { background: #0a0a0a; padding: 20px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 10px 0; }
        .stButton>button { background-color: #FF3131; color: white; border-radius: 10px; border: none; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

if 'trade_setup' not in st.session_state:
    st.session_state.trade_setup = None

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF3131; font-size:10px; margin-top:-15px; letter-spacing:3px;'>NEURAL PREDATOR V35.0</p>", unsafe_allow_html=True)

# --- PARAMÈTRES D'ACTIFS ---
assets = {
    "BITCOIN (BTC)": "BTC-USD",
    "NASDAQ (NQ)": "NQ=F",
    "US30 (DOW)": "YM=F",
    "GOLD (XAU)": "GC=F",
    "EURUSD": "EURUSD=X"
}

target_label = st.selectbox("CHOISIR L'ACTIF", list(assets.keys()), label_visibility="collapsed")
target_symbol = assets[target_label]

col_smt, col_tf = st.columns(2)
with col_smt:
    use_smt = st.toggle("CONFIRMATION SMT", value=True)
with col_tf:
    tf_choice = st.selectbox("TIMEFRAME", ["1D", "4H", "1H", "15M", "5M", "1M"], index=4)

# Zone d'upload pour tes 6 captures (SMC/Bookmap/CVD)
uploaded_files = st.file_uploader("CHARGE TES 6 DATASETS", accept_multiple_files=True)

# --- ENGINE DE VISION IA ---
def get_ai_analysis(files, asset_name):
    # Conversion des fichiers pour Gemini
    images = [PIL.Image.open(f) for f in files]
    
    prompt = f"""
    Analyse d'expert Institutionnel pour {asset_name}.
    Examine ces 6 graphiques (Volume Profile, CVD, SMC).
    1. Détecte la structure du marché (CHoCH, BOS).
    2. Analyse l'Order Flow (Absorption au CVD, Big Trades).
    3. Verdict : Direction (BUY ou SELL), Confiance (90-99%), et Raison technique courte.
    
    IMPORTANT : Réponds UNIQUEMENT avec ce format JSON strict :
    {{"side": "BUY", "confidence": 96, "reason": "Texte court ici"}}
    """
    
    try:
        response = model.generate_content([prompt, *images])
        # Nettoyage et parsing du JSON
        raw_text = response.text.strip().replace('```json', '').replace('```', '')
        return json.loads(raw_text)
    except Exception as e:
        return {"side": "ERROR", "confidence": 0, "reason": f"Erreur IA: {str(e)}"}

# --- EXÉCUTION DU SCAN ---
if uploaded_files and len(uploaded_files) >= 6:
    if st.button("🔥 SCANNER LA CONFLUENCE NEURALE", use_container_width=True):
        with st.status("📡 ANALYSE DES GRAPHES PAR GEMINI...", expanded=True) as status:
            # 1. Analyse Vision
            ai_verdict = get_ai_analysis(uploaded_files, target_label)
            
            if ai_verdict['side'] != "ERROR":
                # 2. Prix réel du marché
                ticker = yf.Ticker(target_symbol)
                price = ticker.history(period="1d")['Close'].iloc[-1]
                
                # 3. Calcul TP/SL Professionnel (Ratio 1:3)
                # On ajuste la volatilité selon l'actif
                mult = 0.0008 if "EURUSD" in target_symbol else 0.004
                side_val = 1 if ai_verdict['side'] == "BUY" else -1
                
                st.session_state.trade_setup = {
                    "side": ai_verdict['side'],
                    "conf": ai_verdict['confidence'],
                    "reason": ai_verdict['reason'],
                    "entry": price,
                    "tp": price + (price * mult * 3 * side_val),
                    "sl": price - (price * mult * side_val)
                }
                status.update(label="ANALYSE TERMINÉE ✅", state="complete")
            else:
                status.update(label="ERREUR D'ANALYSE ❌", state="error")
                st.error(ai_verdict['reason'])

# --- AFFICHAGE ÉLITE ---
if st.session_state.trade_setup:
    res = st.session_state.trade_setup
    color = "#00FF66" if res['side'] == "BUY" else "#FF3131"
    
    st.markdown(f"""
        <div class="res-box">
            <p style="text-align:center; color:#555; font-size:10px; font-weight:bold; letter-spacing:2px; margin:0;">SIGNAL GÉNÉRÉ</p>
            <h1 style="text-align:center; color:{color}; font-size:55px; margin:0;">{res['side']}</h1>
            <p style="text-align:center; opacity:0.8; font-size:13px;">Confiance : {res['conf']}% | <i>"{res['reason']}"</i></p>
        </div>
    """, unsafe_allow_html=True)
    
    st.metric("PRIX D'ENTRÉE LIVE", f"{res['entry']:.5f}" if "EUR" in target_symbol else f"{res['entry']:.2f}")
    
    c_tp, c_sl = st.columns(2)
    with c_tp:
        st.success(f"🎯 TAKE PROFIT\n\n{res['tp']:.5f}" if "EUR" in target_symbol else f"🎯 TP\n\n{res['tp']:.2f}")
    with c_sl:
        st.error(f"📍 STOP LOSS\n\n{res['sl']:.5f}" if "EUR" in target_symbol else f"📍 SL\n\n{res['sl']:.2f}")

    if st.button("🔄 NOUVELLE ANALYSE"):
        st.session_state.trade_setup = None
        st.rerun()

st.markdown("<br><div style='text-align:center; opacity:0.1;'>🌍 | 🧭 | 👑</div>", unsafe_allow_html=True)
