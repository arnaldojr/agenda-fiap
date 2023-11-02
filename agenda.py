from contatos import contatos
from arquivo import arquivo

def obter_entrada(prompt):
    """Trata o input do usuario"""
    resposta = input(prompt).strip()
    return resposta if resposta != "" else None

def opcoes():
    """Exibe as opções do menu"""
    print("\n__agenda de contatos__\n")
    print("1. - adicionar contato")
    print("2. - listar contato")
    print("3. - editar contato")
    print("4. - excluir contato")
    print("5. - buscar contato")
    print("6. - Busca avançada")   
    print("7. - Exportar contatos")
    print("8. - Importar contatos")
    print("9. - sair\n")  


def menu():
    agenda = arquivo.carregar_agenda()
    while True:
        opcoes()
        user_op = obter_entrada("Escolha uma opção:")

        if user_op == "1":
            user_name = obter_entrada("Nome do contato:")
            if user_name not in agenda:
                user_tel = obter_entrada("Tel do contato ('XX-XXXXXXXXX'):")
                user_email = obter_entrada("email do contato:")
                user_end = obter_entrada("end do contato:")
                if contatos.adicionar_contato(agenda,user_name,user_tel,user_email,user_end):
                    print(f"Contato {user_name} adicionado com sucesso!!!")
                else:
                    print("Falha ao adicionar contato. Verifique os dados e tente novamente.")
            else:
                print(f"Contato {user_name} já existe!")

        elif user_op == "2":
            contatos.listar_contato(agenda)

        elif user_op == "3":
            user_name = obter_entrada("Nome do contato:")
            if user_name in agenda:
                user_tel = obter_entrada("Tel do contato (XX-XXXXXXXXX):")
                user_email = obter_entrada("email do contato:")
                user_end = obter_entrada("end do contato:")
                if contatos.editar_contato(agenda,user_name,user_tel,user_email,user_end):
                    print(f"Contato {user_name} editado com sucesso!!!")
                else:
                    print("Falha ao editar contato. Verifique os dados e tente novamente.")

            else:
                print(f"Contato {user_name} não existe!")

        elif user_op == "4":
            user_name = obter_entrada("Escolha o contato para excluir:")
            contatos.excluir_contato(agenda,user_name)

        elif user_op == "5":
            user_name = obter_entrada("Encontre o contato:")
            if contatos.buscar_contato(agenda,user_name):
                print(f"Contato {user_name} excluído com sucesso. :)")
            else:
                print(f"Contato {user_name} não existe!")
                        
        elif user_op == "6":
            user_name = obter_entrada("buca por nome, teleforne, email")
            contatos.buscar_contato_avancado(agenda,user_name)

        elif user_op == "7":
            nome_arquivo = obter_entrada("Nome do arquivo para exportar os contatos: ")
            arquivo.exportar_contatos(agenda, nome_arquivo)

        elif user_op == "8":
            nome_arquivo = obter_entrada("Nome do arquivo para importar os contatos: ")
            arquivo.importar_contatos(agenda, nome_arquivo)

        elif user_op == "9":
            salvar = obter_entrada("Deseja salvar as alterações antes de sair? (s/n): ")
            if salvar.lower() == 's':
                arquivo.salvar_agenda(agenda)
            print("Obrigado, fechando o programa!!")
            break
        else:
            print(f"opção {user_op} invalida! Escolha uma opção valida.")      


if __name__ == "__main__":
    menu()