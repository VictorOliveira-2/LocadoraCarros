import sqlite3
from sqlite3 import Error

class Usuario():

    def __init__(self, app):    
        self.app = app
    
    def InserirUsuario(self, cpf, nome, email, dataNasc):
        try:
            self.app.cursor.execute("insert into usuarios(cpf, nome, email, dataNasc) values (?, ?, ?, ?)", (cpf, nome, email, dataNasc))
            self.app.conexao.commit()
            print("Usuário inserido com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar usuário: ", e)
    
    
    def MostrarTodosUsuarios(self):
        self.app.cursor.execute("select * from usuarios")
        usuarios = self.app.cursor.fetchall()
        for usuario in usuarios:
            print("\nCPF: %s\nNome: %s\nE-mail: %s\nData Nasc: %s" %(usuario))
        
    def DeletarUsuario(self, cpf):
        try:
            self.app.cursor.execute("delete from usuarios where cpf = ?", (cpf, ))
            self.app.conexao.commit()
            print("Usuário deletado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao deletar usuário: ", e)
    
    
        