import json

d = json.loads('{"nom": "Knuth", "prenom": "Donald"}')

with open('Informaticien.json', 'w') as f:
    json.dump(d, f)