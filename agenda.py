import re
import json

def validar_email(email):
    """Valida o formato do email."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validar_telefone(telefone):
    """Valida o formato do telefone."""
    pattern = r'^\d{2}-\d{8,9}$'
    return re.match(pattern, telefone) is not None

def adicionar_contato(agenda,nome,tel,email,end):
    """Adiciona um novo contato à agenda."""
    if not validar_telefone(tel):
        print("Telefone inválido. O formato correto é 'XX-XXXXXXXXX'.")
        return
    if not validar_email(email):
        print("Email inválido.")
        return

    novo_contato = {}
    novo_contato["telefone"] = tel
    novo_contato["email"] = email
    novo_contato["endereço"] = end
    
    agenda[nome]= novo_contato
    print(f"Contato {nome} adicionado com sucesso!!!")


def listar_contato(agenda):
    """Lista todos os contatos na agenda."""
    print(f"agenda possui {len(agenda)} contatos.")
    for nome, contato in agenda.items():
        print(f"\nNome: {nome}")
        for tipo, valor in contato.items():
            print(f"{tipo} - {valor}")


def editar_contato(agenda,nome,tel,email,end):
    """Edita um contato existente na agenda."""
    if not validar_telefone(tel):
        print("Telefone inválido. O formato correto é 'XX-XXXXXXXXX'.")
        return
    if not validar_email(email):
        print("Email inválido.")
        return
    
    novo_contato = {}
    novo_contato["telefone"] = tel
    novo_contato["email"] = email
    novo_contato["endereço"] = end
    
    agenda[nome]= novo_contato
    print(f"contato {nome} editado com sucesso!!!")

def excluir_contato(agenda,nome):
    """Exclui um contato existente na agenda."""
    if nome in agenda:
        del agenda[nome]
        print(f"contato {nome} excluido com sucesso. :)")
    else:
        print(f"Contato {nome} não existe!")
    # forma 2
    # del agenda.get(nome, "Contato não existe!")

def buscar_contato(agenda, nome):
    """Busca um contato na agenda pelo nome."""
    contato = agenda.get(nome)
    if contato:
        print(f"\nNome: {nome}")
        for tipo, valor in contato.items():
            print(f"{tipo} - {valor}")

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

def menu():
    agenda = carregar_agenda()
    while True:
        print("\n__agenda de contatos__\n")
        print(" 1. - adicionar contato")
        print(" 2. - listar contato")
        print(" 3. - editar contato")
        print(" 4. - excluir contato")
        print(" 5. - buscar contato")
        print(" 6. - sair\n")   
        user_op = input("Escolha uma opção:")

        if user_op == "1":
            user_name = input("Nome do contato:")
            if user_name not in agenda:
                user_tel = input("Tel do contato ('XX-XXXXXXXXX'):")
                user_email = input("email do contato:")
                user_end = input("end do contato:")
                adicionar_contato(agenda,user_name,user_tel,user_email,user_end)
            else:
                print(f"Contato {user_name} já existe!")

        elif user_op == "2":
            listar_contato(agenda)

        elif user_op == "3":
            user_name = input("Nome do contato:")
            if user_name in agenda:
                user_tel = input("Tel do contato (XX-XXXXXXXXX):")
                user_email = input("email do contato:")
                user_end = input("end do contato:")
                editar_contato(agenda,user_name,user_tel,user_email,user_end)
            else:
                print(f"Contato {user_name} não existe!")

        elif user_op == "4":
            user_name = input("Escolha o contato para excluir:")
            excluir_contato(agenda,user_name)

        elif user_op == "5":
            user_name = input("Encontre o contato:")
            buscar_contato(agenda,user_name)

        elif user_op == "6":
            print("Obrigado, fechando o programa!!")
            salvar_agenda(agenda)
            break

        else:
            print(f"opção {user_op} invalida! Escolha uma opção valida.")      


if __name__ == "__main__":
    menu()