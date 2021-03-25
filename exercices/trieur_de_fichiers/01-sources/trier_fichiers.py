import os
import json

"""
mp3, wav : Musique
mp4, mov : Videos
jpg, jpeg, png : Images
pdf : Documents
"""

def print_hierarchie(fichier_json):
    with open(fichier_json, 'r') as f:
	    structure = json.load(f)
	    print('Les dossiers existent deja.')


def creer_dossiers(dossier):
    for value in dossier:
        dossier = '{0}/{1}'.format(base, value)
        print('Creation du dossier {0}'.format(dossier))
        os.mkdir(dossier)

def ecrire_json(fichier_json, dictionnaire):
    	with open(fichier_json, 'w') as f:
		    json.dump(dictionnaire, f, indent=4)


base = "/home/dragon76/Documents/ProjetPython/exercices/trieur_de_fichiers/01-sources"
fichier_json = "/home/dragon76/Documents/ProjetPython/exercices/trieur_de_fichiers/structure.json"

#base = base.replace('\\', '/')

structure = {
             "Musique",
             "Videos",
             "Images",
             "Documents"
            }

if os.path.isfile(fichier_json):
    print_hierarchie(fichier_json)
else:
    creer_dossiers(structure)
    ecrire_json(fichier_json, structure)
    








#Création des dossiers et sous dossiers




# Trier les fichiers suivant leurs extansions




