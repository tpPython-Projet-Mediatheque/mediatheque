#Classe Emprunteur : représente un utilisateur de la mediatheque
#Auteurs : ASSOGBA Leonie & FOTOHOUN Samuel

class Emprunteur:
    """Classe representant un emprunteur de la mediatheque."""
    
    def__init__(self, id, nom, prenom, email):
        """Initialise un emprunteur avec ses informations."""
        self.id= id
        self.prenom= prenom
        self.email=email
        self.emprunts_en_cours= []
        
        def peut_emprunter(self):
            """Verifie si l'emprunteur peut encore emprunter (max 3)."""
            return len(self.emprunts_en_cours) < 3
        def ajouter_emprunt(self, emprunt):
            """Ajouter nun emprunt a la liste des emprunts en cours."""
            self.emprunts_en_cours.remove(emprunt)
        def retirer_emprunt(self, emprunt):
            """Retire un emprunt de la liste des emprunts en cours."""
            self.emprunts_en_cours.remove(emprunt)
        def__str__(self):
            """Retourne une representation lisible de l'emprunteur."""
            return f"{self.prenom} {self.nom} ({self.email})"