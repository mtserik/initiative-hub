import streamlit as st
from services.campaign_repository import list_campaigns_by_user

st.header("🏠 Home")

user = st.session_state.get("user")

if not user:
    st.warning("Você precisa estar logado para acessar esta página.")
    st.stop()

campaigns = list_campaigns_by_user(user["id"])

st.subheader("🎲 Minhas campanhas")

if not campaigns:
    st.info("Nenhuma campanha encontrada.")
else:
    for campaign in campaigns:
        with st.container(border=True):
            st.markdown(f"### {campaign['name']}")
            st.write(campaign["description"] or "_Sem descrição_")

            cols = st.columns(3)
            cols[0].markdown(f"**Sistema:** {campaign['system_key']}")
            cols[1].markdown(f"**Papel:** {campaign['role']}")
            cols[2].markdown(
                f"**Criada em:** {campaign['created_at'].strftime('%d/%m/%Y')}"
            )
