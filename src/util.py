import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


str_conn = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=172.17.0.2;DATABASE=sistema_vendas;UID=sa;PWD=@@Error15"