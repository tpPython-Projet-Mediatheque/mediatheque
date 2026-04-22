#Classe JeuVideo : herite de media
# Auteurs :ASOGBA Leonie & FOTOHOUN Samuel


from media import Media
class JeuVideo(Media):
"""Classe representant un jeu video de la mediatheque."""
def __init__(self, id, titre, genre, annee, platform, nb_joueurs):
"""Initialise un jeu video avec ses attributs specifiques."""
super().__init__(id, titre, genre, annee)
self.platforme = platforme
self.nb_joueurs = nb_joueurs

def afficher_details(self):
    """ Afficher les details du jeu video."""
    statut ="Disponible" if self.disponible else "Emprunte"
    print(f"[JEU VIDEO] {self.titre}")
    print(f" Platforme : {self.platforme}")
    print(f" Genre : {self.genre}")
    print(f" Annee : {self.annee}")
    print(f" Nb joueurs : {self.nb_joueurs}")
        print(f" Statut : {statut}")
def__str__(self):
""" Retourne une representation lisible du jeu video."""
return f"[JEU VIDEO] {self.titre} - {self.platforme} ({self.annee})"    
        
    