
""""
o sistema vai ter as funções

adicionar contato
listar contato
editar contato
excluir contato
buscar contato

a estrutura da agenda será um dicionario de dicionarios para cada contato.


"""
agenda = {
    "pedro":{
        "telefone":"22258-6998",
        "email": "pedro@email.com",
        "endeço": "rua pedro, 123"
    },
    "renato":{
        "telefone":"22258-6998",
        "email": "pedro@email.com",
        "endeço": "rua pedro, 123"
    } 
}

def adicionar_contato():
    pass
def listar_contato():
    pass
def editar_contato():
    pass
def excluir_contato(agenda,nome):
    #forma 1
    if nome in agenda:
        del agenda[nome]
        print(f"contato {nome} excluido com sucesso. :)")
    else:
        print(f"Contato {nome} não existe!")
    # forma 2
    #del agenda.get(nome, "não existe")
    




def buscar_contato():
    pass


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
        print("opção1")
    elif user_op == "2":
        print("opção2")
    elif user_op == "3":
        print("opção3")
    elif user_op == "4":
        user_name = input("Escolha o contato para excluir:")
        excluir_contato(agenda,user_name)



    elif user_op == "5":
        print("opção5")  
    elif user_op == "6":
        print("Obrigado, fechando o programa!!")
        break
    else:
        print(f"opção {user_op} invalida! Escolha uma opção valida.")      