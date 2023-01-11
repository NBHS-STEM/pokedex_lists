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

def get_HP_by_name(pokemon):
    return get_pokemon_by_name(pokemon)[5]
    
def is_legendary(pokemon):
    return get_pokemon_by_name(pokemon)[-1] == "True"

def hp_greater_than(threshold):
    """
    Alternate version without listcomp:

    results = []
    for entry in pokedex[1:]:
        if int(entry[5]) > threshold:
            results.append(entry[1])
    return results
    """
    return [entry[1] for entry in pokedex[1:] if int(entry[5]) > threshold]

def has_type(pokemon_type):
    """
    Alternate version without listcomp:

    results = []
    for entry in pokedex[1:]:
        if pokemon_type in entry[2:4]:
            results.append(entry[1])
    return results
    """
    return [entry[1] for entry in pokedex[1:] if pokemon_type in entry[2:4]]
