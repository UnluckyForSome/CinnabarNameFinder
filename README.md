# CinnabarNameFinder

Shows which wild Pokémon a player name would give in the Old Man glitch of Pokémon Red and Blue: after watching the old man in Viridian City catch a Weedle, surfing along Cinnabar Island's east coast meets Pokémon made from the bytes of the player's name.

The script reads a name of up to seven characters, padded with spaces to seven. The 3rd, 5th and 7th characters each pick a Pokémon (or a trainer, or MissingNo.), and the 2nd, 4th and 6th give their levels, from two lookup tables of the game's character codes.

## Requirements

Python 3. Standard library only.

## Run

1. Set `entered_name` near the bottom of `CinnabarNameFinder.py` to the name to check.
2. Run it:

   ```
   python CinnabarNameFinder.py
   ```

It prints a list of `(Pokémon, level)` pairs. For example, `RED` gives:

```
[('Mewtwo', '132'), ('MissingNo.', '127'), ('MissingNo.', '127')]
```

Only characters available when naming the player are accepted (letters, space and `# \ - ? ! * . / ♀ ♂`); anything else raises a `ValueError`.
