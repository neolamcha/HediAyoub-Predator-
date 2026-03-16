import streamlit as st

# CONFIGURATION FULL POWER
st.set_page_config(page_title="HediAyoub - PREDATOR", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
        /* 1. SUPPRESSION TOTALE DES MARGES STREAMLIT */
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            max-width: 100% !important;
        }
        
        /* 2. FOND NOIR ABSOLU */
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }

        /* 3. FULL POWER CAMERA - EXPLOITATION TOTALE DE L'ÉCRAN */
        div[data-testid="stCameraInput"] {
            width: 100% !important;
            max-width: 100% !important;
            margin: 0 auto !important;
            border: 1px solid #FF3131 !important;
            border-radius: 0px !important; /* Carré pour coller aux bords */
        }
        
        /* Forcer la vidéo à remplir tout l'espace disponible sans bandes noires */
        video {
            object-fit: cover !important; 
            width: 100% !important;
            height: auto !important;
        }

        /* 4. MENUS ET BOUTONS DARK */
        div[data-baseweb="select"] > div { background-color: #0A0A0A !important; border: 1px solid #333 !important; }
        .stButton>button { background-color: #1A1A1A; color: #FF3131; border: 1px solid #FF3131; }
        
        /* Matrice visuelle compacte */
        .status-cell { text-align: center; padding: 5px; border-radius: 4px; font-weight: bold; font-size: 10px; }
        .ready { background-color: #00FF00; color: black; }
        .missing { background-color: #111; color: #333; border: 1px solid #222; }
        
        .app-title { color: #FF3131; text-transform: uppercase; font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ... (Le reste du code reste le même, l'interface sera juste beaucoup plus large)
