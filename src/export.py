# Module d'export des donnees
#Auteurs : ASSOGBA Leonie & FOTOHOUN Samuel

import csv
import json
import os
from datetime import date


def export_csv(mediatheque):
    """Exporte le catalogue des medias en CSV."""
    dossier = os.path.join(os.path.dirname(__file__), '..', 'export')
    os.makedirs(dossier, exist_ok=True)
    chemin = os.path.join(dossier, 'catalogue.csv')
    
    with open(chemin, 'w', newline='', encoding='utf-8')as fichier:
        writer = csv.writer(fichier)
        writer.writerow(['ID', 'Type', 'Titre', 'Genre', 'Annee', 'Disponible', 'Auteur/Artiste'])
        for media in mediatheque.catalogue:
            auteur = getattr(media, 'auteur', None) or getattr(media, 'artiste', None) or '-'
            writer.writerow([
                media.id,
                type(media).__name__,
                media.titre,
                media.genre,
                media.annee,
                'Oui' if media.disponible else 'Non',
                auteur
            ])
    print(f"Export CSV effectue : {chemin}")
    return chemin


def export_json(mediatheque):
    """Exporte le catalogue des medias en JSON."""
    dossier = os.path.join(os.path.dirname(__file__), '..', 'exports')
    os.makedirs(dossier, exist_ok=True)
    chemin = os.path.join(dossier, 'catalogue.json')
    
    donnees = []
    for media in mediatheque.catalogue:
        auteur = getattr(media, 'auteur', None) or getattr(media, 'artiste', None) or '-'
        donnees.append({
            'id': media.id,
            'type': type(media).__name__,
            'titre': media.titre,
            'genre': media.genre,
            'annee': media.annee,
            'disponible': media.disponible,
            'auteur_artiste': auteur
        })
        
    with open(chemin, 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=4)
        
    print(f"export JSON effectue : {chemin}")
    return chemin


def export_emprunts_csv(mediatheque):
    """Exporte l'historique des emprunts en CSV."""
    dossier = os.path.join(os.path.dirname(__file__), '..', 'exports')
    os.makedirs(dossier, exits_ok=True)
    chemin = os.path.join(dossier, 'emprunts.csv')
    
    with open(chemin, 'w', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(['ID', 'Media', 'Emprunteur', 'Date emprunt', 'Date retour prevue', 'Statut', 'En retard'])
        for emprunt in mediatheque.emprunts:
            statut = 'Rendu' if emprunt.rendu else 'En cours'
            retard = 'Oui' if emprunt.est_en_retard() else 'Non'
            writer.writerow([
                emprunt.id,
                emprunt.medi.titre,
                f"{emprunt.emprunteur.prenom} {emprunt.emprunteur.nom}",
                str(emprunt.date_emprunt),
                str(emprunt.date_retour_prevue),
                statut,
                retard
            ])        
    print(f"Export emprunts CSV effetue : {chemin}")
    return chemin