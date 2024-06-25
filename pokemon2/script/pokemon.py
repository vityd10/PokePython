# Pokemons
import json

# Classe Pokemon
class Pokemon:
    def __init__(self, nome, tipo, taxa_de_captura, raridade):
        self.nome = nome
        self.tipo = tipo
        self.taxa_de_captura = taxa_de_captura
        self.raridade = raridade

# Construir pokemon
def construir_pokemon(pokemon):
    with open("data/pokemon_lista.json", "r", encoding="utf-8") as f:
        pokemon_data = json.load(f)
        pokemon_data = pokemon_data["pokemons"]
        # Procurar em pokemon_data["nomes"] pelo valor igual pokemon
        for entry in pokemon_data:
            if entry["nome"] == pokemon:
                return Pokemon(entry["nome"], entry["tipo"], entry["taxa_de_captura"], entry["raridade"])


