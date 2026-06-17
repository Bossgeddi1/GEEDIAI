import streamlit as st

# 1. Dejinta Guud ee Bogga (Icon-ka Tabs-ka browser-ka)
st.set_page_config(
    page_title="GEEDI SPORTS", 
    page_icon="⚽", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Naqshadda Midabada iyo Qurxinta Icon-ka (Custom CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #ffffff;
    }
    /* Qaybta Icon-ka weyn ee sare */
    .logo-container {
        text-align: center;
        margin-top: 10px;
        margin-bottom: -10px;
    }
    .app-icon {
        font-size: 70px;
        background: radial-gradient(circle, rgba(255,102,0,0.2) 0%, rgba(0,0,0,0) 70%);
        padding: 10px;
        display: inline-block;
        border-radius: 50%;
    }
    .main-title {
        text-align: center;
        color: #ff6600;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 42px;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .sub-title {
        text-align: center;
        color: #8b949e;
        font-size: 16px;
        margin-bottom: 25px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: #161b22;
        border-radius: 8px;
        color: #ffffff;
        padding-left: 15px;
        padding-right: 15px;
        font-weight: bold;
        border: 1px solid #30363d;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        border-color: #ff6600;
        color: #ff6600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff6600 !important;
        color: #0d1117 !important;
        border-color: #ff6600 !important;
    }
    div[data-baseweb="select"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Soo bandhigista Icon-ka iyo Magaca rasmiga ah
st.markdown('<div class="logo-container"><div class="app-icon">⚽</div></div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">GEEDI SPORTS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Nidaamka ugu dhakhsaha badan ee baahinta ciyaaraha iyo natiijooyinka tooska ah</div>', unsafe_allow_html=True)

# 4. QAYBTA ALERT-KA
st.error("🚨 **ALERT - KULAN CUSPAD:** Caawa waxaa si toos ah u dhexmaraya kooxaha waawayn. Hubi inaad ku xirnaato kanaalada **beIN SPORTS** si aadan u moogin billowga ciyaarta!")

st.write("---")

# 5. Sameynta Badhamada Tabs-ka
tab_tv, tab_scores, tab_schedule, tab_tips = st.tabs([
    "📺 LIVE", 
    "📊 SCORES", 
    "📅 KULAMADA", 
    "🔮 CORRECT SCORE"
])

# 6. DATA-DA KANAALADA (IPTV)
channels = {
    "beIN SPORTS 1 Low": "http://mhav56789.com:2095/a3028/302858907/22",
    "beIN SPORTS 2 Low": "http://mhav56789.com:2095/a3028/302858907/23",
    "beIN SPORTS 3 Low": "http://mhav56789.com:2095/a3028/302858907/24",
    "beIN SPORTS 4 Low": "http://mhav56789.com:2095/a3028/302858907/16",
    "beIN SPORTS 5 Low": "http://mhav56789.com:2095/a3028/302858907/17",
    "beIN SPORTS 6 Low": "http://mhav56789.com:2095/a3028/302858907/18",
    "beIN SPORTS 7 Low": "http://mhav56789.com:2095/a3028/302858907/2391",
    "beIN SPORTS 8 Low": "http://mhav56789.com:2095/a3028/302858907/19",
    "beIN SPORTS 9 Low": "http://mhav56789.com:2095/a3028/302858907/20",
    "beIN SPORTS 1Xtra Low": "http://mhav56789.com:2095/a3028/302858907/25",
    "beIN SPORTS 1 English Low": "http://mhav56789.com:2095/a3028/302858907/26",
    "beIN SPORTS 1 (512K)": "http://mhav56789.com:2095/a3028/302858907/4905",
    "beIN SPORTS 2 (512K)": "http://mhav56789.com:2095/a3028/302858907/4906",
    "beIN SPORTS 3 (512K)": "http://mhav56789.com:2095/a3028/302858907/4907",
    "beIN SPORTS 4 (512K)": "http://mhav56789.com:2095/a3028/302858907/4898"
}

# --- TAB 1: TV-GA LIVE-KA AH ---
with tab_tv:
    st.markdown("<br>", unsafe_allow_html=True)
    selected_channel = st.selectbox("Dooro kanaalka aad rabto inaad furto:", list(channels.keys()))
    st.markdown(f"<p style='color: #ff6600; font-weight: bold; font-size: 16px;'>▶️ Hadda Baahinta: {selected_channel}</p>", unsafe_allow_html=True)
    st.video(channels[selected_channel])

# --- TAB 2: NATIIJOOYINKA (LIVE SCORES) ---
with tab_scores:
    st.markdown("<br>", unsafe_allow_html=True)
    st.components.v1.iframe("https://www.scorebat.com/embed/livescore/", height=500, scrolling=True)

# --- TAB 3: KULAMADA MAANTA ---
with tab_schedule:
    st.markdown("<br>", unsafe_allow_html=True)
    st.components.v1.iframe("https://www.scorebat.com/embed/", height=500, scrolling=True)

# --- TAB 4: CORRECT SCORE ---
with tab_tips:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #ff6600;'>🔮 Saadaasha Natiijooyinka Saxda Ah</h3>", unsafe_allow_html=True)
    st.components.v1.iframe("https://dashboard.forebet.com/bwidget/v1/predictions/today/en", height=550, scrolling=True)
