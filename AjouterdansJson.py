import json

chemin = "/home/dragon76/Documents/ProjetPython/fichier.json"

#Partie qui lit les données dans la liste
with open("fichier.json", "r") as f:
    donnees = json.load(f)
    
nom = "Durand"
prenom = "David"
ville = "Angers"

# Partie qui ajoute des donnes à la liste données pour évier d'écraser avec le "w"
donnees.extend([{"nom" : nom, 
                 "prenom" : prenom,
                 "ville" : ville}])


with open("fichier.json", "w") as f:
    json.dump(donnees, f, indent=4)