from flask import Flask, jsonify
from flask_cors import CORS
import json
import os
from dbconfig import Gerenciador
from usuario import Usuario
from alugados import Alugados
from veiculos import Veiculos

app = Gerenciador()
app.criarTabelas()  
usuario = Usuario(app)
alugados = Alugados(app)
veiculos = Veiculos(app)

def menu_locadora():
    print("Menu de opções")
    print("1 - Inserir dados do aluguel")
    print("2 - Mostrar os dados do aluguel")
    print("3 - Apagar dados do aluguel")
    print("---------------------------------")
    print("4 - Inserir dados do Usuário")
    print("5 - Mostrar os dados do Usuário")
    print("6 - Apagar dados do Usuário")
    print("---------------------------------")
    print("7 - Inserir dados dos Veículos")
    print("8 - Mostrar os dados dos Veículos")
    print("9 - Apagar dados dos Veículos")
    print("---------------------------------")
    print("10 - Saindo")



while True:
        menu_locadora()
        opcao = int(input("Escolha umx a opção:"))

        if opcao == 1:
            dataInicio = input("Digite a data do inicio do aluguel: ")
            dataFim = input("Digite a data do fim do aluguel: ")
            precoFinal = input("Digite o preco do aluguel: ")
            cpf = input("Digite o cpf de quem está alugando: ")
            idVeiculo = input("Digite o id do veiculo alugado: ")
            alugados.InserirDadosAlugados(dataInicio, dataFim, precoFinal, cpf, idVeiculo)
        
        elif opcao == 2:
            alugados.mostrarDadosAlugados()

        elif opcao == 3:
            cpf = input("Digite o cpf registrado do dado que será apagado: ")
            alugados.apagarDadosAlugados(cpf)

        elif opcao == 4:
            cpf = input("Digite o CPF:")
            nome = input("Digite o nome:")
            email = input("Digite o e-mail:")
            dataNasc = input("Digite a data de nascimento: (com traços)")
            usuario.InserirUsuario(cpf, nome, email, dataNasc)
        
        elif opcao == 5:
            usuario.MostrarTodosUsuarios()

        elif opcao == 6:
            cpf = input("Digite o CPF do usuário que deseja deletar:")
            usuario.DeletarUsuario(cpf)

        elif opcao == 7:
            idVeiculo = int(input("Digite o Id do veículo:"))
            marca = input("Digite a marca do veículo:") 
            modelo = input("Digite o modelo do veículo:") 
            placa = input("Digite a placa do veículo:") 
            tipoCombustivel = input("Digite o tipo de combustível usado") 
            precoVeiculo = float(input("Digite o preço do aluguel do veículo"))
            veiculos.InserirVeiculos(idVeiculo, marca, modelo, placa, tipoCombustivel, precoVeiculo)

        elif opcao == 8:
            veiculos.MostrarVeiculos()

        elif opcao == 9:
            idVeiculo = int(input("Digite o Id do veículo que deseja deletar"))
            veiculos.DeletarVeiculos(idVeiculo)

        elif opcao == 10:
            print("Saindo..")
            break

        else:
            print("Opção invalida. Tente novamente")

app.fechar()



# Rotas do Flask e leitura dos arquivos json
server = Flask(__name__)
CORS(server)  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@server.route('/usuarios', methods=['GET'])
def get_usuarios():
    file_path = os.path.join(BASE_DIR, 'usuarios.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo usuarios.json não encontrado"}), 404

@server.route('/carros', methods=['GET'])
def get_carros():
    file_path = os.path.join(BASE_DIR, 'veiculos.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo veiculos.json não encontrado"}), 404

@server.route('/alugados', methods=['GET'])
def get_alugados():
    file_path = os.path.join(BASE_DIR, 'alugados.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo alugados.json não encontrado"}), 404

if __name__ == '__main__':
    server.run(debug=True)
