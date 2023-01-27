import csv

with open('pokemon.csv') as f:
    reader = csv.DictReader(f)
    pokedex = {row.pop('Name'): row for row in reader}

def browse_pokemon():
    pass

def get_pokemon_by_name(pokemon):
    return pokedex.get(pokemon)

def get_HP_by_name(pokemon):
    return int(pokedex.get(pokemon)["HP"])
    
def is_legendary(pokemon):
    return pokedex.get(pokemon)["Legendary"] == "True"

def hp_greater_than(threshold):
    return [pokemon for pokemon in pokedex if get_HP_by_name(pokemon) > threshold]

def has_type(pokemon_type):
    return [name for name in pokedex if pokemon_type in [pokedex[name]["Type 1"], pokedex[name]["Type 2"]]]
