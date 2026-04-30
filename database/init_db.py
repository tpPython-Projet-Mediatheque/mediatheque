import sqlite3
import os

def init_db():
    """Cree la base de donnees et les tables si elles n'existent pas."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'mediatheque.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    connexion = sqlite3.connect(db_path)
    curseur = connexion.cursor()
    
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS medias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            genre TEXT NOT NULL,
            annee INTEGER NOT NULL,
            type TEXT NOT NULL,
            disponible INTEGER DEFAULT 1,
            auteur TEXT,
            isbn TEXT,
            artiste TEXT,
            nb_pistes INTEGER,
            platforme TEXT,
            nb_joueurs INTEGER
        )
      ''')
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS emprunteurs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL
        )            
    ''')
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS emprunts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_media INTEGER NOT NULL,
            id_emprunteur INTEGER NOT NULL,
            date_emprunt TEXT NOT NULL,
            date_retour_prevue TEXT NOT NULL,
            date_retour_effective TEXT,
            rendu INTEGER DEFAULT 0,
            FOREIGN KEY (id_media) REFERENCES medias(id),
            FOREIGN KEY (id_emprunteur) REFERENCES emprunteurs(id)
        )            
    ''')
    connexion.commit()
    connexion.close()
    print("Base de donnees initialisee avec succes !")
    
if __name__ == "__main__":
    init_db()
                