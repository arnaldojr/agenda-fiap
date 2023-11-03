import streamlit as st
from arquivo import arquivo
from streamlit_util import mostrar_home, listar_contatos, adicionar_novo_contato, pesquisar_contato

# cabeçalho da pagina
st.set_page_config(page_title='Agenda de contatos', page_icon=':book',layout="wide", initial_sidebar_state='expanded')

# opções de emoji https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

### menu lateral de opções
# Using object notation
opcoes_menu = ['Home', 'Listar Contatos', 'Adicionar Contato', 'Pesquisar Contato']

# Barra lateral para navegação
escolha = st.sidebar.selectbox('Opções da Agenda:', opcoes_menu)

# Carrega a agenda 
agenda = arquivo.carregar_agenda()

# Rotas do menu
if escolha == "Home":
    mostrar_home()
elif escolha == 'Listar Contatos':
    listar_contatos(agenda)
elif escolha == 'Adicionar Contato':
    adicionar_novo_contato(agenda)
elif escolha == 'Pesquisar Contato':
    pesquisar_contato(agenda)

