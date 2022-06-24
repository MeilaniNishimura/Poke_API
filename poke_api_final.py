import requests
import pprint

pp= pprint.PrettyPrinter(indent=3)

class Pokemon:

class Pokedex:
    @staticmethod
    def show_instructions():
        print("""Type 'show' to view Pokedex.
        Type 'quit to exit program.
        Type 'sort' to view a categorized version of your Pokedex.""")

    @classmethod
    def populate(cls, pokemon_name):
        print(pokemon_name)

        if cls.list_:
            pass

        try:
            pass

        except:
            pass
    
    @classmethod 
    def run(cls): 
        done = False
        
        while not done:
            cls.show_instructions()
            
            pokemon_name= input("Type in the name of a Pokemon to populate your Pokedex. Type quit to exit the program ").lower()
            if pokemon_name == quit:
                done = True
            elif pokemon_name== "show":
                pass
            elif pokemon_name == "sort":
                pass
            else:
                #functionality to add pokemon to pokedex
                cls.populate(pokemon_name)

        

