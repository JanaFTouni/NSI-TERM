import json

with open("recette.json") as f:
    rectte = json.load(f)

print(recette["titre"])
