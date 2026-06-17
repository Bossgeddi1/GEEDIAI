import streamlit as st

st.set_page_config(page_title="GEEDIFX - AI Video Generator", layout="centered")
st.title("🎬 Hogaamiye Kontorool - Text to Video")
st.write("Ku beddel sawirkaaga muuqaal ku hadlaya Afsoomaali!")

uploaded_file = st.file_uploader("Gali Sawirka Lagu Hadalsiinayo", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Sawirka aad soo gelisay", width=300)

speech_text = st.text_area("Qoraalka Hadalka", "Aniga waxaan ahay hogaamiye.")
video_format = st.radio("Dooro Qaabka Muuqaalka:", ('Joog (9:16) - Reels/TikTok', 'Jiif (16:9) - YouTube'))

if st.button("🔊 SAWIRKA HADALSII"):
    if not uploaded_file:
        st.error("Fadlan marka hore soo geli sawir!")
    elif not speech_text:
        st.error("Fadlan qor qoraalka uu ku hadlayo sawirku!")
    else:
        st.info("Muuqaalkaaga waxaa lagu dhex diyaarinayaa nidaamka... Fadlan sug.")
        st.success("✅ Habaynta waa diyaar! (Nidaamka isku-xirka API-ga waa diyaar)")
