import sqlite3
from sqlite3 import Error

class Alugados():
    def __init__(self, app):
        self.app = app

    def InserirDadosAlugados(self, dataInicio, dataFim, precoFinal, cpf, idVeiculo):
        try:
            self.app.cursor.execute("insert into alugados(dataInicio, dataFim, precoFinal, cpf, idVeiculo) values (?, ?, ?, ?, ?)",(dataInicio, dataFim, precoFinal, cpf, idVeiculo))
            self.app.conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar alugado: ", e)

    def mostrarDadosAlugados(self):
        self.app.cursor.execute("select * from alugados")
        alugados = self.app.cursor.fetchall()
        for alugados in alugados:
            print("\nData Inicio do aluguel: %s\nData fim do aluguel: %s\nPreço final: %f\nCPF registrado: %s\nID do Veículo Alugado: %d" % alugados)

    def apagarDadosAlugados(self, cpf):
        try:
            self.app.cursor.execute("delete from alugados where cpf = ?", (cpf,))
            self.app.conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao deletar usuário", e)