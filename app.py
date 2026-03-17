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

st.set_page_config(page_title="HEDI AYOUB", layout="centered")

# CSS Elite & Mobile Responsive
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .res-box { background: #0a0a0a; padding: 20px; border-radius: 15px; border: 1px solid #1f1f1f; }
        .logic-badge { background: #1a1a1a; color: #FF3131; padding: 4px 10px; border-radius: 5px; font-size: 10px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

if 'trade_setup' not in st.session_state:
    st.session_state.trade_setup = None

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF3131; font-size:10px; margin-top:-15px;'>IRONCLAD ENGINE V38.0</p>", unsafe_allow_html=True)

assets = {
    "BITCOIN (BTC)": "BTC-USD",
    "NASDAQ (NQ)": "NQ=F",
    "US30 (DOW)": "YM=F",
    "GOLD (XAU)": "GC=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X"
}

target_label = st.selectbox("ACTIF", list(assets.keys()), label_visibility="collapsed")
target_symbol = assets[target_label]

# SÉCURITÉ 1 : Limitation stricte des extensions de fichiers
uploaded_files = st.file_uploader("UPLOAD DATASETS", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

def get_live_liquidity_analysis(files, asset_name):
    images = [PIL.Image.open(f) for f in files]
    prompt = f"""
    Analyse de liquidité vivante pour {asset_name}. 
    1. Trouve le prix exact pour le Stop Loss (derrière le Swing High/Low).
    2. Trouve le prix exact pour le Take Profit (zone de liquidité opposée).
    3. Identifie la direction (BUY/SELL).
    Réponds UNIQUEMENT au format JSON:
    {{"side": "BUY", "confidence": 95, "sl_level": 1.08450, "tp_level": 1.09200, "logic": "Raison courte"}}
    """
    try:
        response = model.generate_content([prompt, *images])
        # SÉCURITÉ 2 : Extraction Regex robuste pour ignorer le texte hors du JSON
        match = re.search(r'\{.*\}', response.text.replace('\n', ''), re.DOTALL)
        if match:
            return json.loads(match.group(0))
        return None
    except Exception as e:
        return None

if uploaded_files and len(uploaded_files) >= 1:
    if st.button("🔥 EXECUTER L'ALGORITHME", use_container_width=True):
        with st.status("🧠 L'IA CALCULE LES ZONES DE SORTIE...") as s:
            verdict = get_live_liquidity_analysis(uploaded_files, target_label)
            
            if verdict:
                # SÉCURITÉ 3 : Protection contre le crash yfinance
                try:
                    ticker = yf.Ticker(target_symbol)
                    current_p = ticker.history(period="1d")['Close'].iloc[-1]
                except:
                    st.error("Flux de prix temporairement indisponible. Réessaie.")
                    st.stop()
                
                # SÉCURITÉ 4 : Vérification mathématique (Sanity Check)
                is_valid_buy = verdict['side'] == "BUY" and verdict['tp_level'] > current_p > verdict['sl_level']
                is_valid_sell = verdict['side'] == "SELL" and verdict['tp_level'] < current_p < verdict['sl_level']
                
                if not (is_valid_buy or is_valid_sell):
                    s.update(label="ERREUR DE COHÉRENCE IA ⚠️", state="error")
                    st.warning("L'IA a généré des niveaux mathématiquement incohérents avec le prix actuel. Relance le scan.")
                    st.stop()
                
                st.session_state.trade_setup = {
                    "side": verdict['side'], "conf": verdict['confidence'],
                    "entry": current_p, "tp": verdict['tp_level'],
                    "sl": verdict['sl_level'], "logic": verdict['logic']
                }
                s.update(label="SETUP VALIDÉ ✅", state="complete")
            else:
                s.update(label="ÉCHEC DE L'ANALYSE ❌", state="error")
                st.error("L'IA n'a pas pu formater sa réponse. Essaie avec des captures plus claires.")

if st.session_state.trade_setup:
    res = st.session_state.trade_setup
    color = "#00FF66" if res['side'] == "BUY" else "#FF3131"
    
    st.markdown(f"""
        <div class="res-box">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span class="logic-badge">LIVE LOGIC</span>
                <span style="font-size:12px; opacity:0.5;">Confiance: {res['conf']}%</span>
            </div>
            <h1 style="text-align:center; color:{color}; font-size:60px; margin:10px 0;">{res['side']}</h1>
            <p style="text-align:center; font-size:13px; font-style:italic; opacity:0.8;">"{res['logic']}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Formatage dynamique (5 décimales pour Forex, 2 pour Crypto/Indices)
    format_p = ".5f" if "USD=X" in target_symbol else ".2f"
    st.metric("PRIX D'ENTRÉE (MARCHÉ)", f"{res['entry']:{format_p}}")
    
    c1, c2 = st.columns(2)
    c1.success(f"🎯 TAKE PROFIT\n\n{res['tp']:{format_p}}")
    c2.error(f"📍 STOP LOSS\n\n{res['sl']:{format_p}}")
    
    risk = abs(res['entry'] - res['sl'])
    reward = abs(res['tp'] - res['entry'])
    rr = reward / risk if risk != 0 else 0
    st.caption(f"Ratio Risque/Rendement Réel du setup : 1:{rr:.2f}")

    if st.button("🔄 RESET"):
        st.session_state.trade_setup = None
        st.rerun()
