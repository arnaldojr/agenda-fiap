import streamlit as st
from contatos import contatos
from arquivo import arquivo

# Funções auxiliares, para tentar manter o código organizado

def mostrar_home():
    """Mostra a página inicial."""
    st.subheader('Home')
    st.subheader(':red[Agenda de Contatos] :ledger:')
    st.markdown(
        """
        Agenda simples de contatos com interface web. Naveque pelo menu lateral.

        #### Funcionalidades Implementadas (Done!)
        * **Listar Contatos**: Veja todos os seus contatos salvos.
        * **Adicionar Contato**: Adicione novos contatos à sua agenda.
        * **Pesquisar Contato**: Encontre rapidamente os detalhes de um contato específico.
        
        #### Funcionalidades Planejadas (To DO)
        
        * **Editar Contato**: Atualize as informações de um contato existente.
        * **Excluir Contato**: Remova contatos que não são mais necessários.
        * **Categorias de Contatos**: Organize seus contatos em categorias como família, trabalho, etc.
        * **Importar/Exportar**: Faça backup e restaure sua agenda de contatos via CSV ou JSON.
        * **Envio de Mensagens**: Integre com serviços de email ou SMS para enviar mensagens diretamente do aplicativo.
        * **Lembretes de Aniversário**: Receba notificações sobre aniversários e outros eventos importantes.
        * **Interface Multilíngue**: Ofereça suporte a múltiplos idiomas na interface do usuário.
        * **Ordenar Contatos**: Permita que os usuários ordenem a lista de contatos por nome, email ou telefone.
        * **Autenticação de Usuário**: Adicione um sistema de login para proteger os contatos e permitir que vários usuários acessem suas próprias agendas.

        ### Para rodar: 
        
        instalar streamlit: `pip install streamlit`, rodar no terminal:

        ```bash
        streamlit run streamlit_app.py        
        ```
        abrir o navegador em `http://localhost:8501/`


    """)


def listar_contatos(agenda):
    """Lista todos os contatos na agenda."""
    st.subheader('Lista de Contatos :blue_book:')

    if agenda:
        # tentativa1 usando com st.table()
        # st.table(agenda) ## formatação errada
        # st.text(agenda)
        # O metodo st.table() entende o formato lista, para funcionar tem que converter a agenda em uma lista de dicionários para exibição.
        lista_contatos = []
        for nome, info in agenda.items():
            contato = {'Nome': nome}
            contato.update(info)
            lista_contatos.append(contato)
        st.table(lista_contatos)
    else:
        st.write('Nenhum contato encontrado.')

def adicionar_novo_contato(agenda):
    """Adiciona um novo contato à agenda."""
    st.subheader('Adicionar Novo Contato :ledger:')
    with st.form("my_form"):
        nome = st.text_input("Nome do Contato")
        telefone = st.text_input("Telefone do Contato")
        email = st.text_input("E-mail do Contato")
        endereco = st.text_input("Endereço do Contato")
        bot_adicionar = st.form_submit_button("Adicionar Contato")

    if bot_adicionar:
        if nome not in agenda:
            if contatos.adicionar_contato(agenda,nome,telefone,email,endereco):
                arquivo.salvar_agenda(agenda)
                st.success(f"Contato {nome} adicionado com sucesso!")
            else:
                st.error(f"Falha ao adicionar contato. Verifique os dados e tente novamente") 
        else:
            st.error(f"Contato {nome} já existe!")
        st.rerun() # Atualiza a página para mostrar o novo contato


def pesquisar_contato(agenda):
    st.subheader('Pesquisar Contato :mag_right:')
    termo_pesquisa = st.text_input("Digite por alguma informação do contato")

    if termo_pesquisa:
        resultados_pesquisa = []
        for nome, info in agenda.items():
            if termo_pesquisa.lower() in nome.lower() or \
                any(termo_pesquisa.lower() in valor.lower() for valor in info.values()):
            # if nome_pesquisa.lower() in nome.lower():
                resultados_pesquisa.append({'Nome': nome, **info})
        
        if resultados_pesquisa:
            st.table(resultados_pesquisa)
        else:
            st.info('Nenhum contato correspondente encontrado.')
        
