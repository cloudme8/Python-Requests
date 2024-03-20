import requests
import pytest


URL = 'https://api.pokemonbattle.me/v2'

HEADERS = {'Content-Type' : 'Application/json '} 

id = 2067

TOKEN = '3e5e9228315007bd5926800401cc904b'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2067})
    assert response.status_code == 200

def test_trainer_id_response():
    response = requests.get(url = f'{URL}/trainers?trainer_id=2067', params = {"trainer_id" : 2067})
    assert response.json()['data'][0]['id'] == '2067'

