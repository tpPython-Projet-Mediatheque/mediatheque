#Fichier principal - Lance l'interface graphique
#Auteurs: ASSOGBA Leonie & FOTOHOUN Samuel

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import App

if __name__=="__main__":
    app = App()
    app.mainloop()