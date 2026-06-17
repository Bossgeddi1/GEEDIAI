import streamlit as st

st.set_page_config(page_title="GEEDI SPORTS", layout="centered")

# CSS-ka qurxinta
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    div.stButton > button { 
        width: 100%; height: 50px; background-color: #ffffff; 
        color: #ff6600; font-weight: bold; border-radius: 8px; border: 2px solid #ff6600;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ GEEDI SPORTS")

# Badhamada Tooska ah
channels = {
    "beIN SPORTS 1": "https://www.youtube.com/embed/live_stream?channel=UC4477474747",
    "beIN SPORTS 2": "https://www.youtube.com/embed/live_stream?channel=UC5588383838"
}

st.write("Dooro kanaalka aad rabto inaad daawato:")

for name, link in channels.items():
    if st.button(name):
        st.subheader(f"▶️ {name}")
        st.components.v1.iframe(link, height=300, scrolling=False)
