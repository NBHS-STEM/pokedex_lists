with open('pokemon.csv') as f:
    pokedex = [line.rstrip().split(",") for line in f]

def browse_pokemon():
    for pokemon in pokedex[1:]:
        if input("Press enter to see the next Pokemon or q to quit:").lower() == 'q':
            break
        else:
            print(pokemon)

def get_pokemon_by_name(pokemon):
    for entry in pokedex[1:]:
        if entry[1] == pokemon:
            return entry
    # explicit is better than implicit!
    return None

def is_legendary(pokemon):
    pass

def hp_greater_than(threshold):
    pass

def has_type(pokemon_type):
    pass