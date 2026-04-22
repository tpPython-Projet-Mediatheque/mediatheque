from datetime import date
class Emprunt:
    """ Emprunt de media."""
    def __init__(self,id,media,emprunteur,date_retour_prevue):
        """ Initialiser un empreunt."""
        self.id=id
        self.media=media
        self.emprunteur=emprunteur
        self.date_emprunt=date.today()
        self.date_retour_prevue=date_retour_prevue
        self.date_retour_effective=None
        self.rendu= False
    def effectuer_retour(self):
        """Enregistrer le retour du media"""
        self.rendu=True
        self.date_retour_effective=date.today()
    def est_en_retard(self):
        """Verifier si le media est rendu en retard."""
        if not self.rendu:
            return date.today()>self.date_retour_prevue
    def __str__(self):
        """Retourner une representation lisible de l'emprunt."""
        statut="Rendu" if self.rendu else "En cours"
        return f"Emprunt {self.id} : {self.media.titre} par {self.emprunteur.nom} - {statut}"