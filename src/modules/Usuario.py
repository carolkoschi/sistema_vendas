from datetime import datetime
from typing import Optional
import pyodbc

class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str, data_cadastro: datetime):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_cadastro = data_cadastro


class UsuarioRepository:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def _get_connection(self):
        return pyodbc.connect(self.connection_string)

    def criar_usuario(self, nome: str, email: str, senha: str) -> Usuario:
        query = """
        INSERT INTO usuarios (nome, email, senha, dataCadastro)
        OUTPUT INSERTED.id, INSERTED.nome, INSERTED.email, INSERTED.senha, INSERTED.dataCadastro
        VALUES (?, ?, ?, DEFAULT)
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nome, email, senha))
            row = cursor.fetchone()
            return Usuario(*row)

    def buscar_usuario_por_id(self, id: int) -> Optional[Usuario]:
        query = "SELECT id, nome, email, senha, dataCadastro FROM usuarios WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            return Usuario(*row) if row else None
        
    def listar_usuario(self) -> Optional[Usuario]:
        query = "SELECT id, nome, email, senha, dataCadastro FROM usuarios ORDER BY nome"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            return Usuario(*row) if row else None

    def buscar_usuario_por_email(self, email: str) -> Optional[Usuario]:
        query = "SELECT id, nome, email, senha, dataCadastro FROM usuarios WHERE email = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            return Usuario(*row) if row else None

    def atualizar_usuario(self, id: int, nome: Optional[str] = None, email: Optional[str] = None, senha: Optional[str] = None) -> bool:
        updates = []
        params = []
        if nome:
            updates.append("nome = ?")
            params.append(nome)
        if email:
            updates.append("email = ?")
            params.append(email)
        if senha:
            updates.append("senha = ?")
            params.append(senha)
        params.append(id)

        if not updates:
            return False

        query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.rowcount > 0

    def deletar_usuario(self, id: int) -> bool:
        query = "DELETE FROM usuarios WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            return cursor.rowcount > 0