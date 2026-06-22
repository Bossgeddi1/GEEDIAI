import streamlit as st

st.set_page_config(
    page_title="GEEDI SPORTS",
    page_icon="⚽",
    layout="wide"
)

# ================= CSS =================

st.markdown("""
<style>

.stApp{
    background:#020817;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:white;
}

.live-box{
    background:#dc2626;
    padding:10px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
    margin-bottom:20px;
}

.card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #1f2937;
}

.footer{
    text-align:center;
    margin-top:50px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================

st.sidebar.title("⚽ GEEDI SPORTS")

page = st.sidebar.radio(
    "MENU",
    [
        "🏠 Home",
        "📺 Live TV",
        "📅 Fixtures",
        "🏆 Results",
        "📰 News"
    ]
)

# ================= HOME =================

if page == "🏠 Home":

    st.markdown(
        "<h1 class='main-title'>⚽ GEEDI SPORTS LIVE</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='live-box'>🔴 LIVE SPORTS TODAY</div>",
        unsafe_allow_html=True
    )

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card'>
        <h1>12</h1>
        <p>Live Matches</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
        <h1>25</h1>
        <p>Leagues</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='card'>
        <h1>8</h1>
        <p>Channels</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🔥 Top Matches")

    st.info("⚽ Arsenal vs Chelsea - 20:00")

    st.info("⚽ Barcelona vs Real Madrid - 22:00")

    st.info("⚽ Inter Milan vs Juventus - 21:45")

# ================= LIVE TV =================

elif page == "📺 Live TV":

    st.title("📺 Live TV")

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

# ================= FIXTURES =================

elif page == "📅 Fixtures":

    st.title("📅 Today's Fixtures")

    st.success("⚽ Arsenal vs Chelsea - 20:00")

    st.success("⚽ Barcelona vs Real Madrid - 22:00")

    st.success("⚽ Inter Milan vs Juventus - 21:45")

# ================= RESULTS =================

elif page == "🏆 Results":

    st.title("🏆 Latest Results")

    st.warning("Arsenal 2 - 1 Liverpool")

    st.warning("Barcelona 3 - 0 Sevilla")

    st.warning("Inter Milan 1 - 1 Juventus")

# ================= NEWS =================

elif page == "📰 News":

    st.title("📰 Sports News")

    st.info("Champions League fixtures announced.")

    st.info("Premier League title race heats up.")

    st.info("Transfer market updates available.")

# ================= FOOTER =================

st.markdown("---")

st.markdown(
    "<div class='footer'>⚽ GEEDI SPORTS © 2026</div>",
    unsafe_allow_html=True
)
