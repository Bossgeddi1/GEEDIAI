import streamlit as st

# 1. Dejinta guud
st.set_page_config(page_title="GEEDI SPORTS", layout="centered")

# 2. Qaybta Tabs-ka (Waa in koodhkan uu ka horreeyaa amarka 'with tab_tv')
tab_tv, tab_scores, tab_jadwal = st.tabs(["📺 LIVE TV", "📊 SCORES", "📅 JADWAL"])

# 3. Hadda ayaad isticmaali kartaa 'with tab_tv'
with tab_tv:
    st.write("Dooro kanaalka:")
    if st.button("beIN SPORTS AFC 1"):
        st.video("https://www.youtube.com/watch?v=Xn7KWR9EOGQ") # Link-gaaga halkan ku dheji

with tab_scores:
    st.write("Natiijooyinka")

with tab_jadwal:
    st.write("Jadwalka")
