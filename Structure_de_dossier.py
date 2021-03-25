import os
import json

def print_hierarchie():
    with open(fichier_json, 'r') as f:
        structure = json.load(f)
    print('Les dossiers existent déjà.')
    print('Voici la hierarchie de dossier:')
    for key, values in structure.items():
        print('. {0}'.format(key))
        for value in values:
            print('|---> {0}'.format(value))
        
        print('='*25)

def creer_dossiers(dossiers):
    for key, values in dossiers.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base, key,value)
            os.makedirs(dossier)
            print('Création du dossier {0}'.format(dossier))


def ecrire_json(fichier_json, dictionnaire):
    with open(fichier_json, 'w') as f:
        json.dump(dictionnaire, f, indent=4)



base = "home/dragon76/Documents/ProjetPython"


fichier_json = "home/dragon76/Documents/ProjetPython/structure.json"



structure = {
            'Musique' : ['Rock', 'Jazz', 'Pop'],
            'Documents' : ['Programmation', 'Travail', 'Maison'],
            'Images' : ['Vacances', 'Travaux'],
            'Videos' : ['Enfants', 'Youtube']
            }


if os.path.isfile(fichier_json):
    print_hierarchie()
else:
    creer_dossiers(structure)
    ecrire_json(fichier_json, structure)
