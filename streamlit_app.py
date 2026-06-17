import streamlit as st

# ... (Qaybta 1, 2, iyo 3 ee koodhkaaga waa sidii hore) ...

# Qaybta tab_tv (Qaybta LIVE TV)
with tab_tv:
    st.markdown("<br>", unsafe_allow_html=True)
    
    for name, link in channels.items():
        if st.button(name):
            st.markdown(f"<p style='text-align: center; color: #ff6600;'>▶️ Hadda waxaa kuu furmaaya: {name}</p>", unsafe_allow_html=True)
            
            # HABKA HAWLGELINTA VIDEO-GA EE CASRIGA AH
            # Waxaan u isticmaalaynaa 'iframe' si uu u qaado format kasta oo IPTV ah
            video_html = f"""
            <video width="100%" height="300" controls autoplay>
                <source src="{link}" type="application/x-mpegURL">
                Your browser does not support the video tag.
            </video>
            """
            st.components.v1.html(video_html, height=320)
            st.write("---")
