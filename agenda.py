import contatos
import arquivo

def menu():
    agenda = arquivo.carregar_agenda()
    while True:
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
        
        user_op = input("Escolha uma opção:")

        if user_op == "1":
            user_name = input("Nome do contato:")
            if user_name not in agenda:
                user_tel = input("Tel do contato ('XX-XXXXXXXXX'):")
                user_email = input("email do contato:")
                user_end = input("end do contato:")
                if contatos.adicionar_contato(agenda,user_name,user_tel,user_email,user_end):
                    print(f"Contato {user_name} adicionado com sucesso!!!")
                else:
                    print("Falha ao adicionar contato. Verifique os dados e tente novamente.")
            else:
                print(f"Contato {user_name} já existe!")

        elif user_op == "2":
            contatos.listar_contato(agenda)

        elif user_op == "3":
            user_name = input("Nome do contato:")
            if user_name in agenda:
                user_tel = input("Tel do contato (XX-XXXXXXXXX):")
                user_email = input("email do contato:")
                user_end = input("end do contato:")
                if contatos.editar_contato(agenda,user_name,user_tel,user_email,user_end):
                    print(f"Contato {user_name} editado com sucesso!!!")
                else:
                    print("Falha ao editar contato. Verifique os dados e tente novamente.")

            else:
                print(f"Contato {user_name} não existe!")

        elif user_op == "4":
            user_name = input("Escolha o contato para excluir:")
            contatos.excluir_contato(agenda,user_name)

        elif user_op == "5":
            user_name = input("Encontre o contato:")
            if contatos.buscar_contato(agenda,user_name):
                print(f"Contato {user_name} excluído com sucesso. :)")
            else:
                print(f"Contato {user_name} não existe!")
                        
        elif user_op == "6":
            user_name = input("buca por nome, teleforne, email")
            contatos.buscar_contato_avancado(agenda,user_name)

        elif user_op == "7":
            nome_arquivo = input("Nome do arquivo para exportar os contatos: ")
            arquivo.exportar_contatos(agenda, nome_arquivo)

        elif user_op == "8":
            nome_arquivo = input("Nome do arquivo para importar os contatos: ")
            arquivo.importar_contatos(agenda, nome_arquivo)

        elif user_op == "9":
            salvar = input("Deseja salvar as alterações antes de sair? (s/n): ")
            if salvar.lower() == 's':
                arquivo.salvar_agenda(agenda)
            print("Obrigado, fechando o programa!!")
            break
        

        else:
            print(f"opção {user_op} invalida! Escolha uma opção valida.")      


if __name__ == "__main__":
    menu()