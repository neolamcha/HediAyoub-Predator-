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

st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .res-box { background: #0a0a0a; padding: 20px; border-radius: 15px; border: 1px solid #1f1f1f; }
    </style>
""", unsafe_allow_html=True)

if 'trade_setup' not in st.session_state:
    st.session_state.trade_setup = None

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)

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
uploaded_files = st.file_uploader("CHARGE TES GRAPHES", accept_multiple_files=True)

def get_safe_analysis(files, asset_name, current_price):
    images = [PIL.Image.open(f) for f in files]
    
    # On donne le prix actuel à l'IA pour qu'elle ne dise pas n'importe quoi
    prompt = f"""
    PRIX ACTUEL : {current_price}
    Analyse ces images pour {asset_name}. 
    1. Identifie la direction (BUY/SELL).
    2. Trouve le Stop Loss logique (Swing High/Low).
    3. Trouve le Take Profit (Zone de liquidité).
    
    Réponds UNIQUEMENT ce format JSON:
    {{"side": "BUY", "confidence": 95, "sl": 0.0, "tp": 0.0, "reason": "..."}}
    """
    
    try:
        response = model.generate_content([prompt, *images])
        # Extraction robuste du JSON
        json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return None
    except:
        return None

if uploaded_files:
    if st.button("🔥 ANALYSER LA CONFLUENCE", use_container_width=True):
        with st.status("🧠 CALCUL EN COURS...") as s:
            # 1. Obtenir le prix réel d'abord
            ticker = yf.Ticker(target_symbol)
            hist = ticker.history(period="1d")
            price = hist['Close'].iloc[-1]
            
            # 2. Envoyer à l'IA
            res = get_safe_analysis(uploaded_files, target_label, price)
            
            if res:
                # 3. Sécurité : Si l'IA donne 0 ou un prix trop éloigné, on calcule mathématiquement
                is_fx = "USD=X" in target_symbol
                safe_dist = price * 0.005 if not is_fx else 0.0015
                
                final_sl = res['sl'] if res['sl'] != 0 else (price - safe_dist if res['side'] == "BUY" else price + safe_dist)
                final_tp = res['tp'] if res['tp'] != 0 else (price + (safe_dist * 3) if res['side'] == "BUY" else price - (safe_dist * 3))

                st.session_state.trade_setup = {
                    "side": res['side'],
                    "conf": res['confidence'],
                    "entry": price,
                    "tp": final_tp,
                    "sl": final_sl,
                    "reason": res['reason']
                }
                s.update(label="ANALYSE RÉUSSIE", state="complete")
            else:
                st.error("L'IA a échoué. Réessaie avec une image plus nette.")

if st.session_state.trade_setup:
    t = st.session_state.trade_setup
    st.divider()
    
    st.markdown(f'<div class="res-box"><h1 style="text-align:center; color:#FF3131;">{t["side"]}</h1><p style="text-align:center;">{t["reason"]}</p></div>', unsafe_allow_html=True)
    
    st.metric("ENTRÉE", f"{t['entry']:.5f}" if "USD=X" in target_symbol else f"{t['entry']:.2f}")
    
    c1, c2 = st.columns(2)
    fmt = ".5f" if "USD=X" in target_symbol else ".2f"
    c1.success(f"🎯 TP: {t['tp']:{fmt}}")
    c2.error(f"📍 SL: {t['sl']:{fmt}}")
    
    if st.button("🔄 RESET"):
        st.session_state.trade_setup = None
        st.rerun()
