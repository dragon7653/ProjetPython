import json

chemin = "/home/dragon76/Documents/ProjetPython/fichier.json"
with open(chemin, "r") as f:
    #Ajouter des données dans un fichier json
    #json.dump(list(range(10)), f, indent=4) #Pour écrire dans le fichier json
    
    # 2crire dans un fichier json
    liste = json.load(f)
    print(liste)



# with open(chemin, "r") as f:
#     contenu = f.read()
#     #contenu = repr(f.read())   Pour éviter les retour à la ligne
#     # contenu = Ou f.readlines()
#     # contenu = f.read().splitlines() retourne une liste
#     print(contenu)

# Pour écrire dans un fichier
# with open(chemin, "w") as f : écrase ce qu'il y a dans le fichier'
# with open(chemin, "a") as f :
#     f.write("\nAu revoir") écrit à la suite

