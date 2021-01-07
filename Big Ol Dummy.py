x = 'hello'
print(f"this is {x} the answer {3**5}")


import requests
import json
import urllib.request

wub = requests.get('https://pokeapi.co/api/v2/pokemon/flareon')

print(wub)

print(json.dumps(wub.json()['abilities'][0]['ability']['name'], sort_keys=True, indent=4))

lub = requests.get(wub.json()['abilities'][0]['ability']['url'])

print(json.dumps(lub.json(), sort_keys=True, indent=4))