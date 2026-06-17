import streamlit as st

# 1. Dejinta Guud ee Bogga
st.set_page_config(page_title="GEEDI SPORTS", page_icon="⚽", layout="centered")

# 2. Naqshadda CSS (Madow iyo Oranji)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .main-title { text-align: center; color: #ff6600; font-family: sans-serif; font-size: 32px; font-weight: bold; }
    div.stButton > button {
        background-color: #ffffff !important;
        color: #ff6600 !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 50px !important;
        border-radius: 8px !important;
        border: 2px solid #ff6600 !important;
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header
st.markdown('<div class="main-title">⚽ GEEDI SPORTS</div>', unsafe_allow_html=True)
st.markdown("---")

# 4. Tabs
tab_tv, tab_scores, tab_jadwal = st.tabs(["📺 LIVE TV", "📊 SCORES", "📅 JADWAL"])

# 5. Kanaalada (Links-kaaga dhabta ah)
channels = {
    "beIN SPORTS AFC 1": "https://iptv-org.github.io/channels/qa/beINSportsAFC1#SD",
    "beIN SPORTS 2 Low": "http://mhav56789.com:2095/a3028/302858907/23",
    "beIN SPORTS 3 Low": "http://mhav56789.com:2095/a3028/302858907/24",
    "beIN SPORTS 4 Low": "http://mhav56789.com:2095/a3028/302858907/16"
}

# 6. Logiga Tabs-ka
with tab_tv:
    st.subheader("Dooro Channel-ka:")
    for name, link in channels.items():
        if st.button(name):
            st.write(f"▶️ Waxaa kuu furmay: {name}")
            # Isticmaalka HTML5 player si uu link-ga u shaqeeyo
            video_html = f"""
            <video width="100%" height="300" controls autoplay>
                <source src="{link}" type="application/x-mpegURL">
                Your browser does not support the video.
            </video>
            """
            st.components.v1.html(video_html, height=320)

with tab_scores:
    st.components.v1.iframe("https://www.scorebat.com/embed/livescore/", height=500, scrolling=True)

with tab_jadwal:
    st.components.v1.iframe("https://www.scorebat.com/embed/", height=500, scrolling=True)
