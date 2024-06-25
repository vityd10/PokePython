# Rotas
import json
import random

# Função para carregar as rotas
def carregar_rotas():
    with open("data/rotas_lista.json", "r", encoding="utf-8") as f:
        rotas_data = json.load(f)
        return rotas_data["rotas"]

# Função para procurar um pokemon aleatório da rota
def procurar_pokemons(rota_escolhida):
    pokemons = rota_escolhida["pokemons"]
    n = random.randint(1, 10000)
    if n == 1:
        pokemons = pokemons["lendario"]
    elif n <= 11:
        pokemons = pokemons["epico"]
    elif n <= 102:
        pokemons = pokemons["raro"]
    elif n <= 1000:
        pokemons = pokemons["incomum"]
    else:
        pokemons = pokemons["comum"]

    pokemon = random.choice(pokemons)    
    return pokemon