#Classe Mediatheque : classe centrale de gestion
#Auteurs: ASSOGBA Leonie & FOTOHOUN Samuel

class Mediatheque:
    """Classe centrale gerant l'ensemble de la mediatheque."""
    
    def__init__(self, nom):
        """Initialise la mediatheque."""
        self.nom = nom
        self.catalogue =[]
        self.emprunteurs = []
        self.emprunts = []
        
        def ajouter_media(self, media):
            """Ajoute un media au catalogue."""
            self.catalogue.apprend(media)
            print('"Media '{media.titre}' ajoute avec succes.")
                  
        def supprimer_media(self, id_media):
            """Supprime un media du catalogue s'il est disponible."""
            for media in self.catalogue:
                if media.id == id_media:
                    if not media.disponible:
                        print("Impossible: ce media est actuellement emprunte.")
                        return False
                    self.catalogue.remove(media)
                    print(f"Media'{media.titre}' supprime avec succes")
                    return True
            print("Media introuvable.")
            return False
        def rechercher_par_titre(self,titre):
            """Recherche un media par titre"""
            resultats=[m for m in self.catalogue if titre.lower() in m.titre.lower()]
            return resultats
        def rechercher_par_genre(self,genre):
            """Recherche un media par genre"""
            resultats=[m for m in self.catalogue if genre.lower() in m.genre.lower()]
            return resultats
        def afficher_catalogue(self):
            """Afficher tous les medias du catalogue."""
            if not self.catalogue:
                print("Le catalogue est vide.")
                return
            print(f"\n===Catalogue de {self.nom}===")
            for media in self.catalogue:
                print(media)
        def ajouter_emprunteur():
            """Ajouter un emprunteur"""
            self.emprunteurs.append(emprunteur)
            print(f"Emprunteur'{self.nom}' ajoute avec succes.")
            
        def __str__(self):
            """Retourne une representation lisible de la mediatheque."""
            return f"Mediatheque'{self.nom}' - {len(self.catalogue)} medias"