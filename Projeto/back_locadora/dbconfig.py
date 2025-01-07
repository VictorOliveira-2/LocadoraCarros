import sqlite3
import os


class Gerenciador:
    def __init__(self):
        self.conexao = sqlite3.connect("locadoraVeiculos.db")
        self.cursor = self.conexao.cursor()
    

    def criarTabelas(self):
       
        self.cursor.execute('''
        create table if not exists usuarios(
        cpf text primary key, 
        nome text, 
        email text, 
        dataNasc text);''')

        #Veiculos:
        self.cursor.execute('''
        create table if not exists veiculos(
        idVeiculo integer primary key, 
        marca text, modelo text, 
        placa text, 
        tipoCombustivel text, 
        precoVeiculo decimal);''')

        #Alugados:
        self.cursor.execute('''
        create table if not exists alugados(
        dataInicio text,
        dataFim text, 
        precoFinal decimal,
        cpf text,
        idVeiculo integer,
        foreign key (cpf) references usuarios(cpf),
        foreign key (idVeiculo) references veiculos(idVeiculo)
        );''')

        self.conexao.commit()

    def fechar (self):
        self.conexao.close()