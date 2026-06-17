import streamlit as st

# Dejinta guud ee App-ka (Page Configuration)
st.set_page_config(page_title="GEEDI SPORTS", page_icon="⚽", layout="centered")

# Naqshadda kore ee App-ka (Header)
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>⚽ GEEDI SPORTS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Ku soo dhowaada App-ka ugu dhakhsaha badan ee baahinta ciyaaraha tooska ah!</p>", unsafe_allow_html=True)

st.hr()

# Qaybaha App-ka (Tabs)
tab1, tab2, tab3 = st.tabs(["📺 DAASHO TOOS AH (LIVE)", "📊 NATIIJOOYINKA (SCORES)", "📅 JADWALKA MAANTA"])

# --- TAB 1: KANAALADA LIVE-KA AH ---
with tab1:
    st.subheader("📺 Dooro Channel-ka Aad Rabto Inaad Daawato:")
    
    # Koodhka liiska 4-ta kanaal
    channel = st.selectbox("Kanaalada Diyaar Ah:", [
        "Select a channel...",
        "beIN SPORTS 1 HD", 
        "beIN SPORTS 2 HD", 
        "SKY SPORTS LIVE",
        "CHAMPIONS LEAGUE LIVE"
    ])
    
    if channel == "beIN SPORTS 1 HD":
        st.info("🔥 Baahinta Tooska ah ee beIN Sports 1 waa diyaar!")
        # Fiiro gaar ah: Halkaan waxaad dhex gelin kartaa link kasta oo YouTube Live ama IPTV (.m3u8) ah maalin walba
        st.video("https://www.youtube.com/watch?v=Xn7KWR9EOGQ") 
        
    elif channel == "beIN SPORTS 2 HD":
        st.info("🔥 Baahinta Tooska ah ee beIN Sports 2 waa diyaar!")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
    elif channel == "SKY SPORTS LIVE":
        st.info("🔥 Sky Sports Premium Live")
        st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4")
        
    elif channel == "CHAMPIONS LEAGUE LIVE":
        st.info("🔥 Champions League Premium Live")
        st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4")

# --- TAB 2: NATIIJOOYINKA TOOSKA AH (LIVE SCORES) ---
with tab2:
    st.subheader("📊 Natiijooyinka Ciyaaraha Caalamka Toos")
    st.write("Dhibcaha kooxaha iyo daqiiqadaha ay ciyaartu marayso maadaama ay Live tahay:")
    # Nidaamka ScoreBat iframe-ka ah oo bilaash ku keenaya dhibcaha isaga oo aan API Key u baahnayn
    st.components.v1.iframe("https://www.scorebat.com/embed/livescore/", height=500, scrolling=True)

# --- TAB 3: JADWALKA CIYAARAHA ---
with tab3:
    st.subheader("📅 Kulamada Xiisaha Leh ee Maanta")
    
    st.markdown("""
    * **Premier League:** Arsenal 🆚 Chelsea — *8:30 PM*
    * **La Liga:** Real Madrid 🆚 Barcelona — *10:00 PM*
    * **Serie A:** Juventus 🆚 AC Milan — *6:00 PM*
    """)
    st.success("Talo: Waqtiyada kor ku xusan waa saacadda Geeska Afrika.")
