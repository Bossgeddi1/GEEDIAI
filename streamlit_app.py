with tab_tv:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e;'>Guji kanaalka aad rabto inaad daawato:</p>", unsafe_allow_html=True)
    
    # Liiska kanaalada oo leh link-yo toos ah oo Embed ah
    channels = {
        "beIN SPORTS 1": "https://www.youtube.com/embed/live_stream?channel=UC5588383838", # Ku beddel link-gaaga halkan
        "beIN SPORTS 2": "https://www.youtube.com/embed/live_stream?channel=UC4477474747"
    }

    for name, link in channels.items():
        if st.button(f"📺 {name}"):
            st.markdown(f"<p style='color: #ff6600; font-weight: bold; text-align: center;'>▶️ Hadda Waxaa kuu furmaaya: {name}</p>", unsafe_allow_html=True)
            
            # ISTICMAALKA EMBED (IFRAME)
            st.components.v1.iframe(link, height=300, scrolling=False)
            st.write("---")
