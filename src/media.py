
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
    def empreuter(self):
        """Marquer le media emprunter"""
        if self.disponible:
            self.disponible= False
            return True
        return False
    def retourner(self):
        """Marquer le media comme disponible."""
        self.disponible=True
    @abstractmethod
    def afficher_details(self):
        """Chaque methode affiche ses details."""
        pass
    def __str__(self):
        """Retourne une representation lisible de média."""
        statut= "Disponible" if self.disponible else "Emprunte"
        return f"{self.titre}({self.genre},{self.annee}) - {statut}"

