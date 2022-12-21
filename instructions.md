# Using Lists to Answer Data Questions

The file `main.py` loads the file `pokemon.csv` as a *list of strings* into a variable called `scuffed_pokedex`. We'd like to manipulate this list a bit in order to more easily answer data-centric questions about Pokemon.

Let's say we'd like to figure out Espeon's HP. We might loop through the list checking to see if the string `Espeon` was in an entry, and then capture that entry. Doing so, we get:

`"196,Espeon,Psychic,,525,65,65,60,130,95,110,2,False"`

But how do we know which value is the one for HP?

And how do we capture *just* that value?

**12/21/22**:

Today we'll be using the `.split()` method in order to process strings like these in order to make individual values accessible via index. Our goal today is to write a function that allows us to enter a Pokemon's name and retrieve its HP. We'll call this function `get_HP_by_name()`.

*Update: hi*