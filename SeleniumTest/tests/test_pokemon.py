import requests
import pytest
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': '85710c63fd47e361f0eb58f0760636fb'
         }
def test_get_trainers():
    """
    KTI-1. get_trainers_by_id
    """
    response = requests.get(url=f'{URL}/pokemons', params={'trainers_id':3588},headers=HEADER,timeout=5) 
    assert response.status_code == 200, 'Unexpected status code'
    
def test_get_trainer():    
    """
    KTI-2. get_trainer_name
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3588},headers=HEADER,timeout=5) 
    assert response.json()['trainer_name'] == 'PROba6ka', ''