import os
from pprint import pprint


fichier = "/home/dragon76/Documents/ProjetPython/exercices/trier_noms"

liste_nom = os.path.join(fichier, "prenom.txt")
trie = os.path.join(fichier, "prenom_trie.txt")
nouvelle_liste =[]
with open(liste_nom, "r") as f:
    contenue = f.read()
    contenue= contenue.split()
    for i in contenue:
        nouvelle_liste.append(i.strip(" ,."))
liste2 = sorted(nouvelle_liste)
print(liste2)
liste2 = str(liste2).replace(",", "\n")
liste2 = liste2.strip("['")
print(type(liste2))

with open(trie, "a") as f:
    for i in liste2:
        f.write(i)

