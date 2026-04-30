#Fichier principak de test des classes POO
#Auteurs: ASSOGBA Leonie & FOTOHOUN Samuel

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.init_db import init_db
from  src.livre import Livre
from src.vinyle import Vinyle
from src.jeu_video import JeuVideo
from src.emprunteur import Emprunteur
from src.mediatheque import Mediatheque
from src.emprunt import Emprunt
from datetime import date

#Initialisation de la base de donnees
init_db()

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

# Affichage du catalogue
print("\n=== Catalogue initial ===")
ma_mediatheque.afficher_catalogue()

#Details d'un media
print("\n=== Details ===")
livre1.afficher_details()
vinyle1.afficher_details()
jeu1.afficher_details()

#Creation d'un emprunteur
emprunteur1 = Emprunteur(1, "ASSOGBA", "Leonie", "asgleonie@gmail.com")
ma_mediatheque.ajouter_emprunteur(emprunteur1)

#Emprunt via la mediatheque
print("\n=== Emprunt ===")
livre1.emprunter()
emprunt1 = ma_mediatheque.enregistrer.emprunt(livre1, emprunteur1) 

#Affichage apres emprunt
print("\n=== Catalogue apres emprunt ===")
ma_mediatheque.afficher_catalogue()

#Historique des emprunts
ma_mediatheque.afficher_historique()

#Verification des retards
print("\n=== Verification des retards ===")
ma_mediatheque.detecter_retards()

#Retour du media
print("\n=== Retour ===")
ma_mediatheque.effectuer_catalogue()

#Affichage apres retour
print("\n=== Catalogue apres retour ===")
ma_mediatheque.afficher_catalogue()

#Test de recherche
print("\n=== Recherche par titre : 'Dune' ===" )
resultats = ma_mediatheque.rechercher_par_titre("Dune")
for r in resultats:
    print(r)
    
print("\n=== Rechercher par auteur : 'Herbert' ===")
resultats = ma_mediatheque.rechercher_par_auteur("Herbert")
for r in resultats:
    print(r)
    
print("\n=== Rechercher par genre : 'Pop' ===")
resultats = ma_mediatheque.rechercher_par_genre("Pop")
for r in resultats:
    print(r)
