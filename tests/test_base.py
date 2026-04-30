
#Test unitaires du projet Gestionnaire de Mediatheque Intelligente
#Auteurs : ASSOGBA Leonie & FOTOHOUN Samuel
import sys
import os
import pytest
from datetime import date, timedelta
from src.livre import Livre
from src.vinyle import Vinyle
from src.jeu_video import JeuVideo
from src.emprunteur import Emprunteur
from src.emprunt import Emprunt
from src.mediatheque import Mediatheque
from database.init_db import init_db

@pytest.fixture(autouse=True)
def initialiser_db():
    """Initialise la base de donnéés avant chaque test."""
    init_db()

@pytest.fixture
def livre():
    return Livre(1, "Dune", "Science-Fiction", 1965, "Frank Herbert", "978-0441013")

@pytest.fixture
def vinyle():
    return Vinyle(2, "Thriller", "Pop", 1982, "Michael Jackson", 9)

@pytest.fixture
def jeu():
    return JeuVideo(3, "FIFA 24", "Sport", 2023, "PS5", 4)

@pytest.fixture
def emprunteur():
    return Emprunteur(1, "ASSOGBA", "Leonie", "asgleonie@gmail.com")

@pytest.fixture
def mediatheque():
    return Mediatheque("Mediatheque de Parakou")


class TestEmprunteur:
    def test_creation_emprunteur(self, emprunteur):
        """Verifie la creation correcte d'un emprunteur."""
        assert emprunteur.nom =="ASSOGBA"
        assert emprunteur.prenom == "Leonie"
        assert emprunteur.email == "asgleonie@gmail.com"
        
    def test_email_invalide(self):
        """Veerifie qu'un email invalide leve une erreur."""
        with pytest.raises(ValueError):
            Emprunteur(1, "ASSOGBA", "Leonie", "emailinvalide")
            
    def test_peut_emprunter(self, emprunteur):
        """Verifie qu'un emprunteur sans emprunt peut emprunter."""
        assert emprunteur.peut_emprunter() is True 
        
    def test_limite_emprunts(self, emprunteur, livre, vinyle, jeu):
        """Verifie qu'un emprunteur ne peut pas depasser 3 emprunts."""
        date_retour = date.today() + timedelta(days=14)
        emprunt1 = Emprunt(1, livre, emprunteur, date_retour)
        emprunt2 = Emprunt(2, vinyle, emprunteur, date_retour)
        emprunt3 = Emprunt(3, jeu, emprunteur, date_retour)
        emprunteur.ajouter_emprunt(emprunt1)
        emprunteur.ajouter_emprunt(emprunt2)
        emprunteur.ajouter_emprunt(emprunt3)
        assert emprunteur.peut_emprunter() is False
        
    def test_retirer_emprunt_inexistant(self, emprunteur, livre):
        """Verifie qu'on ne peut pas retirer un emprunt inexistant."""
        date_retour =date.today() + timedelta(days=14)
        emprunt =Emprunt(1, livre, emprunteur, date_retour)
        with pytest.raises(ValueError):
            emprunteur.retirer_emprunt(emprunt)
            
            
            
class TestEmprunt:
    def test_creation_emprunt(self, livre, emprunteur):
        """Verifie la cretaion correcte d'un emprunt."""
        date_retour =date.today() + timedelta(days=14)
        emprunt = Emprunt(1, livre, emprunteur, date_retour)
        assert emprunt.rendu is False 
        assert emprunt.date_retour_effective is None
        
    def test_date_retour_passee(self, livre, emprunteur):
        """Verifie qu'une date de retour passee leve une erreur."""
        with pytest.raises(ValueError):
            Emprunt(1, livre, emprunteur, date.today() - timedelta(days=1))
            
    def test_effectuer_retour(self, livre, emprunteur):
        """Verifie qu'un retour est correctement enregistre."""
        date_retour = date.today() + timedelta(days=14)
        emprunt = Emprunt(1, livre, emprunteur, date_retour)
        emprunt.effectuer_retour()
        assert emprunt.rendu is True
        assert emprunt.date_retour_effective == date.today()
        
    def test_double_retour(self, livre, emprunteur):
        """Verifie qu'on ne peut pas rendre un media deja rendu."""
        date_retour = date.today() + timedelta(days=14)
        emprunt = Emprunt(1, livre, emprunteur, date_retour)
        emprunt.effectuer_retour()
        with pytest.raises(ValueError):
            emprunt.effectuer_retour()
            
    def test_pas_en_retard(self, livre, emprunteur):
        """Verifie qu'un emprunt recent n'est pas en retard."""
        date_retour = date.today() + timedelta(days=14)
        emprunt = Emprunt(1, livre, emprunteur,date_retour)
        assert emprunt.est_en_retard() is False
        
        
        

class TestMediatheque:
    
    def test_creation_mediatheque(self, mediatheque):
        """Verifie la creation correcte d'une mediatheque."""
        assert mediatheque.nom == "Mediatheque de Parakou"
        assert len(mediatheque.catalogue) == 0
        
    def test_nom_invalide(self):
        """Verifie qu'un nom vide leve une erreur."""
        with pytest.raises(ValueError):
            Mediatheque("")
            
    def test_ajouter_media(self, mediatheque, livre):
        """Verifie l'ajout d'un media au catalogue."""
        mediatheque.ajouter_media(livre)
        assert len(mediatheque.catalogue) == 1
        
    def test_ajouter_media_doublon(self, mediatheque, livre):
        """Verifie qu'on ne peut pas ajouter deux medias avec le meme id."""
        mediatheque.ajouter_media(livre)
        with pytest.raises(ValueError):
            mediatheque.ajouter_media(livre)
            
    def test_supprimer_media(self, mediatheque, livre):
        """Verifie la suppresion d'un media disponible."""
        mediatheque.ajouter_media(livre)
        resultat = mediatheque.supprimer_media(1)
        assert resultat is True
        assert len(mediatheque.catalogue) == 0
        
    def test_supprimer_media_emprunte(self, mediatheque, livre, emprunteur): 
        """Verifie qu'on ne peut pas supprimer un media emprunter."""
        mediatheque.ajouter_media(livre)
        mediatheque.ajouter_emprunteur(emprunteur)
        mediatheque.enregistrer_emprunt(emprunteur, livre)
        resultat = mediatheque.supprimer_media(1)
        assert resultat is False
        
    def test_rechercher_par_titre(self, mediatheque, livre):
        """Verifie la recherche par titre."""
        mediatheque.ajouter_media(livre)
        resultats = mediatheque.rechercher_par_titre("Dune")
        assert len(resultats) == 1
        
    def test_rechercher_par_auteur(self,mediatheque, livre):
        """Verifie la recherche par auteur."""
        mediatheque.ajouter_media(livre)
        resultats = mediatheque.rechercher_par_auteur("Herbert")
        assert len(resultats) == 1
        
    def test_rechercher_par_genre(self, mediatheque, livre):
        """Verifie la recherche pae genre."""
        mediatheque.ajouter_media(livre)
        resultats = mediatheque.rechercher_par_genre("Science-Fiction")
        assert len(resultats) == 1
        
    def test_enregistrer_emprunt(self, mediatheque, livre, emprunteur):
        """Verifie l'enregistrement d'un emprunt."""
        mediatheque.ajouter_media(livre)
        mediatheque.ajouter_emprunteur(emprunteur)
        emprunt = mediatheque.enregistrer_emprunt(emprunteur, livre)
        assert emprunt is not None
        assert livre.disponible is False
        
    def test_emprunt_media_indisponible(self, mediatheque, livre, emprunteur):
        """Verifie qu'on ne peut pas emprunter un media indisponible."""
        mediatheque.ajouter_media(livre)
        mediatheque.ajouter_emprunteur(emprunteur)
        mediatheque.enregistrer_emprunt(emprunteur, livre)
        emprunt2 = mediatheque.enregistrer_emprunt(emprunteur, livre)
        assert emprunt2 is None
        
    def test_effectuer_retour(self, mediatheque, livre, emprunteur):
        """Verifie le retour d'un retour d'un media emprunte."""
        mediatheque.ajouter_media(livre)
        mediatheque.ajouter_emprunteur(emprunteur)
        mediatheque.enregistrer_emprunt(emprunteur, livre)
        resultats = mediatheque.effectuer_retour(1)
        assert resultats is True
        assert livre.disponible is True
         
            
