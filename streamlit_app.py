import streamlit as st

# 1. Dejinta Guud ee Bogga
st.set_page_config(
    page_title="GEEDI SPORTS", 
    page_icon="⚽", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Naqshadda Midabada Casriga ah iyo Badhamada waaweyn ee Yacine TV
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
    /* Qurxinta badhamada Tabs-ka */
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
    
    /* BADHAMADA YACINE TV STYLE */
    div.stButton > button {
        background-color: #ffffff !important;
        color: #ff6600 !important;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 55px !important;
        border-radius: 10px !important;
        border: 2px solid #30363d !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2) !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
        margin-bottom: -10px !important;
    }
    div.stButton > button:hover {
        background-color: #ff6600 !important;
        color: #ffffff !important;
        border-color: #ff6600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Soo bandhigista Icon-ka iyo Magaca rasmiga ah
st.markdown('<div class="logo-container"><div class="app-icon">⚽</div></div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">GEEDI SPORTS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Nidaamka ugu dhakhsaha badan ee baahinta ciyaaraha iyo natiijooyinka tooska ah</div>', unsafe_allow_html=True)

# 4. QAYBTA ALERT-KA
st.error("🚨 **ALERT - KULAN CUSPAD:** Ciyaarihii ugu dambeeyey ee AFC ayaa hadda toos u socda! Guji badhamada hoose si aad u furto kanaalka baahinta dhabta ah.")

st.write("---")

# 5. Sameynta Badhamada Tabs-ka
tab_tv, tab_scores, tab_schedule, tab_tips = st.tabs([
    "📺 LIVE TV", 
    "📊 SCORES", 
    "📅 KULAMADA", 
    "🔮 CORRECT SCORE"
])

# 6. DATA-DA KANAALADA (Halkaan waxaa ku jira link-gaagii cusbaa)
channels = {
    "beIN SPORTS AFC 1 (Cusub)": "https://iptv-org.github.io/channels/qa/beINSportsAFC1#SD",
    "beIN SPORTS 1 Low": "http://mhav56789.com:2095/a3028/302858907/22",
    "beIN SPORTS 2 Low": "http://mhav56789.com:2095/a3028/302858907/23",
    "beIN SPORTS 3 Low": "http://mhav56789.com:2095/a3028/302858907/24",
    "beIN SPORTS 4 Low": "http://mhav56789.com:2095/a3028/302858907/16"
}

# --- TAB 1: TV-GA LIVE-KA AH ---
with tab_tv:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e;'>Guji kanaalka aad rabto inaad daawato:</p>", unsafe_allow_html=True)
    
    # Samaynta badhamada taxan
    for channel_name, link in channels.items():
        if st.button(f"📺 {channel_name}"):
            st.markdown(f"<p style='color: #ff6600; font-weight: bold; font-size: 18px; text-align: center; margin-top: 15px;'>▶️ Hadda Waxaa kuu furmaaya: {channel_name}</p>", unsafe_allow_html=True)
            
            # Shuruud lagu hubinayo hadda link-ga uu yahay kii github si loogu baahiyo qaab habboon
            if "github" in link:
                st.video(link, format="video/mp4")
            else:
                st.video(link)
            st.write("---")

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
