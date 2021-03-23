import json

chemin = "/home/dragon76/Documents/ProjetPython/fichier.json"

with open("fichier.json", "r") as f:
    donnees = json.load(f)
nom = "Durand"
prenom = "David"
ville = "Angers"
donnees.extend([{"nom" : nom, 
                 "prenom" : prenom,
                 "ville" : ville}])


with open("fichier.json", "w") as f:
    json.dump(donnees, f, indent=4)