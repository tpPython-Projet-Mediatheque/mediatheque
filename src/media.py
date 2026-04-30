
from abc import ABC,abstractmethod
class Media(ABC):
    """ Classe abstraite representant un media de la mediateque"""
    def __init__(self,id,titre,genre,annee):
        """ Initialiser les attributs communs a tous les medias. """
        self.id=id
        self.titre=titre
        self.genre=genre
        self.annee=annee
        self.disponible=True
    def emprunter(self):
        """Marquer le media comme emprunte."""
        if not self.disponible:
            raise ValueError(f"'{self.titre}' est deja emprunte.")
            self.disponible= False
            return True
        return False
    def retourner(self):
        """Marquer le media comme disponible."""
        if self.disponible:
            raise ValueError(f"'{self.titre}' n'est pas emprunte")
        self.disponible= True
        
    @abstractmethod
    def afficher_details(self):
        """Chaque methode affiche ses details."""
        pass
    def __str__(self):
        """Retourne une representation lisible de média."""
        statut= "Disponible" if self.disponible else "Emprunte"
        return f"{self.titre}({self.genre},{self.annee}) - {statut}"

