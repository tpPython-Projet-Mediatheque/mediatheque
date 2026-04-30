import sqlite3
import os
class DBManager:
     """Classe gerant la connexion a la base de donnees SQLite."""
     
     def __init__(self):
         """Initialise le chemin vers la base de donnees."""
         self.db_path =os.path.join(
             os.path.dirmane(__file__), '..', 'data', 'mediatheque.db'
         )
         
         def get_connexion(self):
             """Retourne une connexion a la base de donnees."""
             connexion =sqlite3.conect(self.db_path)
             connexion.row_factory = sqlite3.Row
             return connexion