from database.db_manager import DBManager


class MediaDAO:
    """Classe gerant les operations sur les medias en base de donnees."""
    
    def __init__(self):
        """Initialise le DAO avec le gestionnaire de connexion."""
        self.db = DBManager()
        
    def ajouter_media(self, media):
        """Ajoute un media dans la base de donnees."""
        connexion = self.db.get_connexion()
        curseur = connexion.cursor()
        curseur.execute('''
           INSERT INTO medias(titre, genre, annee, type, disponible, auteur, isbn, artiste, nb_pistes, platforme, nb_joueurs)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            media.titre,
            media.genre,
            media.annee,
            type(media).__name__, 
            media.disponible,
            getattr(media, 'auteur', None),
            getattr(media, 'isbn', None),
            getattr(media, 'artiste', None),
            getattr(media, 'nb_pistes', None),
            getattr(media, 'platforme', None),
            getattr(media, 'nb_joueurs', None),            
        ))
        connexion.commit()
        connexion.close()
        print(f"Media '{media.titre}' sauvegarde en base de donnees.")
         
    def get_tous_les_medias(self):
        """Recupere tous les medias de la base de donnees."""
        connexion =self.db.get_connexion()
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM medias")
        medias = curseur.fetchall()
        connexion.close()
        return medias
    
    def rechercher_par_titre(self, titre):
        """Recherche des medias par titre."""
        connexion = self.db.get_connexion()
        curseur = connexion.cursor()
        curseur.execute(
            "SELECT * FROM medias WHERE titre LIKE ?", ('%' +titre + '%',)
        )        
        resultats = curseur.fetchall()
        connexion.close()
        return resultats
    
    def rechercher_par_auteur(self, auteur):
        """Recherher des medias par auteur."""
        connexion = self.db.get_connexion()
        curseur = connexion.cursor()
        curseur.execute(
            "SELECT * FROM medias WHERE auteur LIKE ?", ('%' + auteur + '%',)
        )
        resultats =curseur.fetchall()
        connexion.close()
        return resultats
    
    def modifier_media(self, id_media, titre, genre, annee):
        """Modifie les informations d'un media."""
        connexion =self.db.get_connexion()
        curseur =connexion.cursor()
        curseur.execute('''
            UPDATE medias SET titre = ?, genre = ?, annee = ?,
            WHERE id = ?
        ''', (titre, genre, annee, id_media))
        connexion.commit()
        connexion.close()
        print(f"Media {id_media} modifie avec succes.")
    
    def supprimer_media(self,id_media):
        """Supprimer un media de le base de donnees."""
        connexion = self.db.get_connexion()
        curseur = connexion.execute("DELETE FROM medias WHERE id = ?",(id_media,))
        connexion.commit()
        connexion.close()
        print(f"Media {id_media} supprime de la base de donnees.")
        
    