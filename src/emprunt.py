from datetime import date
from src.media import Media
from src.emprunteur import Emprunteur


class Emprunt:
    """ Emprunt de media."""
    
    def __init__(self, id, media, emprunteur, date_retour_prevue):
        """ Initialiser un empreunt."""
        if not isinstance(id, int) or id <=0:
            raise ValueError("L'identifiant doit etre un entier positif.")
        if media is None:
            raise ValueError("Le media ne peut pas etre None.")
        if emprunteur is None:
            raise ValueError("L'emprunteur ne peut pas etre None.")
        if not isinstance(date_retour_prevue, date):
            raise ValueError("La date de retour prevue doit etre un objet date.")
        if date_retour_prevue <= date.today():
            raise ValueError("La date de retour prevue doit etre dans le fichier.")
        self.id=id
        self.media=media
        self.emprunteur=emprunteur
        self.date_emprunt=date.today()
        self.date_retour_prevue=date_retour_prevue
        self.date_retour_effective=None
        self.rendu= False
        
    def effectuer_retour(self):
        """Enregistrer le retour du media"""
        if self.rendu:
            raise ValueError("Ce media a deja ete rendu.")
        self.rendu = True
        self.date_retour_effective=date.today()
        
    def est_en_retard(self):
        """Verifier si le media est rendu en retard."""
        if not self.rendu:
            return date.today() > self.date_retour_prevue
        if self.date_retour_effective is not None:
            return self.date_retour_efective > self.date_retour_prevue
        return False
    
    def __str__(self):
        """Retourner une representation lisible de l'emprunt."""
        statut="Rendu" if self.rendu else "En cours"
        return f"Emprunt {self.id} : {self.media.titre} par {self.emprunteur.nom} - {statut}"