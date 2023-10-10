
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
def excluir_contato():
    pass
def buscar_contato():
    pass

print("__agenda de contatos__")
print(" 1. - adicionar contato")
print(" 2. - listar contato")
print(" 3. - editar contato")
print(" 4. - excluir contato")
print(" 5. - buscar contato")
user_op = input("Escolha uma opção:")