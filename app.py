import streamlit as st

# CONFIGURATION PREDATOR V3.3 (CAMERA FIX)
st.set_page_config(page_title="HediAyoub - PREDATOR", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
        
        /* FIX CAMERA : Forcer le cadrage et supprimer les marges blanches */
        div[data-testid="stCameraInput"] {
            border: 2px solid #FF3131 !important;
            border-radius: 15px;
            overflow: hidden;
            max-width: 100% !important;
        }
        
        /* Forcer la vidéo à s'adapter sans zoomer/déformer */
        video {
            object-fit: contain !important;
            background-color: #000 !important;
        }

        /* Style Ultra Dark pour le reste */
        div[data-baseweb="select"] > div { background-color: #0A0A0A !important; border: 1px solid #333 !important; }
        .stButton>button { background-color: #1A1A1A; color: #FF3131; border: 1px solid #FF3131; border-radius: 5px; }
        .status-cell { text-align: center; padding: 10px; border-radius: 6px; font-weight: bold; }
        .ready { background-color: #002200; color: #00FF00; border: 1px solid #00FF00; }
        .missing { background-color: #050505; color: #333; border: 1px solid #222; }
        .app-title { color: #FF3131; text-transform: uppercase; font-size: 26px; font-weight: bold; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# ... (Reste du code identique)
