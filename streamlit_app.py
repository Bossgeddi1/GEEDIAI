import streamlit as st
import requests
import base64
import time
import json

# CLASS-KA YACINE TV (Hubi in dhammaan function-yada ay leeyihiin space-ka saxda ah)
class YacineTV:
    api_url = "http://ver3.yacinelive.com"
    key = "c!xZj+N9&G@Ev@vw"

    def decrypt(self, enc, key=key):
        enc = base64.b64decode(enc.encode("ascii")).decode("ascii")
        result = ""
        for i in range(len(enc)):
            result = result + chr(ord(enc[i]) ^ ord(key[i % len(key)]))
        return result

    def req(self, path):
        r = requests.get(self.api_url + path)
        timestamp = str(int(time.time()))
        if "t" in r.headers:
            timestamp = r.headers["t"]
        try:
            return json.loads(self.decrypt(r.text, key=self.key + timestamp))
        except Exception:
            return {"success": False, "error": "can't parse json."}

# Halkan ka bilow koodhka Streamlit (Waa inay la siman yihiin bilowga xariiqda)
st.set_page_config(page_title="GEEDI SPORTS API", layout="centered")

st.title("⚽ GEEDI SPORTS API")
yacine = YacineTV()

categories = yacine.get_categories()
if categories.get("success"):
    st.write("Dooro Category:")
    cat_id = st.selectbox("Categories", [c['id'] for c in categories['data']])
    
    channels = yacine.get_category_channels(cat_id)
    if channels.get("success"):
        for ch in channels['data']:
            if st.button(ch['name']):
                st.write(f"Waxaad dooratay: {ch['name']}")
else:
    st.error("Xogta lagama soo saari karo API-ga Yacine TV.")
