import os
from pages import usuarios
from util import clear_screen

rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns)
title = "SISTEMA DE VENDAS"
padding = (columns - len(title) - 2) // 2

def display_login_page():
    clear_screen()
    print("+" + "-" * (columns - 2) + "+")
    print("|" + " " * (columns - 2) + "|")
    print("|" + " " * padding + title + " " * padding + "|")
    print("|" + " " * (columns - 2) + "|")
    print("+" + "-" * (columns - 2) + "+")
    username = input("| Username: ")
    password = input("| Password: ")
    print("+" + "-" * (columns -2) + "+")
    return username, password

def display_menu():
    clear_screen()
    print("+" + "-" * (columns - 2) + "+")
    print("| MENU DE OPÇÕES")
    print("+" + "-" * (columns - 2) + "+")
    print("| 1. Usuários   ")
    print("| 2. Produtos   ")
    print("| 3. Vendas     ")
    print("| 4. Sair       ")
    print("+" + "-" * (columns - 2) + "+")
    
def display_footer():
    print("+" + "-" * (columns - 2) + "+")

def home():
    username, password = display_login_page()
    if username == "admin" and password == "password":
        clear_screen()
        display_menu()
        choice = input("Escolha uma opção: ")
        if choice == "1":
            clear_screen()
            usuarios.main()
        elif choice == "2":
            clear_screen()
            print("Produtos menu not implemented yet.")
        elif choice == "3":
            clear_screen()
            print("Vendas menu not implemented yet.")
        elif choice == "4":
            clear_screen()
            print("Obrigado...")
        else:
            print("Opção inválida!")
    else:
        print("Invalid credentials. Please try again.")



if __name__ == "__main__":
    home()