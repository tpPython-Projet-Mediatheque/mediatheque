from src.emprunt import Emprunt
from database.media_dao import MediaDAO
from database.emprunt_dao import EmpruntDAO
from datetime import date,timedelta

class Mediatheque:
    
    def __init__(self,nom):

        if not isinstance(nom,str) or not nom.strip():
            raise ValueError ("Le nom de la mediatheque doit etre une chaîne non vide.")
        self.nom=nom
        self.catalogue=[]
        self.emprunteurs=[]
        self.emprunts=[]
        self.media_dao= MediaDAO()
        self.emprunt_dao= EmpruntDAO()

    def ajouter_media(self,media):

        if media is None:
            raise ValueError("Le media ne peut pas etre None.")
        for m in self.catalogue:
            if m.id== media.id:
                raise ValueError("Un  media avec l'identifiant {media.id} existe deja.")
            self.catalogue.append(media)
            self.media_dao.ajouter_media(media)
            print(f"Media '{media.titre}' ajoute avec succes.")
    
    def supprimer_media(self,id_media):

        if not isinstance (id_media,int) or id_media<=0:
            raise ValueError("L'identifiant doit etre un entier positif.")
        for media in self.catalogue:
            if media.id== id_media:
                if not media.disponible:
                    print("Impossible ce media est actuellement emprunte.")
                    return False
                self.catalogue.remove(media)
                self.media_dao.supprimer_media(id_media)
                print(f"Media '{media.titre}' supprime avec succes.")
                return True
            print("Media Intouvable.")
            return False
    
    def modifier_media(self, id_media,titre=None, genre=None, annee=None):

        if not isinstance(id_media,int) or id_media<=0:
            raise ValueError("L'identifiant doit etre un entier positif.")
        if annee is not None and (not isinstance(annee,int) or annee< 1000 or annee> 9999):
            raise ValueError("L'annee doit etre un entier a 4 chiffres.")
        for media in self.catalogue:
            if media.id== id_media:
                if titre:
                    media.titre=titre
                if genre:
                    media.genre=genre
                if annee:
                    media.annee=annee
                self.media_dao.modifier_media(id_media, media.titre, media.genre, media.annee)
                print(f"Media '{media.titre}' modifie avec succes.")
                return True
            print("Media introuvable")
            return False

    def rechercher_par_titre(self,titre):
        """"""
        if not isinstance(titre,str) or not titre.strip():
            raise ValueError("Le titre doit etre une chaîne de caracteres non vide.")
        resultats=[m for m in self.catalogue if titre.lower() in m.titre.lower()]
        return resultats

    def rechercher_par_genre(self,genre):
        """"""
        if not isinstance(genre,str) or not genre.strip():
            raise ValueError("Le genre doit etre une chaîne de caracteres non vide.")
        resultats=[m for m in self.catalogue if genre.lower() in m.genre.lower()]
        return resultats

    def rechercher_par_auteur(self,auteur):
        """"""
        if not isinstance(auteur,str) or not auteur.strip():
            raise ValueError("L'auteur doit etre une chaîne de caracteres non vide.")
        resultats=[]
        for m in self.catalogue:
            auteur_media=getattr(m,'auteur', None) or getattr(m,'artiste', None)
            if auteur_media and auteur.lower() in auteur_media.lower() in auteur_media.lower():
                resultats.append(m)
        return resultats

    def ajouter_emprunteur(self,emprunteur):
        """"""
        if emprunteur in None:
            raise ValueError("L'empruteur ne peut pas etre None.")
        for e in self.emprunteurs:
            if e.id == emprunteur.id:
                raise ValueError(f"Un emprunteur avec l'identifiant '{emprunteur.id}'existe deja.")
                self.emprunteurs.append(emprunteur)
            self.emprunt_dao.ajouter_emprunteur(emprunteur)
            print(f"Emprunteur '{emprunteur.nom}'ajoute avec succes.")

    def enregistrer_emprunt(self,emprunteur, media, duree_jour= 14):
        """"""



    def effectuer_retour(self,id_emprunt):
        """Enregistre le retour d'un media"""
        if not isinstance(id_emprunt,int) or id_emprunt <=0:
            raise ValueError("L'identifiant doit etre un entier positif.")
        for emprunt in self.emprunts:
            if emprunt.id== id_emprunt:
                if emprunt.rendu:
                    print("Ce media a deja ete rendu.")
                    return False
                emprunt.effectuer_retour()
                emprunt.media.retourner()
        emprunt.emprunteur.retirer_emprunt(emprunt)
        self.emprunt_dao.effectuer_retour_db(id_emprunt, emprunt.date_retour_effective)
        print(f"Retour enregistre:'{emprunt.media.titre}'.")
        return True
        print("Emprunt introuvable.")
        return False
    
    def detecter_retards(self):
        """Affiche tous les emprunts en retard."""
        retards=[e for e in self.emprunts if e.est_en_retard()]
        if not retards:
            print("Aucun retard detecte.")
        else:
            print("\n=== Emprunts en retard ===")
            for emprunt in retards:
                print(f"{emprunt}")
        return retards


    def afficher_catalogue(self):
        """Affiche tous les media du catalogue."""
        if not self.catalogue:
            print("Le catalogue est vide.")
            return
        print("\n=== Catalogue de {self.nom} ===")
        for media in self.catalogue:
            print(media)

    def afficher_historique(self):
        """Affiche tout l'historique des emprunts."""
        if not self.emprunts:
            print("Aucun emprunt enregistre.")
            return
        print("\n=== Historique des emprunts ===")
        for emprunt in self.emprunts:
            print(f"{emprunt}")

    def __str__(self):
        """Retourne une representation lisible de la mediatheque"""
        return f"Mediatheque '{self.nom}'-{len(self.catalogue)} medias"