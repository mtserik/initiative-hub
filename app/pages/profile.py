import streamlit as st
from services.supabase_client import supabase

st.header("👤 Perfil")

user = st.session_state.get("user")
if not user:
    st.stop()

st.write(f"Email: {user['email']}")

if st.button("🚪 Logout"):
    supabase.auth.sign_out()
    st.session_state.clear()
    st.rerun()  # 🔑 NÃO usa switch_page
