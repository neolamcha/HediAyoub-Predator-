# --- TIMER MODULE (MACRO WINDOW DYNAMIQUE) ---
st.markdown("<div class='card' style='text-align:center;'>", unsafe_allow_html=True)
st.markdown("<p class='label-mini'>Macro Window Open In</p>", unsafe_allow_html=True)

# Intégration du moteur de calcul du temps en temps réel
components.html("""
    <div id="timer-display" style="
        font-family: 'Orbitron', sans-serif; 
        font-size: 45px; 
        color: #ff0000; 
        text-align: center; 
        text-shadow: 0 0 15px rgba(255,0,0,0.6);
        font-weight: 900;
    ">08:14</div>

    <script>
        // Configuration du temps initial (8 min 14 sec)
        let totalSeconds = (8 * 60) + 14; 
        
        const display = document.getElementById('timer-display');
        
        const countdown = setInterval(() => {
            let minutes = Math.floor(totalSeconds / 60);
            let seconds = totalSeconds % 60;
            
            // Formatage 00:00
            let displayMin = minutes < 10 ? '0' + minutes : minutes;
            let displaySec = seconds < 10 ? '0' + seconds : seconds;
            
            display.innerHTML = displayMin + ':' + displaySec;
            
            if (totalSeconds <= 0) {
                display.innerHTML = "OPEN";
                display.style.color = "#00ff41"; // Vert quand la fenêtre est ouverte
                display.style.textShadow = "0 0 15px rgba(0,255,65,0.6)";
                clearInterval(countdown);
            } else {
                totalSeconds--;
            }
        }, 1000);
    </script>
""", height=60)

st.markdown("<p style='color:#333; font-size:10px; margin-top:5px; text-align:center;'>ALGORITHMIC VOLATILITY DETECTED</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
