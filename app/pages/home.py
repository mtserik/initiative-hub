import streamlit as st
from app.services.campaign_repository import list_campaigns_by_user

st.header('Home')
st.caption('Validação inicial de campanhas')

st.divider()

# UUID MOCK
USER_ID = '11111111-1111-1111-1111-111111111111'

campaigns = list_campaigns_by_user(USER_ID)

if not campaigns:
    st.info('Nenhuma campanha encontrada.')
else:
    st.subheader('🎲 Minhas campanhas')
    
    for campaign in campaigns:
        with st.container(border=True):
            st.markdown(f"### {campaign['name']}")
            st.write(campaign['description'] or '_Sem descrição_')
            
            cols = st.columns(3)
            cols[0].markdown(f"**Sistema:** {campaign['system_key']}")
            cols[1].markdown(f"**Papel:** {campaign['role']}")
            cols[2].markdown(
                f"**Criada em:** {campaign['created_at'].strftime('%d/%m/%Y')}"
            )