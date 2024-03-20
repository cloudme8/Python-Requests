import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'Application/json', 'trainer_token' : '3e5e9228315007bd5926800401cc904b'}
TOKEN = '3e5e9228315007bd5926800401cc904b'


body = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body) 

print(response.text)



body = {
    "pokemon_id": "14449",
    "name": "пукич",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body) 

print(response.text)



body = {
    "pokemon_id": "14449"
}

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body) 

print(response.text)


