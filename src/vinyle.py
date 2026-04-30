#Classe Vinyle: herite de media
#Auteurs : ASSOGBA Leonie & FOTOHOUN Samuel

from src.media import Media

class Vinyle(Media):
    """Classe representant un vinyle de la mediatheque."""

    def __init__(self, id, titre, genre, annee,artiste, nb_pistes):
        """Initialise un vinyle avec ses attributs spécifiques."""
        super().__init__(id, titre, genre, annee)
        self.artiste = artiste
        self.nb_pistes =nb_pistes
    
    def afficher_details(self):
        """Afficher les détails du vinyles."""
        statut ="Disponible" if self.disponible else "Emprunte"
        print(f"[VINYLE] {self.titre}")
        print(f" Artiste  : {self.genre}")
        print(f" Genre  : {self.genre}")
        print(f" Annee  : {self.annee}")
        print(f" Nb pistes  : {self.nb_pistes}")
        print(f" Statut  : {statut}")
        
    def __str__(self):
        """Retourne une representation lisible du vinyle."""
        return f"[VINYLE] {self.titre} - {self.artiste} ({self.annee})"