import requests
import os
from IPython.display import Image, display


class Pokemon:
    def __init__(self, name, height, weight, types, sprite, color, habitat, shape, flavor, dex_counter):
        self.name = name
        self.height = height
        self.weight = weight
        self.types = types
        self.sprite = sprite
        self.color = color
        self.habitat = habitat
        self.shape = shape
        self.flavor = flavor
        self.dex_counter = dex_counter

    def __str__(self):
        output = f"{self.name.title()}       \n"
        output += f"Height: {self.height:.2f} inches       \n"
        output += f"Weight: {self.weight:.2f} pounds       \n"
        output += f"Type(s): {', '.join(self.types)}       \n"
        # output += f"Sprite {self.sprite}           \n"
        output += f"Color: {self.color.title()}       \n"
        output += f"Habitat: {self.habitat.title()}       \n"
        output += f"Shape: {self.shape.title()}       \n"
        output += f"\nInformation: {self.flavor}\n"
        output += f"\nPokedex # {self.dex_counter}\n"

        return output
    
    def __repr__(self):
        return f"<Pokemon | {self.name}>"


class PokemonAPI:
    def __init__(self):
        self.base_url1 = "https://pokeapi.co/api/v2/pokemon/"
    
    def get_pokemon_data(self, pokemon_name):
        res = requests.get(f"{self.base_url1}/{pokemon_name}")
        if res.ok:
            data = res.json()
            name = data['name']
            height = data['height']*3.937
            weight = data['weight']//4.536
            types = [data['types'][0]['type']['name']]
            if len(data['types']) > 1:
                types.append(data['types'][1]['type']['name'])
            sprite = data['sprites']['front_shiny']
            return name, height, weight, tuple(types), sprite
        return None, None, None, None

class SpeciesAPI:
    def __init__(self):
        self.base_url2 = "https://pokeapi.co/api/v2/pokemon-species/"

    def __get_species_data(self, pokemon_name):
        res = requests.get(f"{self.base_url2}/{pokemon_name}")
        if res.ok:
            data = res.json()
            color = data['color']['name']
            habitat = data['habitat']['name']
            shape = data['shape']['name']
            flavor = data['flavor_text_entries'][0]['flavor_text']
            dex_counter = data['pokedex_numbers'][0]['entry_number']
            return color, habitat, shape, flavor, dex_counter
        return

    def get_pokemon(self, pokemon_name):
        name, height, weight, types, sprite = PokemonAPI().get_pokemon_data(pokemon_name)
        if not name:
            return f"{pokemon_name.title()} isn't a POKéMON silly! Check your spelling please?"
        
        color, habitat, shape, flavor, dex_counter = self.__get_species_data(pokemon_name)

        new_pokemon = Pokemon(name, height, weight, types, sprite, color, habitat, shape, flavor, dex_counter)
        return new_pokemon

os.system("cls" if os.name == "nt" else "clear")
pokemon_name = input("Please choose a POKéMON and I will provide some stats and useful information. :)\n\n ")
os.system("cls" if os.name == "nt" else "clear")

pokemon1 = SpeciesAPI()
new = pokemon1.get_pokemon(pokemon_name)
output = str(new)

print("++=====++" * 4) 
if new.sprite:
    display(Image(url=new.sprite))       
print(output)
print("++=====++" * 4)