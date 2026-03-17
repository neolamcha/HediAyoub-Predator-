import streamlit as st
import google.generativeai as genai
import requests
import time
from PIL import Image

# --- CONFIGURATION SYSTÈME ---
st.set_page_config(page_title="HEDI AYOUB | PREDATOR VISION", layout="centered")

# CLÉS API ACTIVÉES
GEMINI_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg"
TWELVE_DATA_KEY = "16058da3ebae49158ff0bc81a802c5d3"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- MOTEUR DE PRIX RÉEL ---
def get_live_price(symbol):
    symbols = {"US30": "DJI", "NAS100": "IXIC", "GOLD": "XAU/USD", "EURUSD": "EUR/USD", "BTCUSD": "BTC/USD"}
    try:
        url = f"https://api.twelvedata.com/quote?symbol={symbols.get(symbol, symbol)}&apikey={TWELVE_DATA_KEY}"
        data = requests.get(url, timeout=5).json()
        return float(data['close']), float(data['percent_change'])
    except: return 0.0, 0.0

# --- DESIGN "PREDATOR" ---
st.markdown("""
    <style>
        header, footer, .stDeployButton {visibility: hidden !important;}
        .stApp { background-color: #010203; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        .main-card { background: #0a0c10; border: 1px solid #1a1e23; border-radius: 12px; padding: 20px; text-align: center; }
        .vision-box { background: rgba(255, 255, 255, 0.02); border: 1px solid #333; border-radius: 15px; padding: 25px; margin-top: 20px; }
        .label-pro { color: #555; font-size: 10px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; }
        .signal-text { font-size: 45px; font-weight: 900; letter-spacing: -1px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; letter-spacing:12px; font-weight:100; margin-bottom:0;'>HEDI AYOUB</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF3131; font-size:9px; letter-spacing:4px; margin-top:0;'>PREDATOR QUANTUM VISION V34.0</p>", unsafe_allow_html=True)

# --- NAVIGATION ---
st.write("---")
asset = st.selectbox("ACTIF À ANALYSER", ["US30", "NAS100", "GOLD", "EURUSD", "BTCUSD"], label_visibility="collapsed")

# Affichage du prix live
price, change = get_live_price(asset)
if price > 0:
    st.markdown(f"""
        <div class="main-card">
            <div class="label-pro">LIVE MARKET FEED</div>
            <div style="font-size:32px; font-weight:200;">{price:,.2f} <span style="font-size:16px; color:{'#00FF66' if change > 0 else '#FF3131'}">{change:+.2f}%</span></div>
        </div>
    """, unsafe_allow_html=True)

# --- UPLOAD DES 6 CONFLUENCES ---
st.write("---")
uploaded_files = st.file_uploader("CHARGEZ VOS 6 GRAPHES (BOOKMAP, SMT, TF...)", accept_multiple_files=True, label_visibility="collapsed")

if uploaded_files and len(uploaded_files) >= 6:
    if st.button("🔥 LANCER L'ANALYSE PAR INTELLIGENCE VISIONNAIRE", use_container_width=True):
        with st.status("🧠 GEMINI AI ANALYSE LES STRUCTURES DE MARCHÉ...", expanded=True) as status:
            
            # Préparation des images pour l'IA
            images = [Image.open(f) for f in uploaded_files]
            
            # Prompt de Trading Institutionnel
            prompt = f"""
            Analyse ces 6 graphiques de trading pour {asset}. 
            Tu dois agir comme un trader de fonds spéculatifs.
            Cherche : 1. Zones de liquidité Bookmap. 2. Divergences RSI/Delta. 3. Structure SMT. 4. Order Blocks.
            Réponds EXACTEMENT sous ce format sans texte inutile :
            DIRECTION | SCORE% | RAISON_TECHNIQUE_COURTE
            """
            
            try:
                response = model.generate_content([prompt] + images)
                raw_res = response.text.split("|")
                
                side = raw_res[0].strip()
                confidence = raw_res[1].strip()
                analysis = raw_res[2].strip()

                # Calcul des niveaux réels basés sur la volatilité
                dist = price * 0.005
                tp = price + (dist if "BUY" in side else -dist)
                sl = price - (dist/3 if "BUY" in side else -dist/3)

                status.update(label="ANALYSE VISION TERMINÉE", state="complete")

                # AFFICHAGE FINAL
                color_sig = "#00FF66" if "BUY" in side else "#FF3131"
                st.markdown(f"""
                    <div class="vision-box" style="border-top: 4px solid {color_sig};">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div><div class="label-pro">SIGNAL VISION</div><div class="signal-text" style="color:{color_sig};">{side}</div></div>
                            <div style="text-align:right;"><div class="label-pro">CONFIANCE</div><div style="font-size:35px; font-weight:bold;">{confidence}</div></div>
                        </div>
                        <p style="margin-top:15px; font-size:13px; color:#ccc;"><b>Analyse IA :</b> {analysis}</p>
                        <hr style="border:0.1px solid #222; margin:20px 0;">
                        <div style="display:flex; justify-content:space-between;">
                            <div><div class="label-pro">OBJECTIF TP</div><div style="font-size:22px; font-weight:bold; color:#00FF66;">{tp:,.2f}</div></div>
                            <div style="text-align:right;"><div class="label-pro">PROTECTION SL</div><div style="font-size:22px; font-weight:bold; color:#FF3131;">{sl:,.2f}</div></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur d'analyse : {e}")
else:
    st.markdown(f"<div style='text-align:center; padding:40px; border:1px dashed #222; border-radius:15px; color:#444; font-size:10px; letter-spacing:2px;'>EN ATTENTE DE 6 CONFLUENCES VISUELLES ({len(uploaded_files) if uploaded_files else 0}/6)</div>", unsafe_allow_html=True)

# Navigation
st.markdown("""<div style='position:fixed; bottom:20px; left:50%; transform:translateX(-50%); width:220px; background:rgba(10,12,15,0.95); padding:12px; border-radius:40px; border:1px solid #1a1e23; display:flex; justify-content:space-around; z-index:1000;'><span style='opacity:0.3;'>🌍</span><span style='opacity:0.3;'>🧭</span><span style='color:#FF3131; filter: drop-shadow(0 0 5px #FF3131);'>👑</span></div>""", unsafe_allow_html=True)
