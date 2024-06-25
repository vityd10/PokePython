# Treinador
import json
import random

# Função para criar um treinador
class Treinador:
    def __init__(self, nome, pokemons = [], experiencia = 0):
        self.nome = nome
        self.pokemons = []
        self.experiencia = 0
        self.local = None

    def __str__(self):
        pokemons = []
        for pokemon in self.pokemons:
            pokemons.append(pokemon.nome)

        return f"Nome: {self.nome}\nPokemons: {pokemons}\nExperiência: {self.experiencia}"

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def add_experiencia(self, experiencia):
        self.experiencia += experiencia

        
    

# Função para criar um novo treinador
def novo_treinador():
    print("Você está criando um novo treinador!")
    nome = input("Nome do treinador: ")
    treinador = Treinador(nome)
    print(treinador)
    print("Treinador criado com sucesso!")
    return treinador

def capturar_pokemon(treinador, pokemon):
    chance = random.random()
    if chance <= pokemon.taxa_de_captura:
        treinador.add_pokemon(pokemon)
        return [True, pokemon.nome]
    else:
        return [False, pokemon.nome]


