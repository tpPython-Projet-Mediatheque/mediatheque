#Fichier principak de test des classes POO
#Auteurs: ASSOGBA Leonie & FOTOHOUN Samuel

from livre import Livre
from vinyle import Vinyle
from jeu_video import JeuVideo
from emprunteur import Emprunteur
from mediatheque import Mediatheque
from emprunt import Emprunt
from datetime import date


#Creation de la mediatheque
ma_mediatheque = Mediatheque("Mediatheque de Parakou")

#Creation des medias 
livre1 = Livre(1, "Dune", "Science-Fiction", 1965, "Frank Herbert", "978-0441013")
vinyle1 = Vinyle(2, "Thriller", "Pop",1982, "Michael Jackson", 9)
jeu1 = JeuVideo(3, "FIFA 24", "Sport", 2023, "PS5", 4)

#Ajout au catalogue
ma_mediatheque.ajouter_media(livre1)
ma_mediatheque.ajouter_media(vinyle1)
ma_mediatheque.ajouter_media(jeu1)

#Details d'un media

print("\n=== Details ===")
livre1.afficher_details()

#Creation d'un emprunteur
emprunteur1 = Emprunteur(1, "ASSOGBA", "Leonie", "asgleonie@gmail.com")
ma_mediatheque.ajouter_emprunteur(emprunteur1)

#Emprunt
print("\n=== Emprunt ===")
livre1.emprunter()
emprunt1 = Emprunt(1, livre1, emprunteur1, date(2026, 5, 22))

#Affichage apres emprunt
ma_mediatheque.afficher_catalogue()
