import os
from glob import glob
import shutil
from pprint import pprint

chemin = "/home/dragon76/Documents/ProjetPython/exercices/trieur_de_fichiers/01-sources"

extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents"}

fichiers = glob(os.path.join(chemin, "*"))
#pprint(fichiers)
for fichier in fichiers:
    extension = os.path.splitext(fichier)[-1]
    dossier = extensions.get(extension)
    if dossier:
        chemin_dossier = os.path.join(chemin, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)
        shutil.move(fichier, chemin_dossier)

#base = base.replace('\\', '/')



    








#Création des dossiers et sous dossiers




# Trier les fichiers suivant leurs extansions




