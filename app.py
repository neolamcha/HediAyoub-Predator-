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

# --- DESIGN TACTIQUE ELITE ---
st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important;}
        .stApp { background-color: #050505; color: white; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 30px; margin-top: 20px; }
        .sub-title { text-align: center; color: #FF3131; font-size: 10px; margin-top: -15px; letter-spacing: 3px; font-weight: bold;}
        .res-box { background: #0a0a0a; padding: 25px; border-radius: 15px; border: 1px solid #1f1f1f; margin: 15px 0; }
        .smt-info { background: rgba(255, 49, 49, 0.05); border-left: 3px solid #FF3131; padding: 12px; font-size: 11px; margin-bottom: 25px; border-radius: 0 10px 10px 0; }
        
        div.stButton > button {
            background: linear-gradient(90deg, #600000 0%, #ff0000 100%) !important;
            color: white !important;
            border: none !important;
            font-size: 16px !important;
            font-weight: bold !important;
            letter-spacing: 3px !important;
            padding: 18px !important;
            border-radius: 12px !important;
            box-shadow: 0 10px 30px rgba(255, 0, 0, 0.3) !important;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

if 'trade_setup' not in st.session_state:
    st.session_state.trade_setup = None

st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>INSTITUTIONAL QUANT V43.0</div>", unsafe_allow_html=True)

assets = {
    "BITCOIN (BTC)": {"symbol": "BTC-USD", "smt": "ETH/BTC"},
    "NASDAQ (NQ)": {"symbol": "NQ=F", "smt": "DOW JONES (YM)"},
    "US30 (DOW)": {"symbol": "YM=F", "smt": "NASDAQ (NQ)"},
    "GOLD (XAU)": {"symbol": "GC=F", "smt": "DXY Index"},
    "EURUSD": {"symbol": "EURUSD=X", "smt": "DXY Index"}
}

target_label = st.selectbox("ACTIF", list(assets.keys()), label_visibility="collapsed")
current_asset = assets[target_label]

st.markdown(f"""
    <div class="smt-info">
        🛡️ <b>FILTRE INSTITUTIONNEL ACTIF</b><br>
        🔄 <b>SMT :</b> Vérification vs <b>{current_asset['smt']}</b><br>
        ⏱️ <b>TIMEFRAMES :</b> Structure 15M | Entrée 5M
    </div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader("CHARGE TES DATASETS SMC/ORDERFLOW", accept_multiple_files=True)

def get_pro_analysis(files, asset_name, smt_ref):
    try:
        images = [PIL.Image.open(f) for f in files]
        prompt = f"""
        En tant qu'analyste senior spécialisé en SMC (Smart Money Concepts) et Order Flow.
        Analyse {asset_name} avec corrélation {smt_ref}.
        Considère : CHoCH, BOS, Fair Value Gaps, et Divergence SMT.
        
        SI LE SETUP N'EST PAS CLAIR À 90%, RÉPONDS "NEUTRAL".
        SI SETUP CLAIR, RÉPONDS EN JSON STRICT :
        {{"side": "BUY", "reason": "...", "confidence": 95}}
        OU
        {{"side": "NEUTRAL", "reason": "Manque de confluence institutionnelle", "confidence": 0}}
        """
        response = model.generate_content([prompt, *images])
        clean_json = re.search(r'\{.*\}', response.text.strip(), re.DOTALL).group()
        return json.loads(clean_json)
    except:
        return {"side": "NEUTRAL", "reason": "Données incomplètes pour valider un setup.", "confidence": 0}

if uploaded_files:
    if st.button("🔥 EXECUTE NEURAL QUANT SCAN"):
        with st.status("📡 ANALYSE DES FLUX EN COURS...") as status:
            ticker = yf.Ticker(current_asset['symbol'])
            price = ticker.history(period="1d")['Close'].iloc[-1]
            
            verdict = get_pro_analysis(uploaded_files, target_label, current_asset['smt'])
            
            if verdict['side'] in ["BUY", "SELL"]:
                is_fx = "USD=X" in current_asset['symbol']
                sl_dist = price * 0.0012 if is_fx else price * 0.006
                side_mult = 1 if verdict['side'] == "BUY" else -1
                
                st.session_state.trade_setup = {
                    "side": verdict['side'],
                    "entry": price,
                    "tp": price + (sl_dist * 3.5 * side_mult),
                    "sl": price - (sl_dist * side_mult),
                    "reason": verdict['reason'],
                    "conf": verdict['confidence']
                }
            else:
                st.session_state.trade_setup = {"side": "NEUTRAL", "reason": verdict['reason']}
            
            status.update(label="SCAN TERMINÉ", state="complete")

# --- AFFICHAGE CONDITIONNEL (LE VRAI DU LOURD) ---
if st.session_state.trade_setup:
    res = st.session_state.trade_setup
    
    if res['side'] == "NEUTRAL":
        st.markdown(f"""
            <div class="res-box" style="border: 1px solid #333;">
                <h2 style="text-align:center; color:#555; margin:0;">NEUTRAL ⚖️</h2>
                <p style="text-align:center; font-size:12px; opacity:0.6; margin-top:10px;">{res['reason']}</p>
            </div>
        """, unsafe_allow_html=True)
        # Ici on ne met rien d'autre. Pas de TP, pas de SL.
    else:
        color = "#00FF66" if res['side'] == "BUY" else "#FF3131"
        fmt = ".5f" if "USD=X" in current_asset['symbol'] else ".2f"
        
        st.markdown(f"""
            <div class="res-box">
                <p style="text-align:center; font-size:10px; letter-spacing:2px; opacity:0.5; margin:0;">SIGNAL IDENTIFIÉ</p>
                <h1 style="text-align:center; color:{color}; font-size:60px; margin:0;">{res['side']}</h1>
                <p style="text-align:center; font-size:12px; opacity:0.8;">{res['reason']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.metric("PRIX D'ENTRÉE", f"{res['entry']:{fmt}}")
        c1, c2 = st.columns(2)
        c1.success(f"TARGET (TP)\n\n{res['tp']:{fmt}}")
        c2.error(f"PROTECTION (SL)\n\n{res['sl']:{fmt}}")
    
    if st.button("🔄 RESET ENGINE"):
        st.session_state.trade_setup = None
        st.rerun()
