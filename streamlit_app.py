import streamlit as st

# 1. Dejinta guud (Page Config)
st.set_page_config(page_title="GEEDI SPORTS", layout="centered")

# 2. Naqshadda (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    div.stButton > button {
        background-color: #ffffff !important;
        color: #ff6600 !important;
        font-weight: bold !important;
        width: 100% !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Qaybta Tabs-ka (WAA INAY HORDHAC U AHAATAAN)
tab_tv, tab_scores, tab_jadwal = st.tabs(["📺 LIVE TV", "📊 SCORES", "📅 JADWAL"])

# 4. Content-ka Tabs-ka
with tab_tv:
    st.subheader("Dooro Channel-ka:")
    if st.button("beIN SPORTS AFC 1"):
        st.write("▶️ Waxaa kuu furmay: beIN SPORTS AFC 1")
        st.components.v1.iframe("https://iptv-org.github.io/channels/qa/beINSportsAFC1#SD", height=400)
    
    if st.button("beIN SPORTS 2 Low"):
        st.video("http://mhav56789.com:2095/a3028/302858907/23")

with tab_scores:
    st.components.v1.iframe("https://www.scorebat.com/embed/livescore/", height=500)

with tab_jadwal:
    st.components.v1.iframe("https://www.scorebat.com/embed/", height=500)
