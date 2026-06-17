import streamlit as st

st.set_page_config(page_title="GEEDI SPORTS", page_icon="⚽", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>⚽ GEEDI SPORTS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Ku soo dhowaada App-ka ugu dhakhsaha badan ee baahinta ciyaaraha tooska ah!</p>", unsafe_allow_html=True)

# Meeshan st.hr() ayaan ka saaray si aanay cilad u keenin
st.write("---") 

tab1, tab2, tab3 = st.tabs(["📺 LIVE", "📊 SCORES", "📅 JADWAL"])

with tab1:
    st.subheader("Dooro Channel:")
    channel = st.selectbox("Kanaalada:", ["beIN SPORTS 1 HD", "SKY SPORTS LIVE"])
    if channel == "beIN SPORTS 1 HD":
        st.video("https://www.youtube.com/watch?v=Xn7KWR9EOGQ")
    else:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with tab2:
    st.subheader("Natiijooyinka")
    st.components.v1.iframe("https://www.scorebat.com/embed/livescore/", height=400)

with tab3:
    st.write("Kulamada maanta: Arsenal vs Chelsea - 8:30 PM")
