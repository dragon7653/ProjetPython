import json

chemin = "/home/dragon76/Documents/ProjetPython/fichier.json"

with open("fichier.json", "r") as f:
    donnees = json.load(f)

donnees.append(4)


with open("fichier.json", "w") as f:
    json.dump(donnees, f, indent=4)