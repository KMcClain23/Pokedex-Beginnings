import requests

class Pokemon:
    def __init__(self, name, height, weight, base_xp):
        self.name = name
        self.height = height
        self.weight = weight
        self.base_xp = base_xp

    def __str__(self):
        output = f"       {self.name.title()}       \n"
        output += f"       Height: {self.height}       \n"
        output += f"       Weight: {self.weight}       \n"
        output += f"       Base XP: {self.base_xp}       \n"

        return output
    
    def __repr__(self):
        return(f"<Pokemon | {self.name}>")


class PokemonAPI:
    def __init__(self):
        self.base_url= "https://pokeapi.co/api/v2/pokemon/"

    
    def __get(self, poke_name):
        res = requests.get(f"{self.base_url}/{poke_name}")
        if res.ok:
            return res.json()
        return

    def get_pokemon(self, pokemon_name):
        data = self.__get(pokemon_name)
        if not data:
            return f"{pokemon_name.title()} isn't a pokémon! Silly!"
        else:
            print("")
            name = data['name']
            height = data['height']
            weight = data['weight']
            base_xp = data['base_experience']

            new_pokemon = Pokemon(name,height,weight, base_xp)
            return new_pokemon
       
print("++=====++" *4)        

pokemon1 = PokemonAPI()
new = pokemon1.get_pokemon('squirtle')
print(new)

print("++=====++" *4)

pokemon2 = PokemonAPI()
new2 = pokemon2.get_pokemon('squirty')
print(new2)

print("++=====++" *4)