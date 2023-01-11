# Using Lists to Answer Data Questions

The file `main.py` loads the file `pokemon.csv` as a *list of strings* into a variable called `scuffed_pokedex`. We'd like to manipulate this list a bit in order to more easily answer data-centric questions about Pokémon.

Let's say we'd like to figure out Espeon's HP. We might loop through the list checking to see if the string `Espeon` was in an entry, and then capture that entry. Doing so, we get:

`"196,Espeon,Psychic,,525,65,65,60,130,95,110,2,False"`

But how do we know which value is the one for HP?

And how do we capture *just* that value?

**12/21/22**:

Today we'll be using the `.split()` method in order to process strings like these in order to make individual values accessible via index. Our goal today is to write a function that allows us to enter a Pokémon's name and retrieve its HP. We'll call this function `get_HP_by_name()`.

**1/09/23**:

Today we'll write a function called `get_pokemon_by_name()` that takes a string as an argument and returns the list corresponding to the Pokémon with that name. If the Pokémon is not found, the function should return `None`. 

**1/11/23**:
Today we plan on completing three functions:
- `is_legendary()`: a function that takes a Pokémon name as an argument and returns `True` if the Pokémon is legendary, and `False` otherwise. We'll deal with the case where the input isn't a valid Pokémon later.
- `hp_greater_than()`: a function that returns a list of all Pokémon with HP (strictly) greater than the number passed as an argument. For example, `hp_greater_than(60)` should return a list names for all Pokémon with HP *greater than* 60. It should **not** return any Pokémon with exactly 60 HP.
- `has_type()`: a function that returns a list of all Pokémon names of a given type. For example, `has_type("Ghost")` should return a list of the names of every Ghost type Pokémon.
