import sqlite3
from sqlite3 import Error

class Veiculos():
    def __init__(self, app):
        self.app = app

    def InserirVeiculos(self, idVeiculo, marca, modelo, placa, tipoCombustivel, precoVeiculo):
        try:
            self.app.cursor.execute("insert into veiculos(idVeiculo, marca, modelo, placa, tipoCombustivel, precoVeiculo) values(?, ?, ?, ?, ?, ?)", (idVeiculo, marca, modelo, placa, tipoCombustivel, precoVeiculo))
            self.app.conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao cadastar veículo", e)
        
    def MostrarVeiculos(self):
        self.app.cursor.execute("select * from veiculos")
        veiculos = self.app.cursor.fetchall()
        for veiculo in veiculos:
            print("\nId: %d\nMarca: %s\nModelo: %s\nPlaca: %s\nTipo de Combustível: %s\nPreço %f" %veiculo)
    
    def DeletarVeiculos(self, idVeiculo):
        try:
            self.app.cursor.execute("delete from veiculos where idVeiculo = ?", (idVeiculo, ))
            self.app.conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao deletar veículo", e)