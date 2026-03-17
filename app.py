import streamlit as st
import google.generativeai as genai
import requests
import time
from PIL import Image

# --- SETUP ---
st.set_page_config(page_title="HEDI AYOUB | INDICATOR VISION", layout="centered")

GEMINI_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg"
TWELVE_DATA_KEY = "16058da3ebae49158ff0bc81a802c5d3"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_live_price(symbol):
    symbols = {"US30": "DJI", "NAS100": "IXIC", "GOLD": "XAU/USD", "EURUSD": "EUR/USD", "BTCUSD": "BTC/USD"}
    try:
        url = f"https://api.twelvedata.com/quote?symbol={symbols.get(symbol, symbol)}&apikey={TWELVE_DATA_KEY}"
        data = requests.get(url, timeout=5).json()
        return float(data['close']), float(data['percent_change'])
    except: return 0.0, 0.0

# --- STYLE CSS TERMINAL ---
st.markdown("""
    <style>
        header, footer, .stDeployButton {visibility: hidden !important;}
        .stApp { background-color: #010203; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .label-pro { color: #555; font-size: 10px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; }
        .terminal-card { background: #0a0c10; border: 1px solid #1a1e23; border-radius: 12px; padding: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; letter-spacing:10px; font-weight:100;'>HEDI AYOUB</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF3131; font-size:9px; letter-spacing:4px; margin-top:-10px;'>MULTI-INDICATOR ANALYTICS V36.0</p>", unsafe_allow_html=True)

# --- LIVE PRICE ---
asset = st.selectbox("", ["US30", "NAS100", "GOLD", "EURUSD", "BTCUSD"], label_visibility="collapsed")
price, change = get_live_price(asset)

if price > 0:
    st.markdown(f"""
        <div class="terminal-card" style="text-align:center; margin-bottom:20px;">
            <div class="label-pro">MARKET FEED</div>
            <div style="font-size:32px; font-weight:200;">{price:,.2f} <span style="font-size:16px; color:{'#00FF66' if change > 0 else '#FF3131'}">{change:+.2f}%</span></div>
        </div>
    """, unsafe_allow_html=True)

# --- UPLOAD & ANALYSIS ---
uploaded_files = st.file_uploader("GLISSEZ VOS GRAPHES TRADINGVIEW ICI", accept_multiple_files=True, label_visibility="collapsed")

if uploaded_files:
    if st.button("🔥 ANALYSER TOUS LES INDICATEURS", use_container_width=True):
        with st.status("🧠 L'IA DÉCRYPTE VOS INDICATEURS...", expanded=True) as status:
            images = [Image.open(f) for f in uploaded_files]
            
            # PROMPT ULTRA-PRÉCIS POUR INDICATEURS
            prompt = f"""
            Analyse ces graphiques pour {asset}. 
            Tu dois lire TOUS les indicateurs présents : RSI, moyennes mobiles, MACD, nuages Ichimoku, volumes, ainsi que les bougies et tes tracés.
            Vérifie la confluence entre les indicateurs et la structure du prix (SMC/ICT).
            Identifie si les indicateurs confirment une prise de liquidité (vu précédemment sur Bookmap).
            RÉPONDS STRICTEMENT : DIRECTION | CONFIANCE% | RÉSUMÉ_DES_INDICATEURS
            """
            
            try:
                response = model.generate_content([prompt] + images)
                raw = response.text.split("|")
                
                side = raw[0].strip()
                conf = raw[1].strip()
                summary = raw[2].strip()

                # Calcul Niveaux
                dist = price * 0.005
                tp = price + (dist if "BUY" in side else -dist)
                sl = price - (dist/3 if "BUY" in side else -dist/3)

                status.update(label="ANALYSE INDICATEURS TERMINÉE ✅", state="complete")

                # RÉSULTAT FINAL
                color = "#00FF66" if "BUY" in side else "#FF3131"
                st.markdown(f"""
                    <div class="terminal-card" style="border-top: 4px solid {color};">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div><div class="label-pro">SIGNAL FINAL</div><div style="font-size:40px; font-weight:900; color:{color};">{side}</div></div>
                            <div style="text-align:right;"><div class="label-pro">CONFLUENCE</div><div style="font-size:30px; font-weight:bold;">{conf}</div></div>
                        </div>
                        <p style="margin-top:15px; font-size:13px; color:#aaa; line-height:1.5;"><b>Analyse des indicateurs :</b> {summary}</p>
                        <hr style="border:0.1px solid #222;">
                        <div style="display:flex; justify-content:space-between; text-align:center;">
                            <div><div class="label-pro">PRIX</div><b>{price:,.2f}</b></div>
                            <div><div class="label-pro">TAKE PROFIT</div><b style="color:#00FF66;">{tp:,.2f}</b></div>
                            <div><div class="label-pro">STOP LOSS</div><b style="color:#FF3131;">{sl:,.2f}</b></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur Vision : {e}")

# NAV
st.markdown("<div style='position:fixed; bottom:20px; left:50%; transform:translateX(-50%); width:200px; background:#0a0c10; padding:12px; border-radius:40px; border:1px solid #1a1e23; display:flex; justify-content:space-around; z-index:1000;'><span style='opacity:0.2;'>🌍</span><span style='opacity:0.2;'>🧭</span><span style='color:#FF3131;'>👑</span></div>", unsafe_allow_html=True)
