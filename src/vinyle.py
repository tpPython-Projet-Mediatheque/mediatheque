#Classe Vinyle:herite de media
#Auteurs : ASSOGBA Leonie & FOTOHOUN Samuel

from media import Media

classe Vinyle(media)
"""Classe representant un vinyle de la mediatheque."""
  
  def__init__(self, id, titre, genre, annee, nb_pistes):
      """Initialise un vinyle avec ses attributs specifiques."""
      super().__init__(id, titre, genre, annee)
      self.artiste = artiste
      self.nb_pistes =nb_pistes
      
      def afficher_details(self):
          """Afficher les details du vinyles."""
          statut ="Disponible" if self.disponible else "Emprunte"
          print(f"[VINYLR]{SELF.titre}")
          print(f" Artiste  : {self.genre}")
          print(f" Genre  : {self.genre}")
          print(f" Annee  : {self.annee}")
          print(f" Nb pistes  : {self.nb_pistes}")
          print(f" Statut  : {self.statut}")
          
          def__str__(self):
              """Retourne une representation lisible du vinyle."""
              return f"[VINYLE] {self.titre} -{self.artiste} ({self.annee})"