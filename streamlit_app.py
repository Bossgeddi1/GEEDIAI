import streamlit as st
import requests
import base64
import time
import json

# 1. Dejinta Class-ka Yacine
class YacineTV:
    def __init__(self):
        self.api_url = "http://ver3.yacinelive.com"
        self.key = "c!xZj+N9&G@Ev@vw"

    def decrypt(self, enc, key):
        enc = base64.b64decode(enc.encode("ascii")).decode("ascii")
        result = ""
        for i in range(len(enc)):
            result = result + chr(ord(enc[i]) ^ ord(key[i % len(key)]))
        return result

    def req(self, path):
        try:
            r = requests.get(self.api_url + path, timeout=10)
            timestamp = r.headers.get("t", str(int(time.time())))
            return json.loads(self.decrypt(r.text, key=self.key + timestamp))
        except:
            return {"success": False}

    def get_categories(self):
        return self.req("/api/categories")

# 2. Naqshadda App-ka
st.set_page_config(page_title="GEEDI SPORTS", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ffffff; color: #cc0000; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ GEEDI SPORTS")

# 3. Bilowga App-ka
yacine = YacineTV()
categories = yacine.get_categories()

if categories and categories.get("success"):
    st.write("Dooro qaybta aad rabto:")
    for cat in categories['data']:
        if st.button(cat['name']):
            st.success(f"Waxaad dooratay: {cat['name']}")
            # Halkan ku dar xiriirka channels-ka haddii loo baahdo
else:
    st.error("Khalad ayaa dhacay! Fadlan dib u soo celi bogga.")
