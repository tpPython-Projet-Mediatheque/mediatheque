#Classe Emprunteur : représente un utilisateur de la mediatheque
#Auteurs : ASSOGBA Leonie & FOTOHOUN Samuel


class Emprunteur:
    """Classe representant un emprunteur de la mediatheque."""

    def __init__(self, id, nom, prenom, email):
        """Initialise un emprunteur avec ses informations."""
        if not isinstance(id,int)or id <=0:
            raise ValueError("L'identifiant doit etre un entier positif.")
        if not isinstance(nom,str) or not nom.strip():
            raise ValueError("Le nom doit etre une chaîne de caractere non vide.")
        if not isinstance(prenom,str) or not prenom.strip():
            raise ValueError("Le prenom doit etre une chaîne de caractere non vide.")
        if not isinstance(email,str) or '@' not in email:
            raise ValueError("L'email doit etre une adresse valide.")
        self.id= id
        self.nom=nom
        self.prenom= prenom
        self.email=email
        self.emprunts_en_cours= []
        
    def peut_emprunter(self):
        """Verifie si l'emprunteur peut encore emprunter (max 3)."""
        return len(self.emprunts_en_cours) < 3
    
    def ajouter_emprunt(self, emprunt):
        """Ajouter un emprunt a la liste des emprunts en cours."""
        self.emprunts_en_cours.append(emprunt)
        
    def retirer_emprunt(self, emprunt):
        """Retire un emprunt de la liste des emprunts en cours."""
        if emprunt not in self.emprunts_en_cours:
            raise ValueError("Cet emprunt ne figure pas dans la liste des emprunts en cours.")
        self.emprunts_en_cours.remove(emprunt)
        
    def __str__(self):
        """Retourne une representation lisible de l'emprunteur."""
        return f"{self.prenom} {self.nom} ({self.email})"