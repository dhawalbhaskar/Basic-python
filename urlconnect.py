import requests
import pandas as pd

baseurl ='https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url=f"{baseurl}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code != 200:
        print('Something went wrong')
    else:
        return response.json()


pokemon = 'pikachu'
pokemon_info = get_pokemon_info(pokemon)
print(f"name {pokemon_info['name']}")
print(f"id {pokemon_info['id']}")
print(f"height :  {pokemon_info['height']}")
print(f"weight :  {pokemon_info['weight']}")

