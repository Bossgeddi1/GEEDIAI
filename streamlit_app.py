import streamlit as st
import requests
import base64
import time
import json

# [Dhex geli halkan Class-ka YacineTV ee aad soo dirtay]
class YacineTV:
    # ... (Koodhkii aad soo dirtay oo dhan halkan geli) ...

# 1. Bilowga App-ka
st.set_page_config(page_title="GEEDI SPORTS API", layout="centered")
yacine = YacineTV()

# 2. Soo saarista Channels-ka (Halkii aad gacanta u qori lahayd links-ka)
categories = yacine.get_categories()

if categories.get("success"):
    st.write("Dooro Category:")
    cat_id = st.selectbox("Categories", [c['id'] for c in categories['data']])
    
    # Soo saar channels-ka qaybtaas
    channels = yacine.get_category_channels(cat_id)
    if channels.get("success"):
        for ch in channels['data']:
            if st.button(ch['name']):
                # Halkan geli logic-ga video-ga
                st.write(f"Waxaad dooratay: {ch['name']}")
else:
    st.error("Xogta lagama soo saari karo API-ga Yacine TV.")
