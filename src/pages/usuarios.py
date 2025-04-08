import home
from modules.Usuario import UsuarioRepository
import util
import os
from util import clear_screen

rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns)
title = "SISTEMA DE VENDAS"
padding = (columns - len(title) - 2) // 2

def display_menu():
    conn_str = util.str_conn
    repo = UsuarioRepository(conn_str)

    while True:
        print("+" + "-" * (columns - 2) + "+")
        print("| MENU DE OPÇÕES")
        print("+" + "-" * (columns - 2) + "+")
        print("| 1. Criar Usuário")
        print("| 2. Buscar por ID")
        print("| 3. Buscar por Email")
        print("| 4. Atualizar Usuário")
        print("| 5. Deletar Usuário")
        print("| 6. Listar Usuários")
        print("| 7. Sair")
        print("+" + "-" * (columns - 2) + "+")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            util.clear_screen()
            print("+" + "-" * (columns - 2) + "+")
            print("| CRIAR USUÁRIO")
            print("+" + "-" * (columns - 2) + "+")
            nome = input("| Nome: ")
            email = input("| Email: ")
            senha = input("| Senha: ")
            print("+" + "-" * (columns - 2) + "+")
            usuario = repo.criar_usuario(nome, email, senha)
            print("Usuário criado:", usuario.__dict__)
            print("+" + "-" * (columns - 2) + "+")
            print("Pressione Enter para continuar...")
            input()
            util.clear_screen()

        elif escolha == "2":
            id = int(input("ID do usuário: "))
            usuario = repo.buscar_usuario_por_id(id)
            print(usuario if usuario else "Usuário não encontrado.")

        elif escolha == "3":
            email = input("Email: ")
            usuario = repo.buscar_usuario_por_email(email)
            print(usuario if usuario else "Usuário não encontrado.")

        elif escolha == "4":
            id = int(input("ID do usuário a atualizar: "))
            nome = input("Novo nome (pressione Enter para manter): ")
            email = input("Novo email (pressione Enter para manter): ")
            senha = input("Nova senha (pressione Enter para manter): ")
            sucesso = repo.atualizar_usuario(id, nome or None, email or None, senha or None)
            print("Atualizado com sucesso!" if sucesso else "Falha na atualização.")

        elif escolha == "5":
            id = int(input("ID do usuário a deletar: "))
            sucesso = repo.deletar_usuario(id)
            print("Deletado com sucesso!" if sucesso else "Usuário não encontrado.")

        elif escolha == "6":
            lista = repo.listar_usuario()
            print(lista if lista else "Usuário não encontrado.")

        elif escolha == "7":
            home.display_menu()
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    display_menu()