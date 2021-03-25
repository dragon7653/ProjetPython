import json

with open("test.json", "w") as f:
    json.dump("Pèche", f, ensure_ascii=False) # Pour éviter d'avoir comme résultat "P\u00e8che"