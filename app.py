import streamlit as st
import google.generativeai as genai
import requests
import time
from PIL import Image

# --- CONFIGURATION FINALE ---
st.set_page_config(page_title="PREDATOR INSTITUTIONAL", layout="centered")

# TES CLÉS ACTIVES
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

# --- DESIGN ÉPURÉ ---
st.markdown("""
    <style>
        header, footer, .stDeployButton {visibility: hidden !important;}
        .stApp { background-color: #010203; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .main-card { background: #0a0c10; border: 1px solid #1a1e23; border-radius: 12px; padding: 25px; text-align: center; }
        .label-pro { color: #555; font-size: 10px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; }
        .vision-res { background: rgba(255,255,255,0.02); border: 1px solid #333; border-radius: 15px; padding: 25px; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; letter-spacing:10px; font-weight:100;'>HEDI AYOUB</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF3131; font-size:9px; letter-spacing:4px; margin-top:-10px;'>INSTITUTIONAL VISION TERMINAL</p>", unsafe_allow_html=True)

# --- FLUX MARCHÉ ---
st.write("---")
asset = st.selectbox("", ["US30", "NAS100", "GOLD", "EURUSD", "BTCUSD"], label_visibility="collapsed")
price, change = get_live_price(asset)

if price > 0:
    st.markdown(f"""
        <div class="main-card">
            <div class="label-pro">LIVE MARKET FEED</div>
            <div style="font-size:38px; font-weight:200;">{price:,.2f} <span style="font-size:16px; color:{'#00FF66' if change > 0 else '#FF3131'}">{change:+.2f}%</span></div>
        </div>
    """, unsafe_allow_html=True)

# --- ANALYSE VISION ---
st.write("---")
files = st.file_uploader("UPLOAD 6 TRADINGVIEW CAPTURES", accept_multiple_files=True, label_visibility="collapsed")

if files and len(files) >= 6:
    if st.button("🔥 EXECUTE QUANTUM VISION SCAN", use_container_width=True):
        with st.status("🧠 ANALYSE DES INDICATEURS ET DE LA STRUCTURE...", expanded=True) as status:
            images = [Image.open(f) for f in files]
            prompt = f"""
            Analyse ces graphiques TradingView pour {asset}. 
            Lis tous les indicateurs (RSI, EMA, etc.) et la structure (MSS, FVG).
            L'utilisateur a déjà confirmé la liquidité Bookmap en live.
            Réponds strictement : DIRECTION | CONFIANCE% | ANALYSE_TECHNIQUE_COURTE
            """
            try:
                response = model.generate_content([prompt] + images)
                raw = response.text.split("|")
                side, conf, analysis = raw[0].strip(), raw[1].strip(), raw[2].strip()

                # Calcul TP/SL
                dist = price * 0.005
                tp = price + (dist if "BUY" in side else -dist)
                sl = price - (dist/3.5 if "BUY" in side else -dist/3.5)
                
                status.update(label="ANALYSE TERMINÉE ✅", state="complete")

                color = "#00FF66" if "BUY" in side else "#FF3131"
                st.markdown(f"""
                    <div class="vision-res" style="border-top: 4px solid {color};">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div><div class="label-pro">SIGNAL</div><div style="font-size:45px; font-weight:900; color:{color};">{side}</div></div>
                            <div style="text-align:right;"><div class="label-pro">CONFIANCE</div><div style="font-size:35px; font-weight:bold;">{conf}</div></div>
                        </div>
                        <p style="margin-top:15px; font-size:13px; color:#ccc;">{analysis}</p>
                        <hr style="border:0.1px solid #222;">
                        <div style="display:flex; justify-content:space-between; text-align:center;">
                            <div><div class="label-pro">ENTRY</div><b>{price:,.2f}</b></div>
                            <div><div class="label-pro">TAKE PROFIT</div><b style="color:#00FF66;">{tp:,.2f}</b></div>
                            <div><div class="label-pro">STOP LOSS</div><b style="color:#FF3131;">{sl:,.2f}</b></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur d'analyse : {e}")

# FOOTER
st.markdown("<div style='position:fixed; bottom:20px; left:50%; transform:translateX(-50%); width:200px; background:#0a0c10; padding:12px; border-radius:40px; border:1px solid #1a1e23; display:flex; justify-content:space-around; z-index:1000;'><span style='opacity:0.2;'>🌍</span><span style='opacity:0.2;'>🧭</span><span style='color:#FF3131;'>👑</span></div>", unsafe_allow_html=True)
