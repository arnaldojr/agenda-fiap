import arquivo.validacao as validacao

def adicionar_contato(agenda,nome,tel,email,end):
    """Adiciona um novo contato à agenda."""
    if not validacao.validar_telefone(tel):
        return False
    if not validacao.validar_email(email):
        return False

    novo_contato = {}
    novo_contato["telefone"] = tel
    novo_contato["email"] = email
    novo_contato["endereço"] = end
    agenda[nome]= novo_contato
    return True

def ordenar_agenda_por_nome(agenda):
    """Retorna uma cópia da agenda ordenada por nome."""
    return dict(sorted(agenda.items()))

def imprimir_contato(nome, contato):
    """Imprime as informações de um contato de forma formatada."""
    print(f"Nome: {nome}")
    for tipo, valor in contato.items():
        print(f"{tipo.capitalize()}: {valor}")
    print("-" * 30)  # Linha de separação entre contatos

def listar_contato(agenda):
    """Lista todos os contatos na agenda, ordenados por nome."""
    contatos_ordenados = ordenar_agenda_por_nome(agenda)
    quantidade_contatos = len(contatos_ordenados)
    print(f"agenda possui {quantidade_contatos} contatos.")
    for nome, contato in contatos_ordenados.items():
        imprimir_contato(nome, contato)

def editar_contato(agenda,nome,tel,email,end):
    """Edita um contato existente na agenda."""
    if not validacao.validar_telefone(tel):
        return False
    if not validacao.validar_email(email):
        return False
    
    novo_contato = {}
    novo_contato["telefone"] = tel
    novo_contato["email"] = email
    novo_contato["endereço"] = end
    
    agenda[nome]= novo_contato
    return True

def excluir_contato(agenda,nome):
    """Exclui um contato existente na agenda."""
    if nome in agenda:
        del agenda[nome]
        return True
    else:
        return False
    # forma 2
    # del agenda.get(nome, "Contato não existe!")

def buscar_contato(agenda, nome):
    """Busca um contato na agenda pelo nome."""
    contato = agenda.get(nome)
    if contato:
        imprimir_contato(nome, contato)

def buscar_contato_avancado(agenda, termo_pesquisa):
    """Busca um contato na agenda por qualquer campo."""
    resultados = []
    for nome, contato in agenda.items():
        if termo_pesquisa.lower() in nome.lower() or \
           any(termo_pesquisa.lower() in valor.lower() for valor in contato.values()):
            resultados.append((nome, contato))
            
    if resultados:
        print("Contatos encontrados:")
        for nome, contato in resultados:
            imprimir_contato(nome, contato)
    else:
        print("Nenhum contato encontrado.")
