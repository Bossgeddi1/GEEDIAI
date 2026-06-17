import streamlit as st

# Dejinta guud ee bogga
st.set_page_config(page_title="GEEDI SPORTS", page_icon="⚽", layout="centered")

# Qaybta sare (Header)
st.markdown("<h1 style='text-align: center;'>⚽ GEEDI SPORTS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ku soo dhowaada App-ka ugu dhakhsaha badan ee baahinta ciyaaraha tooska ah!</p>", unsafe_allow_html=True)

# Qaybta Tabs-ka (Waxaan magacyada u dhigay tab_tv, tab_scores, tab_jadwal)
tab_tv, tab_scores, tab_jadwal = st.tabs(["📺 LIVE", "📊 SCORES", "📅 JADWAL"])

# --- TAB 1: KANAALADA LIVE-KA AH ---
with tab_tv:
    st.subheader("Dooro Channel-ka Aad Rabto Inaad Daawato:")
    
    channel = st.selectbox("Kanaalada:", [
        "beIN SPORTS 1 HD", 
        "beIN SPORTS 2 HD", 
        "SKY SPORTS LIVE"
    ])
    
    if channel == "beIN SPORTS 1 HD":
        st.info("Baahinta Tooska ah ee beIN Sports 1")
        # Hubi in link-gan uu yahay mid shaqaynaya
        st.video("https://www.youtube.com/watch?v=Xn7KWR9EOGQ")
    elif channel == "beIN SPORTS 2 HD":
        st.info("Baahinta Tooska ah ee beIN Sports 2")
        st.video("https://www.youtube.com/watch?v=Xn7KWR9EOGQ")
    elif channel == "SKY SPORTS LIVE":
        st.info("Sky Sports Premium Live")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# --- TAB 2: SCORES ---
with tab_scores:
    st.subheader("Natiijooyinka Tooska ah")
    st.write("Halkan waxaad ka arki kartaa dhibcaha ciyaaraha.")

# --- TAB 3: JADWAL ---
with tab_jadwal:
    st.subheader("Jadwalka Ciyaaraha")
    st.write("Jadwalka kulamada maanta.")
