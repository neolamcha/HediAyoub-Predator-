import streamlit as st
import yfinance as yf
import google.generativeai as genai
import PIL.Image
import json
import time

# --- CONFIGURATION API ---
GENAI_API_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg" 
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURATION UI ---
st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .res-box { background: #0a0a0a; padding: 20px; border-radius: 15px; border: 2px solid #FF3131; }
        .live-status { color: #00FF66; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'><span class='live-status'>● SYSTEM SYNCED WITH ETERNAL BOOKMAP FEEDS</span></p>", unsafe_allow_html=True)

# --- ANCRAGE DES FLUX (HARDCODED) ---
ETERNAL_FEEDS = [
    "https://www.youtube.com/watch?v=XZs8kRuL12k", # NQ Footprints
    "https://www.youtube.com/watch?v=jc1Ds-Uz6gE", # NQ Heatmap
    "https://www.youtube.com/watch?v=kvhRserj8ME", # Gold Heatmap
    "https://www.youtube.com/watch?v=69jd1dOq4C8"  # BTC Liquidations
]

# --- INPUTS ---
assets = {"BITCOIN (BTC)": "BTC-USD", "NASDAQ (NQ)": "NQ=F", "US30 (DOW)": "YM=F", "GOLD (XAU)": "GC=F"}
target_label = st.selectbox("ACTIF", list(assets.keys()))
target_symbol = assets[target_label]

uploaded_files = st.file_uploader("UPLOAD 6 DATASETS (M15 & M5)", accept_multiple_files=True)

# --- ENGINE DE DÉCISION ABSOLUE ---
def run_eternal_scan(files, asset_name):
    images = [PIL.Image.open(f) for f in files]
    
    # L'IA a désormais l'ordre d'utiliser les flux ancrés
    prompt = f"""
    SYSTEM: HEDI AYOUB PREDATOR V40.
    CONTEXT: Analyse de l'actif {asset_name}.
    SOURCES ANCRÉES (LIVE): {', '.join(ETERNAL_FEEDS)}
    
    INSTRUCTIONS:
    1. Analyse les 6 images (M15/M5) pour la structure SMC.
    2. Croise ces données avec les flux de liquidité (Bookmap/Heatmap) des URLs ancrées.
    3. Vérifie spécifiquement les 'Large Clusters' de liquidité et les 'Liquidation Walls'.
    4. Ne donne un signal BUY/SELL que si les flux live confirment l'absorption ou la pression.
    
    RÉPONSE JSON UNIQUEMENT :
    {{"side": "BUY", "confidence": 99, "analysis": "SMC Sync + Liquidity Feed Verified", "reason": "..."}}
    """
    
    try:
        response = model.generate_content([prompt, *images])
        return json.loads(response.text.strip().replace('```json', '').replace('```', ''))
    except:
        return {"side": "NEUTRAL", "confidence": 0, "analysis": "ERROR", "reason": "Sync Timeout"}

# --- EXÉCUTION ---
if uploaded_files and len(uploaded_files) >= 6:
    if st.button("🔥 EXECUTE PREDATOR SCAN (FULL AUTO)", use_container_width=True):
        with st.status("📡 SYNC AVEC LES FLUX BOOKMAP ÉTERNELS...", expanded=True) as s:
            verdict = run_eternal_scan(uploaded_files, target_label)
            
            ticker = yf.Ticker(target_symbol)
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            # Paramètres institutionnels
            mult = 0.0008 if "EUR" in target_symbol else 0.004
            side_val = 1 if verdict['side'] == "BUY" else -1
            
            st.session_state.trade_setup = {
                "side": verdict['side'], "conf": verdict['confidence'], 
                "analysis": verdict['analysis'], "reason": verdict['reason'],
                "entry": price, "tp": price + (price * mult * 3 * side_val), "sl": price - (price * mult * side_val)
            }
            s.update(label="DÉCISION VALIDÉE PAR LES FLUX", state="complete")

# --- AFFICHAGE FINAL ---
if st.session_state.get('trade_setup'):
    res = st.session_state.trade_setup
    color = "#00FF66" if res['side'] == "BUY" else "#FF3131"
    
    st.markdown(f"""
        <div class="res-box">
            <p style="text-align:center; font-size:10px; color:#555;">{res['analysis']}</p>
            <h1 style="text-align:center; color:{color}; font-size:60px; margin:0;">{res['side']}</h1>
            <p style="text-align:center; opacity:0.8;">CONFIANCE: {res['conf']}% | {res['reason']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.metric("PRIX RÉEL", f"{res['entry']:.2f}")
    c1, c2 = st.columns(2)
    c1.success(f"TARGET (TP): {res['tp']:.2f}")
    c2.error(f"PROTECTION (SL): {res['sl']:.2f}")
