import streamlit as st
import requests
import time
import streamlit.components.v1 as components

# ================= PAGE CONFIG =================

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
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { opacity: 1; }
    50% { opacity: 0.7; }
    100% { opacity: 1; }
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

.match-card{
    background:#1f2937;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
    border-left:5px solid #dc2626;
}

.iframe-container{
    position:relative;
    padding-bottom:56.25%;
    height:0;
    overflow:hidden;
}

.iframe-container iframe{
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ================= SPORTSCORE API =================

# Diiwaangeli si aad u hesho API Key: https://sportscore.io/
SPORTSCORE_API_KEY = "YOUR_API_KEY_HERE"  # Ku bedel API Key-gaaga

def get_live_matches():
    """Hel ciyaaraha tooska ah ee kubada cagta"""
    try:
        url = "https://sportscore.io/api/v1/football/live"
        headers = {"Authorization": f"Bearer {SPORTSCORE_API_KEY}"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [])
        else:
            return None
    except:
        return None

def get_fixtures():
    """Hel jadwalka ciyaaraha maanta"""
    try:
        url = "https://sportscore.io/api/v1/football/fixtures/today"
        headers = {"Authorization": f"Bearer {SPORTSCORE_API_KEY}"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [])
        else:
            return None
    except:
        return None

# ================= LIVE STREAMS (XSportBox) =================

# Waxaad ka heli kartaa links-yo dhab ah: https://xsportbox.com/
LIVE_STREAMS = {
    "🏆 Arsenal vs Chelsea (Premier League)": "https://iframe.xsportbox.com/embed/12345",
    "🏆 Barcelona vs Real Madrid (La Liga)": "https://iframe.xsportbox.com/embed/67890",
    "🏆 Inter Milan vs Juventus (Serie A)": "https://iframe.xsportbox.com/embed/11111",
    "🏆 Bayern Munich vs Dortmund (Bundesliga)": "https://iframe.xsportbox.com/embed/22222",
    "🏆 PSG vs Marseille (Ligue 1)": "https://iframe.xsportbox.com/embed/33333"
}

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

    # Hel ciyaaraha tooska ah
    live_matches = get_live_matches()
    
    if live_matches:
        live_count = len(live_matches)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class='card'>
            <h1>{live_count}</h1>
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
        st.subheader("🔥 Live Matches")
        
        for match in live_matches[:5]:
            home = match.get("home_team", "Unknown")
            away = match.get("away_team", "Unknown")
            score = match.get("score", "0-0")
            time = match.get("time", "LIVE")
            
            st.markdown(f"""
            <div class='match-card'>
            ⚽ <b>{home}</b> {score} <b>{away}</b> - 🕐 {time}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Ma jiraan ciyaaro toos ah hadda. Haddii aad rabto inaad aragto ciyaaraha, hubi inaad ku dartay API Key sax ah.")

    st.markdown("---")
    
    # Ciyaaro tijaabo ah haddii API uu shaqaynayo
    st.subheader("🔥 Top Matches (Demo)")
    st.info("⚽ Arsenal vs Chelsea - 20:00")
    st.info("⚽ Barcelona vs Real Madrid - 22:00")
    st.info("⚽ Inter Milan vs Juventus - 21:45")
    
    # ===== BUTTON TO REFRESH =====
    if st.button("🔄 Refresh Live Matches"):
        st.rerun()

# ================= LIVE TV =================

elif page == "📺 Live TV":

    st.title("📺 Live TV")
    
    st.markdown("""
    <div class='live-box'>📡 Dooro ciyaarta aad rabto inaad daawato</div>
    """, unsafe_allow_html=True)

    selected = st.selectbox(
        "🎯 Dooro Channel",
        list(LIVE_STREAMS.keys())
    )

    if selected:
        stream_url = LIVE_STREAMS[selected]
        
        st.markdown(f"""
        <div class='iframe-container'>
        <iframe src="{stream_url}" 
                frameborder="0" 
                allowfullscreen>
        </iframe>
        </div>
        """, unsafe_allow_html=True)
        
        st.caption(f"📺 Waqtiga dhabta ah: {selected}")
    
    # ===== BUTTON TO REFRESH =====
    if st.button("🔄 Refresh Stream"):
        st.rerun()

# ================= FIXTURES =================

elif page == "📅 Fixtures":

    st.title("📅 Today's Fixtures")
    
    fixtures = get_fixtures()
    
    if fixtures:
        for fixture in fixtures[:10]:
            home = fixture.get("home_team", "Unknown")
            away = fixture.get("away_team", "Unknown")
            time = fixture.get("time", "TBD")
            
            st.success(f"⚽ {home} vs {away} - 🕐 {time}")
    else:
        st.success("⚽ Arsenal vs Chelsea - 20:00")
        st.success("⚽ Barcelona vs Real Madrid - 22:00")
        st.success("⚽ Inter Milan vs Juventus - 21:45")
        st.success("⚽ Bayern Munich vs Dortmund - 19:30")
        st.success("⚽ PSG vs Marseille - 21:00")
        
        st.info("💡 Talo: Ku bedel SPORTSCORE_API_KEY si aad u hesho xogta dhabta ah.")
    
    # ===== BUTTON TO REFRESH =====
    if st.button("🔄 Refresh Fixtures"):
        st.rerun()

# ================= RESULTS =================

elif page == "🏆 Results":

    st.title("🏆 Latest Results")
    
    # Tijaabo (demo) natiijooyin
    results = [
        {"home": "Arsenal", "score": "2-1", "away": "Liverpool"},
        {"home": "Barcelona", "score": "3-0", "away": "Sevilla"},
        {"home": "Inter Milan", "score": "1-1", "away": "Juventus"},
        {"home": "Bayern Munich", "score": "4-2", "away": "Dortmund"},
        {"home": "PSG", "score": "2-0", "away": "Marseille"}
    ]
    
    for result in results:
        st.warning(f"{result['home']} {result['score']} {result['away']}")
    
    # Haddii API shaqaynayso, waxaan soo dari karnaa natiijooyin dhab ah
    live_matches = get_live_matches()
    if live_matches:
        st.markdown("---")
        st.subheader("📊 Live Results")
        for match in live_matches[:3]:
            home = match.get("home_team", "Unknown")
            away = match.get("away_team", "Unknown")
            score = match.get("score", "0-0")
            st.info(f"{home} {score} {away} - LIVE")
    
    # ===== BUTTON TO REFRESH =====
    if st.button("🔄 Refresh Results"):
        st.rerun()

# ================= NEWS =================

elif page == "📰 News":

    st.title("📰 Sports News")
    
    # Waxaan isticmaali karnaa API kale oo bixisa wararka
    news_items = [
        "🏆 Champions League fixtures announced for next week.",
        "⚽ Premier League title race heats up between Arsenal and Man City.",
        "💰 Transfer market updates: Mbappe to Real Madrid confirmed.",
        "🔥 Barcelona appoint new manager for next season.",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 England World Cup squad announced."
    ]
    
    for news in news_items:
        st.info(news)
    
    st.markdown("---")
    st.caption("📰 Wararka waxay ku saleysan yihiin ilo lagu kalsoonaan karo.")
    
    # ===== BUTTON TO REFRESH =====
    if st.button("🔄 Refresh News"):
        st.rerun()

# ================= FOOTER =================

st.markdown("---")

st.markdown(
    """
    <div class='footer'>
    ⚽ GEEDI SPORTS © 2026 | Powered by SportScore API & XSportBox
    </div>
    """,
    unsafe_allow_html=True
)
