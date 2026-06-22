import streamlit as st

st.set_page_config(
    page_title="GEEDI SPORTS",
    layout="wide"
)

st.title("⚽ GEEDI SPORTS LIVE")

st.sidebar.header("Settings")

stream_url = st.sidebar.text_input(
    "Geli Live Stream URL",
    placeholder="https://example.com/live.m3u8"
)

if stream_url:
    st.success("Stream loaded")
    st.video(stream_url)
else:
    st.info("Geli URL sharci ah oo live stream ah.")

st.markdown("---")
st.subheader("Sports News")

news = [
    "Wararka ciyaaraha halkan ku soo bandhig.",
    "Jadwalka ciyaaraha maanta.",
    "Natiijooyinka ugu dambeeyay."
]

for item in news:
    st.write("•", item)
