with open('pokemon.csv') as f:
    scuffed_pokedex = [line.rstrip() for line in f]

def browse_pokemon():
    for pokemon in scuffed_pokedex[1:]:
        if input("Press enter to see the next Pokemon or q to quit:").lower() == 'q':
            break
        else:
            print(pokemon)
        