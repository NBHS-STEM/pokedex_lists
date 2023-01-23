import csv

with open('pokemon.csv') as f:
    reader = csv.DictReader(f)
    pokedex = {row.pop('Name'): row for row in reader}

def browse_pokemon():
    pass

def get_pokemon_by_name(pokemon):
    pass

def get_HP_by_name(pokemon):
    pass
    
def is_legendary(pokemon):
    pass

def hp_greater_than(threshold):
    pass

def has_type(pokemon_type):
    pass