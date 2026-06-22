import streamlit as st

st.set_page_config(
    page_title="GEEDI SPORTS",
    page_icon="⚽",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color:#0d1117;
    color:white;
}

footer {
    visibility:hidden;
}

.main-title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:white;
}

.card {
    background:#161b22;
    padding:15px;
    border-radius:10px;
    margin:10px 0;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("⚽ GEEDI SPORTS")

page = st.sidebar.radio(
    "MENU",
    ["🏠 Home", "📺 Live TV", "📅 Fixtures", "🏆 Results", "📰 News"]
)

# HOME
if page == "🏠 Home":

    st.markdown(
        "<h1 class='main-title'>⚽ GEEDI SPORTS LIVE</h1>",
        unsafe_allow_html=True
    )

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Soccerball.svg/1024px-Soccerball.svg.png",
        width=150
    )

    st.success("Ku soo dhawoow GEEDI SPORTS")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Live Matches", "12")

    with col2:
        st.metric("Leagues", "25")

    with col3:
        st.metric("Channels", "8")

# LIVE TV
elif page == "📺 Live TV":

    st.title("📺 LIVE TV")

    channels = {
        "Demo Channel 1":
        "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",

        "Demo Channel 2":
        "https://test-streams.mux.dev/test_001/stream.m3u8"
    }

    selected = st.selectbox(
        "Dooro Channel",
        list(channels.keys())
    )

    st.video(channels[selected])

# FIXTURES
elif page == "📅 Fixtures":

    st.title("📅 Today's Fixtures")

    st.markdown("""
    <div class='card'>
    Arsenal vs Chelsea - 20:00
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    Barcelona vs Real Madrid - 22:00
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    Inter Milan vs Juventus - 21:45
    </div>
    """, unsafe_allow_html=True)

# RESULTS
elif page == "🏆 Results":

    st.title("🏆 Latest Results")

    st.markdown("""
    <div class='card'>
    Arsenal 2 - 1 Liverpool
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    Barcelona 3 - 0 Sevilla
    </div>
    """, unsafe_allow_html=True)

# NEWS
elif page == "📰 News":

    st.title("📰 Sports News")

    st.markdown("""
    <div class='card'>
    Champions League fixtures announced.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    Premier League title race heats up.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 GEEDI SPORTS")
