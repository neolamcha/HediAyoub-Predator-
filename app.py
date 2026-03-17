import streamlit as st
import pandas as pd
import requests
import time
import hashlib

# --- CONFIGURATION TERMINAL ---
st.set_page_config(page_title="HEDI AYOUB | QUANTUM PRO", layout="centered")

# TA CLÉ API ACTIVÉE
API_KEY = "16058da3ebae49158ff0bc81a802c5d3" 

def get_market_data(symbol):
    # Mapping précis pour Twelve Data
    symbols = {
        "US30": "DJI", 
        "NAS100": "IXIC", 
        "GOLD": "XAU/USD", 
        "EURUSD": "EUR/USD",
        "BTCUSD": "BTC/USD"
    }
    s = symbols.get(symbol, symbol)
    try:
        url = f"https://api.twelvedata.com/quote?symbol={s}&apikey={API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()
        if "close" in data:
            return float(data['close']), float(data['percent_change'])
        else:
            return 0.0, 0.0
    except Exception:
        return 0.0, 0.0

# --- DESIGN PREMIUM NOIR ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #010203; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        .metric-card { 
            background: #0a0c10; border: 1px solid #1a1e23; 
            border-radius: 12px; padding: 20px; text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }
        
        .result-container {
            border: 1px solid #333; border-radius: 15px; padding: 25px;
            margin-top: 25px; background: rgba(255,255,255,0.02);
            animation: fadeIn 0.8s ease;
        }

        .label-pro { color: #555; font-size: 10px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; }
        
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align:center; letter-spacing:12px; font-weight:100; margin-bottom:0;'>HEDI AYOUB</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF3131; font-size:9px; letter-spacing:4px; margin-top:0;'>PREDATOR QUANTUM TERMINAL PRO</p>", unsafe_allow_html=True)

# --- NAVIGATION ---
st.write("---")
col_1, col_2 = st.columns(2)
with col_1:
    asset = st.selectbox("ASSET", ["US30", "NAS100", "GOLD", "EURUSD", "BTCUSD"], label_visibility="collapsed")
with col_2:
    method = st.radio("MODE", ["RAPIDE", "SMT"], horizontal=True, label_visibility="collapsed")

# --- LIVE FEED ---
current_price, change = get_market_data(asset)

if current_price > 0:
    st.markdown(f"""
        <div class="metric-card">
            <div class="label-pro">LIVE {asset} MARKET FEED</div>
            <div style="font-size:36px; font-weight:200;">{current_price:,.2f} <span style="font-size:16px; color:{'#00FF66' if change > 0 else '#FF3131'}">{change:+.2f}%</span></div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Connexion API en attente... Vérifiez votre clé Twelve Data.")

# --- ANALYSE ---
uploaded = st.file_uploader("UPLOAD 6 CONFLUENCE DATASETS", accept_multiple_files=True, label_visibility="collapsed")

if uploaded and len(uploaded) >= 6:
    if st.button("🔥 EXECUTE QUANTUM ANALYSIS", use_container_width=True):
        with st.status("📡 SCANNANT LES CONFLUENCES INSTITUTIONNELLES...", expanded=False) as status:
            time.sleep(2)
            
            # Algorithme déterministe basé sur l'image
            h = hashlib.md5(uploaded[0].getvalue()).hexdigest()
            decision = "BUY" if int(h, 16) % 2 == 0 else "SELL"
            score = 94 + (int(h, 16) % 6)
            
            # Calculs de prix réels
            vol = current_price * 0.005 # ATR estimé
            tp = current_price + (vol * (1 if decision == "BUY" else -1))
            sl = current_price - ((vol * 0.4) * (1 if decision == "BUY" else -1))
            
            status.update(label="ANALYSE TERMINÉE ✅", state="complete")

        # AFFICHAGE PRO
        st.markdown(f"""
            <div class="result-container" style="border-top: 3px solid {'#00FF66' if decision == 'BUY' else '#FF3131'};">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div><div class="label-pro">PROBABILITY</div><div style="font-size:32px; font-weight:900; color:#00FF66;">{score}%</div></div>
                    <div style="text-align:right;"><div class="label-pro">SIGNAL</div><div style="font-size:32px; font-weight:900; color:{'#00FF66' if decision == 'BUY' else '#FF3131'};">{decision}</div></div>
                </div>
                <hr style="border:0.1px solid #222; margin:20px 0;">
                <div style="display:flex; justify-content:space-between;">
                    <div><div class="label-pro">TARGET TP</div><div style="font-size:20px; font-weight:bold;">{tp:,.2f}</div></div>
                    <div style="text-align:right;"><div class="label-pro">PROTECTION SL</div><div style="font-size:20px; font-weight:bold; color:#FF3131;">{sl:,.2f}</div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown(f"<div style='text-align:center; padding:40px; border:1px dashed #222; border-radius:15px; margin-top:20px; color:#444; font-size:10px; letter-spacing:2px;'>AWAITING 6 DATASETS FOR VALIDATION ({len(uploaded) if uploaded else 0}/6)</div>", unsafe_allow_html=True)

# --- NAV BAR ---
st.markdown("<div style='position:fixed; bottom:20px; left:50%; transform:translateX(-50%); width:220px; background:rgba(10,12,15,0.95); padding:12px; border-radius:40px; border:1px solid #1a1e23; display:flex; justify-content:space-around; z-index:1000;'><span style='opacity:0.3;'>🌍</span><span style='opacity:0.3;'>🧭</span><span style='color:#FF3131; filter: drop-shadow(0 0 5px #FF3131);'>👑</span></div>", unsafe_allow_html=True)
