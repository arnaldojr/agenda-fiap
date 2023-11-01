import json

def salvar_agenda(agenda):
    """Salva a agenda em um arquivo JSON."""
    with open('agenda.json', 'w') as f:
        json.dump(agenda, f)

def carregar_agenda():
    """Carrega a agenda de um arquivo JSON."""
    try:
        with open('agenda.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def exportar_contatos(contatos, nome_arquivo):
    """Exporta os contatos da agenda para um arquivo externo."""
    try:
        nome = nome_arquivo + ".json"
        with open(nome, 'w') as f:
            json.dump(contatos, f)
        print(f"Contatos exportados com sucesso para {nome_arquivo}!")
    except Exception as e:
        print(f"Ocorreu um erro ao exportar os contatos: {e}")

def importar_contatos(agenda, nome_arquivo):
    """Carrega a agenda de um arquivo JSON."""
    try:
        with open(nome_arquivo, 'r') as f:
            contatos_importados = json.load(f)
        agenda.update(contatos_importados)
        print(f"Contatos importados com sucesso de {nome_arquivo}!")
    except Exception as e:
        print(f"Ocorreu um erro ao importar os contatos: {e}")