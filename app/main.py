import streamlit as st

st.set_page_config(
    page_title="Initiative Hub",
    layout="wide"
)

user = st.session_state.get("user")

# ============================
# NÃO AUTENTICADO → Login
# ============================
if not user:
    nav = st.navigation(
        [st.Page("pages/login.py", title="Login")],
        position="top"
    )
    nav.run()
    st.stop()

# ============================
# AUTENTICADO → App
# ============================
nav = st.navigation(
    [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/campaigns.py", title="Campanhas"),
        st.Page("pages/characters.py", title="Personagens"),
        st.Page("pages/profile.py", title="Perfil"),
    ],
    position="top"
)

nav.run()
