# Handler
from script import menu as m
from script import treinador as t
from script import rotas as r
from script import pokemon as pkm
import json

def menu_principal():
    # Carrega ou cria o Treinador
    treinador = novo_jogo()

    # Abre o lobby inicial
    escolha = processar_lobby(treinador)

# Função para criar um novo jogo
def novo_jogo():
    treinador = m.menu_inicial()
    treinador = check_treinador(treinador)
    return treinador

# Funcão para verificar se o treinador foi criado ou carregado
def check_treinador(treinador):
    match treinador:
        case "New":
            treinador = t.novo_treinador()
            return treinador
        case "Load":
            treinador = carregar_treinador()
            return treinador
        case "Quit":
            exit()
        case _:
            print("Erro: Variável 'treinador' desconhecido.")

# Função para processar o lobby
def processar_lobby(treinador):
    escolha = m.lobby_inicial()
    match escolha:
        case "Rotas":
            processar_rotas(treinador)
        case "Treinador":
            print(treinador)
        case "Salvar":
            salvar_treinador(treinador)
        case "Sair":
            sair_do_jogo(treinador)

    # Retorna para o lobby
    processar_lobby(treinador)

def sair_do_jogo(treinador):
    opcao = m.sair_do_jogo()
    match opcao:
        case "Inicio":
            menu_principal()
            

def processar_rotas(treinador):
    # Carregou os dados da rota
    rotas_data = r.carregar_rotas()

    # Menu para escolher uma rota
    rota_escolhida = m.menu_rotas(rotas_data)

    procurar_pokemon(rota_escolhida, treinador)


def procurar_pokemon(rota, treinador):
    pokemon = r.procurar_pokemons(rota)
    escolha = m.capturar_pokemon(pokemon)
    if escolha == "s":
        pokemon = pkm.construir_pokemon(pokemon)
        capturou = t.capturar_pokemon(treinador, pokemon)
        m.capturou(capturou)
        procurar_pokemon(rota, treinador)
            

# Função para salvar o treinador
def salvar_treinador(treinador_original):
    pokemons_dict = {}
    i = 0
    for pokemon in treinador_original.pokemons:
        pokemon_dict = pokemon.__dict__
        pokemons_dict[i] = pokemon_dict
        i += 1
    print(pokemons_dict)
    save_treinador = {"Nome": treinador_original.nome, "Pokemons": pokemons_dict, "Experiencia": treinador_original.experiencia}
    with open("save/save.json", "w") as arquivo:
        json.dump(save_treinador, arquivo, indent=4)
        
# Função para carregar o treinador:
def carregar_treinador():
    with open("save/save.json", "r") as arquivo:
        treinador = json.load(arquivo)
        n_treinador = t.Treinador(treinador["Nome"], [], treinador["Experiencia"])
        for pokemon in treinador["Pokemons"]:
            n_pokemon = treinador["Pokemons"][pokemon]
            n_pokemon = pkm.Pokemon(n_pokemon["nome"], n_pokemon["tipo"], n_pokemon["taxa_de_captura"], n_pokemon["raridade"])
            n_treinador.add_pokemon(n_pokemon)
        print(n_treinador)
        return n_treinador
