# Memorizador
import json
#from script.treinador import Treinador
dados = {}

def salvar_valor(chave, valor):

    # Cria um dicionário para armazenar os valores
    dados[chave] = valor
    return dados

# Salva o dicionário em um arquivo
def salvar_arquivo():
    dados["treinador"] = dados["treinador"].__dict__
    with open("save/memorizador.txt", "w") as arquivo:
        json.dump(dados, arquivo)

# Carrega o dicionário do arquivo
def carregar_arquivo():
    with open("save/memorizador.txt", "r") as arquivo:
        dados = json.load(arquivo)
        dados["treinador"] = Treinador(dados["treinador"]["nome"], dados["treinador"]["pokemons"], dados["treinador"]["experiencia"])
        return dados

if __name__ == "__main__":
    for i in range(4):
        dados = salvar_valor(i, i)
    print(dados)