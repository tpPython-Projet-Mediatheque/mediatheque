
# BLOC 2- Fondations: démonstration des types de données complexes
#projet: Gestionnaire de Médiathèque Intelligente
# Auteurs: ASSOGBA Léonie & FOTOHOUN Samuel

# 1.Dictionnaire(dict): représenter un média du catalogue
livre={
"id":"1",
"titre":"Dune",
"auteur":"Frank Herbert",
"genre":"Science-Fiction",
"annee":1965,
"disponible":True
}

print("=== Dictionnaire ===")
print(livre)
print("Titre :",livre["titre"])
print("Disponible :", livre["disponible"])

# 2.Liste de Dictionnaire : le catalogue complet

catalogue=[
{ 

"id":1,
"titre": "Dune",
"auteur": "Frank Herbert",
"genre": "Science-Fiction",
"disponible": True
},
{
"id":2,
"titre": "Thriller",
"artiste": "Michael jackson",
"genre" :"Pop",
"disponible": False
},
{
"id":3,
"titre":"FIFA 24",
"platforme":"PS5",
"genre":"Sport",
"disponible":True
}
]

print("\n=== Liste de Dictionnaire ===")
print(catalogue)
print("Premier média :", catalogue[0]["titre"])
print("Deuxième média :", catalogue[1]["titre"])

# 3.Tuple: clé composite (id_media, id_emprunteur)

emprunt= (1, 7)
print("\n=== Tuple ===")
print(emprunt)
print("ID du média emprunté :", emprunt[0])
print("ID de l'emprunteur :" , emprunt[1])

# 4.Liste de tuples : résultats bruts SQLite (fetchall)

resultats_sqlite =[
(1,"Dune", "Frank Herbert", "Science-Fiction", True),
(2, "Thriller", "Michael Jackson", "Pop", False),
(3, "FIFA 24","PS5", "Sport", True)
]

print("\n=== Liste de tuples===")
print(resultats_sqlite)
print("Premier résultat :" , resultats_sqlite[0])
print("Titre du premier résultats :", resultats_sqlite[0][1])

# 5.Set: genres uniques du catalogue

tous_les_genres =["Science-Fiction", "Pop","Sport", "Pop", "Science-Fiction","Jazz"]
genres_uniques = set(tous_les_genres)

print("\n=== Set ===")
print("Tous les genres :",tous_les_genres)
print("Genre uniques :", genres_uniques)
