


with open("/home/dragon76/Documents/ProjetPython/exercices/trier_noms/prenom.txt", "r") as f:
    lines = f.read().splitlines()
print(lines)
prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open("/home/dragon76/Documents/ProjetPython/exercices/trier_noms/prenom_trie.txt", "w") as f:
    f.write("\n".join(sorted(prenoms_final)))