from db_manager import DBManager


class EmpruntDAO:
    """Classe gerant les operations sur les emprunts en base de donnees."""
    
    def __init__(self):
        """Iniatilise le DAO avec le gestionnaire de connexion."""
        self.db =DBManager()
        
        
    def ajouter_emprunteur(self, emprunteur):
         """Ajoute un emprunteur dans la base de donnees."""
         connexion = self.db.get_connexion()
         curseur = connexion.cursor()
         curseur.execute('''
                         INSERT INTO emprunteurs (nom, prenom, email)
                         Vlues(?,?,?)
                         ''',(emprunteur.nom, emprunteur.prenom, emprunteur.email))
         connexion.commit()
         connexion.close()
         print(f"Emprunteur  '{emprunteur.nom}' sauvegarde en base de donnees.")
    
    def ajouter_emprunt(self, emprunt):
        connexion = self.db.get_connexion()
        curseur =connexion.cursor()
        curseur.execute('''
                        INSERT INTO emprunts(id_media, id_emprunteur, date_emprunt,date_retour_prevue,rendu)
                        VALUES(?,?,?,?,?)
                        ''',(
                        emprunt.media.id,
                        emprunt.emprunteur.id,
                        str(emprunt.date_emprunt),
                        str(emprunt.date_retour_prevue),
                        emprunt.rendu
                        ))
        connexion.commit()
        connexion.close()
        print(f"Emprunt sauvegarde en base de donnees.")
    
    def effectueré_retour_db(self, id_emprunt, date_retour_effective):
        """Met a jour un emprunt comme rendu dans la base de donnees."""
        connexion = self.db.get_connexion()
        curseur =connexion.cursor()
        curseur.execute('''
                        UPDATE emprunts
                        SET rendu= 1,  date_retour_effective=?
                        WHERE id= ?
                        ''',(
                        str(date_retour_effective),
                        id_emprunt,
                        ))
        connexion.commit()
        connexion.close()
        print(f"Retour de l'emprunt {id_emprunt} enregistre en base de donnees.")
   
    def get_emprunts_en_cours(self):
        """Recupere tous les emprunts en cours."""
        connexion = self.db.get_connexion()
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM emprunts WHERE RENDU=0")
        emprunts = curseur.fetchall()
        connexion.close()
        return emprunts
    
    def get_historique(self):
        """Recupere tout l'historique des emprunts."""
        conexion = self.db.get_connexion()
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM emprunts")
        emprunts = curseur.fetchall()
        connexion.close()
        return emprunts  