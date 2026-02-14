# footer.py

import streamlit as st


def load_footer():
    st.markdown("---")
    st.markdown("© 2026 **Chinnakotla Sree Harsha**")
    st.markdown("AI Powered ATS Resume Scanner Platform")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3536/3536505.png", width=30)
        st.markdown("[LinkedIn](https://www.linkedin.com/in/chinnakotla-sree-harsha-85502620b)")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/841/841364.png", width=30)
        st.markdown("[Portfolio](https://myportfolio-i3gd.onrender.com/)")

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/733/733553.png", width=30)
        st.markdown("[GitHub](https://github.com/ChinnakotlaSreeharsha)")

    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/733/733558.png", width=30)
        st.markdown("[Linktree](https://linktr.ee/chinnakotla_sreeharsha)")
