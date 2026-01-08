import streamlit as st
from services.supabase_client import supabase

st.header("🔐 Login")

with st.form("login"):
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")
    submit = st.form_submit_button("Entrar")

if submit:
    try:
        res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if res.user:
            st.session_state["user"] = {
                "id": res.user.id,
                "email": res.user.email
            }
            st.rerun()  # 🔑 deixa o main decidir

    except Exception:
        st.error("Falha no login")
