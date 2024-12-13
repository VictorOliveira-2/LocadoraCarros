import sqlite3

class Alugados():
    def __init__(self, app):
        self.app = app

    def InserirDadosAlugados(self, dataInicio, dataFim, precoFinal, cpf, idVeiculo):
        self.app.cursor.execute("insert into alugados(dataInicio, dataFim, precoFinal, cpf, idVeiculo) values (?, ?, ?, ?, ?)",(dataInicio, dataFim, precoFinal, cpf, idVeiculo))
        self.app.conexao.commit()

    def mostrarDadosAlugados(self):
        self.app.cursor.execute("select * from alugados")
        alugados = self.app.cursor.fetchall()
        for alugados in alugados:
            print("\nData Inicio do aluguel: %s\nData fim do aluguel: %s\nPreço final: %f\nCPF registrado: %s\nID do Veículo Alugado: %d" % alugados)

    def apagarDadosAlugados(self, cpf):
        self.app.cursor.execute("delete from alugados where cpf = ?", (cpf,))
        self.app.conexao.commit()