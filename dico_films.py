
# recupere la somme des prix des DVD
films = {"Le Seigneur des Anneaux" : 12.00,
         "Harry Potter": 9.00,
         "Blade Runner": 7.50
         }

prix = 0

for cle, valeur in films.items():
    prix += valeur
print(prix)


# for cle in films:
#     print(films[cle])
#     prix += films[cle]

# print(prix)