

chemin = "/home/dragon76/Documents/GitHub.txt"

with open(chemin, "r") as f:
    contenu = f.read()
    #contenu = repr(f.read())   Pour éviter les retour à la ligne
    print(contenu)