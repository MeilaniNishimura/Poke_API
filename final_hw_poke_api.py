import requests
from pprint import pprint

your_pokemon=input("What pokemon are you looking for? ").lower()
base_url = f"https://pokeapi.co/api/v2/pokemon/{your_pokemon}/"

pokemon_requests = requests.get(base_url).json()
pprint(pokemon_requests)

class Pokemon():
    def __init__(self, name, height, weight, type, abilities,):
        self.name = name
        self.height = height
        self.weight = weight
        self.type = type
        self.abilities = abilities


class Pokemon():
    def __init__(self):
        self.type = 'default'
        
    def api_call(self):
        pokemon = 'squirtle'
        api_url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
        response = requests.get(api_url)
        
        self.type = response.json()['types'][0]['type']['name']
        self.name = response.json()['name']
        
pokemon = Pokemon() 
pokemon.api_call()
 print(pokemon)
 print(pokemon.type)
 print(pokemon.name)


import requests
api_url = 'https://pokeapi.co/api/v2/pokemon/' + 'pikachu'
print(api_url)
print(response.json())
response = requests.get(api_url)

class PokedexCreator():
    def __init__(self, type='default_type'):
        self.type = type
        self.pokedex = {}
    
    # Get Poke is now a method of the PokedexCreator class
    def get_poke(self):
        user_pokemon = input('What is the name of the Pokemon you would like to add to your Pokedex?')
        print(f'Here is the Pokemon you decided to search: {user_pokemon}.')
        return user_pokemon.title()
        
    def categoryCreator(self):
        the_pokemon = get_poke()
        api_url = 'https://pokeapi.co/api/v2/pokemon/' + the_pokemon
        type = response.json()['types'][0]['type']['name']
        self.pokedex[type] = the_pokemon
        print(f'Here is the updated Pokedex: {self.pokedex}')


    myPokedex = PokedexCreator()
    myPokedex.categoryCreator()
     print(myPokedex)
     print(myPokedex.type)
