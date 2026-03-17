import streamlit as st
import yfinance as yf
import google.generativeai as genai
import PIL.Image
import json
import re

# --- CONFIGURATION SÉCURISÉE ---
GENAI_API_KEY = "AIzaSyDtFgyDwry4QmPamg6BPQnA8Q4KqlmkKqg" 
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

if 'trade_setup' not in st.session_state:
    st.session_state['trade_setup'] = None

st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

# --- DESIGN "DEEP LIQUIDITY" V47 ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #030303; color: white; }
        .main-title { text-align: center; letter-spacing: 15px; font-weight: 100; font-size: 32px; margin-top: 20px; color: #fff; }
        .sub-title { text-align: center; color: #FF3131; font-size: 9px; margin-top: -15px; letter-spacing: 5px; font-weight: bold; text-transform: uppercase;}
        .res-box { background: linear-gradient(145deg, #0a0a0a, #111); padding: 30px; border-radius: 20px; border: 1px solid #1f1f1f; margin: 20px 0; box-shadow: 0 15px 35px rgba(0,0,0,0.5); }
        .flow-status { background: rgba(0, 255, 102, 0.05); border: 1px solid #00FF66; color: #00FF66; padding: 10px; border-radius: 8px; font-size: 10px; text-align: center; margin-bottom: 20px; }
        
        div.stButton > button {
            background: linear-gradient(90deg, #400000 0%, #ff0000 100%) !important;
            color: white !important;
            border: none !important;
            font-size: 15px !important;
            font-weight: bold !important;
            letter-spacing: 4px !important;
            padding: 20px !important;
            border-radius: 15px !important;
            box-shadow: 0 10px 40px rgba(255, 0, 0, 0.2) !important;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>ORDER FLOW ENGINE V47.0</div>", unsafe_allow_html=True)

# --- MATRICE DE CORRÉLATION ---
assets = {
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "XAG (SILVER)", "anchor": "DXY 1H"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "ES (S&P500)", "anchor": "DXY 1H"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY 1H", "anchor": "DXY 1H"},
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETH", "anchor": "DXY 1H"}
}

target_label = st.selectbox("SÉLECTION ACTIF", list(assets.keys()), label_visibility="collapsed")
c = assets[target_label]

uploaded_files = st.file_uploader("LOGS: DXY 1H + ASSET 15M/5M + BOOKMAP/CVD", accept_multiple_files=True)

def get_order_flow_analysis(files, asset_name, smt, anchor):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        RÔLE: ALGORITHME DE TRADING HAUTE FRÉQUENCE (HFT).
        1. ANALYSE NARRATIVE: DXY 1H (Direction du Dollar).
        2. ANALYSE SMT: Divergence entre {asset_name} et {smt}.
        3. ANALYSE ORDER FLOW: Examine le Delta (CVD) et le Volume. 
           - Cherche l'ABSORPTION: Prix stagne / Delta augmente.
           - Cherche l'AGRESSIVITÉ: Prix explose / Delta explose.
        4. EXÉCUTION: CHoCH 5M confirmé par un pic de volume.

        RÉPONDS EN JSON STRICT :
        {{"side": "SELL", "flow": "Aggressive Selling", "reason": "...", "rr": 4.5}}
        OU
        {{"side": "NEUTRAL", "flow": "Low Conviction", "reason": "Volume insuffisant"}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "flow": "Error", "reason": "Échec de lecture des flux de données."}

if uploaded_files:
    if st.button("⚡ EXECUTE NEURAL FLOW SCAN"):
        with st.status("📡 DÉCODAGE DE L'ORDER FLOW...") as status:
            ticker = yf.Ticker(c['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            res = get_order_flow_analysis(uploaded_files, target_label, c['smt'], c['anchor'])
            
            if res['side'] in ["BUY", "SELL"]:
                is_fx = "USD=X" in c['symbol']
                sl_dist = price * 0.0009 if is_fx else price * 0.0045 # Serrage du SL grâce à l'Order Flow
                m = 1 if res['side'] == "BUY" else -1
                
                st.session_state['trade_setup'] = {
                    "side": res['side'], "entry": price,
                    "tp": price + (sl_dist * res.get('rr', 4.0) * m),
                    "sl": price - (sl_dist * m),
                    "reason": res['reason'], "flow": res['flow']
                }
            else:
                st.session_state['trade_setup'] = {"side": "NEUTRAL", "reason": res['reason'], "flow": res['flow']}
            status.update(label="FLUX DÉCODÉS", state="complete")

# --- INTERFACE DE SORTIE ---
setup = st.session_state.get('trade_setup')

if setup:
    if setup['side'] == "NEUTRAL":
        st.markdown(f'<div class="res-box" style="text-align:center; opacity:0.5;">⚖️ {setup["side"]}<br><small>{setup["reason"]}</small></div>', unsafe_allow_html=True)
    else:
        color = "#00FF66" if setup['side'] == "BUY" else "#FF3131"
        fmt = ".5f" if "USD=X" in c['symbol'] else ".2f"
        
        st.markdown(f"""
            <div class="res-box">
                <div class="flow-status">⚡ ORDER FLOW : {setup['flow'].upper()}</div>
                <h1 style="text-align:center; color:{color}; font-size:60px; margin:0;">{setup['side']}</h1>
                <p style="text-align:center; font-size:11px; opacity:0.7; margin-top:10px;">{setup['reason']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.metric("ENTRÉE INSTITUTIONNELLE", f"{setup['entry']:{fmt}}")
        c1, c2 = st.columns(2)
        c1.success(f"🎯 LIQUIDITY TARGET (TP)\n\n{setup['tp']:{fmt}}")
        c2.error(f"📍 INVALIDATION (SL)\n\n{setup['sl']:{fmt}}")
    
    if st.button("🔄 CLEAR DATA"):
        st.session_state['trade_setup'] = None
        st.rerun()
