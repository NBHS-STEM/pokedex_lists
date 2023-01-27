import csv

with open('pokemon.csv') as f:
    reader = csv.DictReader(f)
    pokedex = {row.pop('Name'): row for row in reader}

def print_pokemon(pokemon):
    print(30 * "*")
    print(f"{pokemon:^30}")
    print(30 * "*")
    for stat, value in get_pokemon_by_name(pokemon).items():
        print(f"{stat:<15}{value:>15}")
        
def browse_pokemon():
    for pokemon in pokedex:
        if input("Press enter to see the next Pokemon or q to quit:").lower() == 'q':
            break
        else:
            print_pokemon(pokemon)

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

<<<<<<< HEAD
=======
def print_pokemon(pokemon):
    print(30 * "*")
    print(f"{pokemon:^30}")
    print(30 * "*")
    for stat, value in get_pokemon_by_name(pokemon).items():
        print(f"{stat:<15}{value:>15}")
>>>>>>> 621b2c2120c4e1fe5c350ea1e4575411c504146d
