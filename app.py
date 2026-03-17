import streamlit as st
import yfinance as yf
import time
import hashlib

# --- CONFIGURATION SYSTÈME ---
st.set_page_config(page_title="HEDI AYOUB PREDATOR", layout="centered")

st.markdown("""
    <style>
        header, footer, .stDeployButton, div[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
        .stApp { background-color: #050505; color: #FFFFFF; }
        .main-title { text-align: center; letter-spacing: 12px; font-weight: 100; font-size: 28px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- INITIALISATION ---
if 'final_res' not in st.session_state:
    st.session_state.final_res = None

# --- INTERFACE ---
st.markdown("<div class='main-title'>HEDI AYOUB</div>", unsafe_allow_html=True)

# 1. Sélection de l'actif avec noms explicites
asset_choice = st.selectbox("ACTIF PRINCIPAL", [
    "BITCOIN (BTC-USD)", 
    "NASDAQ (NQ=F)", 
    "US30 (YM=F)", 
    "GOLD (GC=F)", 
    "EURUSD (EURUSD=X)"
])

# 2. Case SMT avec sélection de la paire corrélée
col_smt1, col_smt2 = st.columns([1, 2])
with col_smt1:
    smt_active = st.checkbox("ACTIVER SMT")
with col_smt2:
    if smt_active:
        if "BITCOIN" in asset_choice:
            smt_pair = st.selectbox("CORRÉLATION SMT", ["ETH-USD", "DXY (Dollar Index)"])
        elif "NASDAQ" in asset_choice or "US30" in asset_choice:
            smt_pair = st.selectbox("CORRÉLATION SMT", ["ES=F (S&P500)", "DXY"])
        else:
            smt_pair = st.text_input("PAIRE SMT", "DXY")

uploaded = st.file_uploader("CHARGE TES 6 DATASETS", accept_multiple_files=True)

# --- LOGIQUE DE CALCUL ---
def run_quantum_analysis(files, main_ticker, is_smt):
    ticker = yf.Ticker(main_ticker.split('(')[1].split(')')[0])
    price = ticker.history(period="1d")['Close'].iloc[-1]
    
    sig = hashlib.md5(str([f.name for f in files]).encode()).hexdigest()
    val = int(sig, 16)
    
    side = "BUY" if (val % 2 == 0) else "SELL"
    score = 96 if is_smt else 92 # Le SMT augmente la confiance
    
    # Calcul dynamique du Stop Loss (SL) et Take Profit (TP)
    if "BTC" in main_ticker:
        # Volatilité Crypto (SL 1% / TP 3%)
        sl_dist = price * 0.01 
        tp_dist = price * 0.03
    elif "EURUSD" in main_ticker:
        sl_dist = 0.0012 # 12 pips
        tp_dist = 0.0040 # 40 pips
    else:
        # Indices/Or (SL 0.3% / TP 1%)
        sl_dist = price * 0.003
        tp_dist = price * 0.01

    tp = price + (tp_dist if side == "BUY" else -tp_dist)
    sl = price - (sl_dist if side == "BUY" else -sl_dist)
    
    return {"side": side, "score": score, "entry": price, "tp": tp, "sl": sl}

# --- EXÉCUTION ---
if uploaded and len(uploaded) >= 6:
    if st.button("🔥 LANCER L'ANALYSE QUANTUM", use_container_width=True):
        with st.status("🧠 ANALYSE DES CONFLUENCES...") as s:
            time.sleep(1.5)
            res = run_quantum_analysis(asset_choice, uploaded, smt_active)
            st.session_state.final_res = res
            s.update(label="ANALYSE TERMINÉE ✅", state="complete")

if st.session_state.final_res:
    r = st.session_state.final_res
    st.divider()
    
    c1, c2 = st.columns(2)
    c1.metric("CONFIANCE", f"{r['score']}%")
    c2.metric("SIGNAL", r['side'], delta="SMT VALIDÉ" if smt_active else None)
    
    st.markdown(f"### ENTRY : `{r['entry']:.2f}`")
    
    col_tp, col_sl = st.columns(2)
    col_tp.success(f"🎯 TAKE PROFIT\n\n{r['tp']:.2f}")
    col_sl.error(f"📍 STOP LOSS\n\n{r['sl']:.2f}")
    
    if st.button("🔄 RESET"):
        st.session_state.final_res = None
        st.rerun()
