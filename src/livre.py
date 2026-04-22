from media import Media
class Livre(Media):
    """Classe representant un livre de la mediatheque"""
    def __init__(self,id,titre,genre, annnee,auteur,isbn):
        """Initialiser un livre avec ses attributs specifiques."""
        super().__init__(id,titre,genre,annee)
        self.auteur=auteur
        self.isbon
    def afficher_details(self):
        """Afficher les detail du livre"""
        statut= "Disponible" if self.disponible else "Emprunte"
        print(f"[LIVRE] {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Genre: {self.genre}")
        print(f"Annee: {self.annee}")
        print(f"ISBN: {self.isbn}")
        print(f"Statut: {statut}")
    def __str__(self):
        """Retourner une representation lisibre du livre."""
        return f"[LIVRE] {self.titre} - {self.auteur} ({self.annee})"