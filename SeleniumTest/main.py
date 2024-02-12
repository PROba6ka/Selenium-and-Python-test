"""
Kolorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': '85710c63fd47e361f0eb58f0760636fb'
          }
#body = {
#"name": "generate",
#"photo": "generate"
    #}

#body = {
    #"pokemon_id": "28744",
   # "name": "Луna",
    #"photo": "https://dolnikov.ru/pokemons/albums/005.png"
#}

body = {
    "pokemon_id": "28742"
}
#response = requests.post(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=5) 
#print(response) 

#response = requests.put(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=5)
#print(response)

response = requests.post(url=f'{URL}/trainers/add_pokeball',json=body,headers=HEADER,timeout=5)
print(response)