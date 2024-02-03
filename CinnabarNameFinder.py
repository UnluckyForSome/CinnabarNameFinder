import re

# Create the Level List
level_list = {
    " ": 127,
    "A": 128,
    "B": 129,
    "C": 130,
    "D": 131,
    "E": 132,
    "F": 133,
    "G": 134,
    "H": 135,
    "I": 136,
    "J": 137,
    "K": 138,
    "L": 139,
    "M": 140,
    "N": 141,
    "O": 142,
    "P": 143,
    "Q": 144,
    "R": 145,
    "S": 146,
    "T": 147,
    "U": 148,
    "V": 149,
    "W": 150,
    "X": 151,
    "Y": 152,
    "Z": 153,
    "(": 154,
    ")": 155,
    ":": 156,
    ";": 157,
    "[": 158,
    "]": 159,
    "a": 160,
    "b": 161,
    "c": 162,
    "d": 163,
    "e": 164,
    "f": 165,
    "g": 166,
    "h": 167,
    "i": 168,
    "j": 169,
    "k": 170,
    "l": 171,
    "m": 172,
    "n": 173,
    "o": 174,
    "p": 175,
    "q": 176,
    "r": 177,
    "s": 178,
    "t": 179,
    "u": 180,
    "v": 181,
    "w": 182,
    "x": 183,
    "y": 184,
    "z": 185,
    "#": 225,
    "\\": 226,
    "-": 227,
    "?": 230,
    "!": 231,
    "♂": 239,
    "*": 241,
    ".": 242,
    "/": 243,
    ",": 244,
    "♀": 245
}

# Create the Pokemon List
pokemon_list = {
    " ": "MissingNo.",
    "A": "Golduck",
    "B": "Hypno",
    "C": "Golbat",
    "D": "Mewtwo",
    "E": "Snorlax",
    "F": "Magikarp",
    "G": "MissingNo.",
    "H": "MissingNo.",
    "I": "Muk",
    "J": "MissingNo.",
    "K": "Kingler",
    "L": "Cloyster",
    "M": "MissingNo.",
    "N": "Electrode",
    "O": "Clefable",
    "P": "Weezing",
    "Q": "Persian",
    "R": "Marowak",
    "S": "MissingNo.",
    "T": "Haunter",
    "U": "Abra",
    "V": "Alakazam",
    "W": "Pidgeotto",
    "X": "Pidgeot",
    "Y": "Starmie",
    "Z": "Bulbasaur",
    "(": "Venusaur",
    ")": "Tentacruel",
    ":": "MissingNo.",
    ";": "Goldeen",
    "[": "Seaking",
    "]": "MissingNo.",
    "a": "MissingNo.",
    "b": "MissingNo.",
    "c": "MissingNo.",
    "d": "Ponyta",
    "e": "Rapidash",
    "f": "Rattata",
    "g": "Raticate",
    "h": "Nidorino",
    "i": "Nidorina",
    "j": "Geodude",
    "k": "Porygon",
    "l": "Aerodactyl",
    "m": "MissingNo.",
    "n": "Magnemite",
    "o": "MissingNo.",
    "p": "MissingNo.",
    "q": "Charmander",
    "r": "Squirtle",
    "s": "Charmeleon",
    "t": "Wartortle",
    "u": "Charizard",
    "v": "MissingNo.",
    "w": "MissingNo. (Kabutops Fossil)",
    "x": "MissingNo. (Aerodactyl Fossil)",
    "y": "MissingNo. (Ghost)",
    "z": "Oddish",
    "#": "Rival Blue",
    "\\": "Professor Oak",
    "-": "Chief",
    "?": "Rocket",
    "!": "Cooltrainer",
    "♂": "Blaine",
    "*": "Gentleman",
    ".": "Rival Blue",
    "/": "Champion Blue",
    ",": "Lorelei",
    "♀": "Channeler"
}

# Create Blank Name Array
name_array = [''] * 7


LEVEL_SEARCH = 1
POKEMON_SEARCH = 2

entered_name = "JOE"
entered_name = entered_name.ljust(7)
illegal_characters = re.compile(r"^[a-zA-Z\s\#\\\-\?\!\*\.\/\♀\♂]{1,7}$")
match = illegal_characters.match(entered_name)
if match:
    name_array[:] = list(entered_name)
else:
    raise ValueError("You can only use characters which were available on Pokemon Red, Blue and Yellow!")

def search_lists(search_by):
    output = []
    for i in range(search_by, len(name_array), 2):
        if search_by == 2:  # Pokémon search
            pokemon = pokemon_list.get(name_array[i], None)
            if pokemon:
                output.append(pokemon)
        else:  # Level search
            level = level_list.get(name_array[i], None)
            if level:
                output.append(str(level))
    return output


pokemon_output = search_lists(POKEMON_SEARCH)
level_output = search_lists(LEVEL_SEARCH)
combined_output = [(pokemon, level) for pokemon, level in zip(pokemon_output, level_output)]



print(combined_output)
