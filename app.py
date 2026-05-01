# Interface graphique Tkinter

import tkinter as tk 
from tkinter import ttk, messagebox, simpledialog 
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'database'))

from livre import Livre
from vinyle import Vinyle
from jeu_video import JeuVideo
from emprunteur import Emprunteur
from mediatheque import Mediatheque
from export import export_csv, export_json, export_emprunts_csv
from database.init_db import init_db

# =====================================================================
# COULEURS ET STYLES
# =====================================================================

BG_DARK="#1e1e2e"
BG_CARD="#2a2a3e"
BG_INPUT="#313145"
ACCENT="#7c3aed"
ACCENT_HOVER="#6d28d9"
SUCCESS="#10b981"
DANGER="#ef4444"
WARNING="#f59e0b"
TEXT_PRIMARY="#f8fafc"
TEXT_SECONDARY="#94a3b8"
BORDER="#3f3f5f"

# =====================================================================
# CLASSE PRINCIPALE
# =====================================================================

class App(tk.Tk):
    """Application principale de gestion de la mediatheque."""
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de mediatheque Intelligente")
        self.geometry("1100x700")
        self.minsize(900,600)
        self.configure(bg=BG_DARK)
        self.resizable(True,True)

        # Initialisation base de donnees et mediatheque
        init_db()
        self.mediatheque= Mediatheque("Mediatheque de Parakou")
        self._charger_donnees_test()
        
        # Construction de l'interface
        self._creer_header()
        self._creer_navigation()
        self._creer_contenu()
        self._creer_statusbar()

        # Afficher le tableau de bord par defaut
        self.afficher_dashboard()

    def _charger_donnees_test(self):
        """Charge des donnees de demonstration."""
        try:
            l1=Livre(1,"Dune"," Science-Fiction",1965,"Frank Herbert","978-0441013")
            l2=Livre(2,"Le Petit Prince"," Conte",1943,"Saint-Exupery","978-2070408504")
            v1=Vinyle(3,"Thriller","Pop",1982,"Michael Jackson",9)
            j1=JeuVideo(4,"FIFA 24"," Sport",2023,"PS5",4)
            j2=JeuVideo(5,"Zelda"," Aventure",2023,"Nintendo Switch",1)
            for media in [l1,l2,v1,j1,j2]:
                self.mediatheque.catalogue.append(media)
        except Exception:
            pass
    
    def _creer_header(self):
        """Cree la barre de titre."""
        header=tk.Frame(self, bg=ACCENT, height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(
            header,
            text="Gestionnaire de Mediatheque Intelligente",
            font=("Segeo UI",16,"bold"),
            bg=ACCENT,
            fg=TEXT_PRIMARY
        ).pack(side=tk.LEFT,padx=20,pady=15)
        tk.Label(
            header,
            text="IUT Parakou - 2025/2026",
            font=("Segoe UI",10),
            bg=ACCENT,
            fg="#c4b5fd"
        ).pack(side=tk.RIGHT,padx=20)

    def _creer_navigation(self):
        """Cree la barre de navigation laterale."""
        self.nav=tk.Frame(self, bg=BG_CARD, width=200)
        self.nav.pack(side=tk.LEFT, fill=tk.Y)
        self.nav.pack_propagate(False)
        tk.Label(
            self.nav,
            text="NAVIGATION",
            font=("Segeo UI",9,"bold"),
            bg=BG_CARD,
            fg=TEXT_SECONDARY
        ).pack(pady=(20,10),padx=15,anchor=tk.W)
        self.boutons_nav={}
        menus=[
            ("Tableau de bord","dashboard"),
            ("Catalogue","catalogue"),
            ("Emprunts","emprunts"),
            ("Rechercher","recherche"),
            ("Historique","historique"),
            ("Exporter","export"),
        ]
        for texte,cle in menus:
            btn=tk.Button (
                self.nav,
                text=texte,
                font=("Segeo UI",11),
                bg=BG_CARD,
                fg=TEXT_PRIMARY,
                bd=0,
                padx=15,
                pady=10,
                anchor=tk.W,
                cursor="hand2",
                activebackground=ACCENT,
                activeforeground=TEXT_PRIMARY,
                command=lambda c=cle: self._naviguer(c)
            )
            btn.pack(fill=tk.X, padx=10, pady=2)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=ACCENT))
            btn.bind("<Leave>", lambda e, b=btn, c=cle: b.configure(
                bg=ACCENT if self.page_active==c else BG_CARD
            ))
            self.boutons_nav[cle]=btn   
            
            #Separateur
            tk.Frame(self.nav, bg=BORDER, height=1).pack(fill=tk.X, padx=10, pady=15)
            
            # Badge retards
            self.label_retards= tk.Label(
                self.nav,
                text="",
                font=("Segoe UI",9),
                bg=BG_CARD,
                fg=DANGER
            )
            self.label_retards.pack(padx=15, anchor=tk.W)
            self.page_active="dashboard"
    
    def _creer_contenu(self):
        """Cree la zone de contenu principale."""
        self.contenu=tk.Frame(self, bg=BG_DARK)
        self.contenu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frames={}
        for page in ["dashboard","catalogue","emprunts","recherche","historique","export"]:
            frame=tk.Frame(self.contenu, bg=BG_DARK)
            self.frames[page]=frame
    
    def _creer_statusbar(self):
        """Cree la barre de statut en bas."""
        self.statusbar=tk.Frame(self, bg=BG_CARD, height=30)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.statusbar.pack_propagate(False)
        self.statut_label=tk.Label(
            self.statusbar,
            text="Application demaree avec succes.",
            font=("Segoe UI",9),
            bg=BG_CARD,
            fg=SUCCESS
        )
        self.status_label.pack(side=tk.LEFT, padx=15)
    
    def _set_status(self,message, couleur=SUCCESS):
        """Met a jour la barre de statut."""
        self.status_label.configure(text=f" {message}", fg=couleur)
    
    def _naviguer(self,page):
        """Navigue vers la page."""
        for cle, btn in self.boutons_nav.items():
            btn.configure(bg=ACCENT if cle==page else BG_CARD)
        self.page_active=page
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[page].pack(fill=tk.BOTH, expand=True)
        methode=getattr(self, f"afficher_{page}")
        methode()

    def _actualiser_badge_retards(self):
        """Met a jour le badge des retards."""
        retards=[e for e in self.mediatheque.emprunts if e.est_en_retard()]
        if retards:
            self.label_retards.configure(
                text=f" {len(retards)} retard(s) detecte(s)"
            )
        else:
            self.label_retards.configure(text="Ancun retard")

    # ==================================================================
    # TABLEAU DE BORD
    # ==================================================================

    def afficher_dashboard(self):
        """Affiche le tableau de bord."""
        frame=self.frames["dashboard"]
        for w in frame.winfo_children():
            w.destroy()
        tk.Label(
            frame,
            text="Vue d'ensemble de votre mediatheque",
            font=("Segeo UI",11),
            bg=BG_DARK,
            fg=TEXT_SECONDARY
        ).pack(padx=30, anchor=tk.W)
        # Cartes de statistiques
        frame_cartes= tk.Frame(frame, bg=BG_DARK)
        frame_cartes.pack (fill=tk.X, padx=30, pady=20)
        nb_livres= sum(1 for m in self.mediatheque.catalogue if type(m).__name__=="Livre")
        nb_vinyles= sum(1 for m in self.mediatheque.catalogue if type(m).__name__=="Vinyle")
        nb_jeux= sum(1 for m in self.mediatheque.catalogue if type(m).__name__=="JeuVideo")
        nb_emprunts= sum(1 for e in self.mediatheque.emprunts if not e.rendu)
        nb_retards= sum(1 for e in self.mediatheque.emprunts if e.est_en_retard())
        stats=[
            ("","Livres", nb_livres, ACCENT),
            ("","Vinyles", nb_vinyles, SUCCESS),
            ("","Jeux Video", nb_jeux, WARNING),
            ("","Emprunts en cours", nb_emprunts, "#3b82f6"),
            ("","Retards", nb_retards, DANGER),
        ]
        for emoji, label, couleur in stats:
            carte=tk.Frame(frame_cartes, bg=BG_CARD, padx=20, pady=15)
            carte.pack(side=tk.LEFT, padx=8, pady=5, fill=tk.Y)
            tk.Label(
                carte,
                text=emoji,
                font=("Segoe UI",24),
                bg=BG_CARD,
                fg=couleur
            ).pack()
            tk.Label(
                carte,
                text=str(valeur),
                font=("Segoe UI",28,"bold"),
                bg=BG_CARD,
                fg=couleur
            ).pack()
            tk.Label(
                carte,
                text=label,
                font=("Segoe UI",10),
                bg=BG_CARD,
                fg=TEXT_SECONDARY
            ).pack()
        # Liste des derniers emprunts
        tk.Label(
                frame,
                text="Emprunts récents",
                font=("Segoe UI",14,"bold"),
                bg=BG_CARD,
                fg=TEXT_PRIMARY
            ).pack(pady=(10,5), padx=30, anchor=tk.W)
        frame_liste=tk.Frame(frame,bg=BG_DARK)
        frame_liste.pack(fill=tk.BOTH, expand=True, padx=30, pady=5)
        cols=("Media", "Emprunteur", "Date retour", "Statut")
        tree=ttk.Treeview(frame_liste, columns=cols, show="headings", height=8)
        self._styler_treeview(tree)
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=180)
        for emprunt in self.mediatheque.emprunts[-5:]:
            statut="Rendu" if emprunt.rendu else ("Retard" if emprunt.est_en_retard() else "En cours")
            tree.insert("", tk.END, values=(
                emprunt.media.titre,
                f"{emprunt.emprunteur.prenom} {emprunt.emprunteur.nom}",
                str(emprunt.date_retour_prevue),
                statut
            ))
        tree.pack(fill=tk.BOTH, expand=True)
        self._actualiser_badge_retards()
    
    # ==================================================================
    # CATALOGUE
    # ==================================================================

    def afficher_catalogue(self):
        """Affiche le catalogue des medias."""
        frame=self.frames["catalogue"]
        for w in frame.winfo_children():
            w.destroy()
        tk.Label(
            frame,
            text="Catalogue des Medias",
            font=("Segoe UI",20, "bold"),
            bg=BG_DARK,
            fg=TEXT_PRIMARY
        ).pack(pady=(30,5), padx=30, anchor=tk.W)
        # Barre d'outils
        frame_outils=tk.Frame(frame, bg=BG_DARK)
        frame_outils.pack(fill=tk.X, padx=30, pady=10)
        for texte, couleur, commande in [
            ("Ajouter", SUCCESS, self._ajouter_media),
            ("Modifier", WARNING, self._modifier_media),
            ("Supprimer", DANGER, self._supprimer_media),
        ]:
            tk.Button(
                frame_outils,
                text=texte,
                font=("Segoe UI", 10, "bold"),
                bg=couleur,
                fg=TEXT_PRIMARY,
                bd=0,
                padx=15,
                pady=8,
                cursor="hand2",
                command=commande
            ).pack(side=tk.LEFT, padx=5)
        # Recherche en temps reel
        frame_search=tk.Frame(frame, bg=BG_DARK)
        frame_search.pack(fill=tk.X, padx=30, pady=5)
        tk.Label(
            frame_search,
            text="Recherche rapide :",
            font=("Segoe UI", 10),
            bg=BG_DARK,
            fg=TEXT_SECONDARY
        ).pack(side=tk.LEFT)
        self.search_var=tk.StringVar()
        self.search_var.trace("w", lambda *a: self._filtrer_catalogue())
        entry=tk.Entry(
            frame_search,
            textvariable=self.search_var,
            font=("Segoe UI", 11),
            bg=BG_INPUT,
            fg=TEXT_PRIMARY,
            insertbackground=TEXT_PRIMARY,
            bd=0,
            width=30
        )
        entry.pack(side=tk.LEFT, padx=10, ipady=5)
        # Tableau
        frame_table=tk.Frame(frame, bg=BG_DARK)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        cols=("ID", "Type", "Titre", "Genre", "Annee", "Statut")
        self.tree_catalogue = ttk.Treeview(frame_table, columns=cols, show="headings")
        self._styler_treeview(self.tree_catalogue)
        largeurs=[50,100,250,150,80,100]
        for col, larg in zip(cols, largeurs):
            self.tree_catalogue.heading(
                col, text=col,
                command=lambda c=col: self._trier_catalogue(c)
            )
            self.tree_catalogue.column(col, width=larg)
        scroll=ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree_catalogue.yview)
        self.tree_catalogue.configure(yscrollcommand=scroll.set)
        self.tree_catalogue.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self._remplir_catalogue(self.mediatheque.catalogue)

    def _styler_treeview(self, tree):
        """Applique le style sombre au treeview."""
        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background=BG_CARD,
            foreground=TEXT_PRIMARY,
            fieldbackground=BG_CARD,
            rowheight=30,
            font=("Segoe UI", 10)
        )
        style.configure("Treeview.Heading",
            background=ACCENT,
            foreground=TEXT_PRIMARY,
            font=("Segoe UI", 10, "bold")
        )
        style.map("Treeview", background=[("selected", ACCENT)])

    def _remplir_catalogue(self, medias):
        """Remplit le tableau du catalogue."""
        self.tree_catalogue.delete(*self.tree_catalogue.get_children())
        for media in medias:
            statut="Disponible" if media.disponible else "Emprunte"
            tag="disponible" if media.disponible else "emprunte"
            self.tree_catalogue.insert("", tk.END, values=(
                media.id,
                type(media).__name__,
                media.titre,
                media.genre,
                media.annee,
                statut
            ), tags=(tag,))
        self.tree_catalogue.tag_configure("disponible", foreground=SUCCESS)
        self.tree_catalogue.tag_configure("emprunte", foreground=DANGER)

    def _filtrer_catalogue(self):
        """Filtre le catalogue en temps reel."""
        terme=self.search_var.get().lower()
        resultats=[
            m for m in self.mediatheque.catalogue
            if terme in m.titre.lower() or terme in m.genre.lower()
        ]
        self._remplir_catalogue(resultats)
    
    def _trier_catalogue(self,colonne):
        """Trier le catalogue par colonne."""
        index=["ID","Type","Titre","Genre","Annee","Statut"].index(colonne)
        medias=sorted(self.mediatheque.catalogue, key=lambda m: str(
            [m.id,type(m).__name__,m.titre,m.genre,m.annee,m.disponible][index]
        ))
        self._remplir_catalogue(medias)

    def _ajouter_media(self):
        """Ouvre une fenetre pour ajouter un media."""
        fenetre=tk.Toplevel(self)
        fenetre.title("Ajouter un media")
        fenetre.configure(bg=BG_DARK)
        fenetre.geometry("420x480")
        fenetre.grab_set()

        tk.Label(fenetre, text="Ajouter un Media", font=("Segoe UI", 14, "bold"),
                bg=BG_DARK, fg=TEXT_PRIMARY).pack(pady=20)
        
        champs={}

        def ajouter_champ(label, cle):
            tk.Label(fenetre, text=label, font=("Segoe UI",10),
                    bg=BG_DARK, fg=TEXT_SECONDARY).pack(anchor=tk.W,padx=30)
            entry=tk.Entry(fenetre, font=("Segoe UI",11),bg=BG_INPUT,
                            fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY,bd=0,width=35)
            entry.pack(padx=30,pady=5,ipady=5)
            champs[cle]=entry

        tk.Label(fenetre, text="Type de media :", font=("Segoe UI", 10),
                bg=BG_DARK, fg=TEXT_SECONDARY).pack(anchor=tk.W, padx=30)
        type_var=tk.StringVar(value="Livre")
        frame_type=tk.Frame(fenetre, bg=BG_DARK)
        frame_type.pack(anchor=tk.W, padx=30)
        for t in ["Livre","Vinyle","JeuVideo"]:
            tk.Radiobutton(frame_type,text=t,variable=type_var, value=t,
                           bg=BG_DARK,fg=TEXT_PRIMARY,selectcolor=BG_CARD,
                           font=("Segoe UI",10)).pack(side=tk.LEFT,padx=5)
            
        ajouter_champ("Titre *", "titre")
        ajouter_champ("Genre *", "genre")
        ajouter_champ("Annee *", "annee")
        ajouter_champ("Auteur / Artiste / Platforme", "specifique")
        ajouter_champ("ISBN / Nb pistes / Nb joueurs", "extra")

        def confirmer():
            try:
                id_media=len(self.mediatheque.catalogue)+1
                titre=champs["titre"].get().strip()
                genre=champs["genre"].get().strip()
                annee=int(champs["annee"].get().strip())
                specifique=champs["specifique"].get().strip()
                extra=champs["extra"].get().strip()
                t=type_var.get()
                if t=="Livre":
                    media=Livre(id_media,titre,genre,annee,specifique,extra)
                elif t=="Vinyle":
                    media=Vinyle(id_media,titre,genre,annee,specifique,int(extra) if extra else 0)
                else:
                    media=JeuVideo(id_media,titre,genre,annee,specifique,int(extra) if extra else 1)
                
                self.mediatheque.ajouter_media(media)
                self._set_status(f"Media '{titre}' ajoute avec succes.")
                fenetre.destroy()
                self.afficher_catalogue()
            except ValueError as e:
                messagebox.showerror("Erreur", str(e), parent=fenetre)
        
        tk.Button(fenetre, text="Confirmer", font=("Segoe UI", 11, "bold"),
                  bg=SUCCESS,fg=TEXT_PRIMARY,bd=0,padx=20,pady=8,
                  cursor="hand2",command=confirmer).pack(pady=20)

    def _modifier_media(self):
        """Modifie le media selectionne."""
        selection=self.tree_catalogue.selection()
        if not selection:
            messagebox.showwarning("Attention","Veuillez selectionner un media.")
            return
        valeurs=self.tree_catalogue.item(selection[0])["values"]
        id_media=int(valeurs[0])

        nouveau_titre=simpledialog.askstring("Modifier", "Nouveau titre :", parent=self)
        nouveau_genre=simpledialog.askstring("Modifier", "Nouveau genre :", parent=self)
        
        if nouveau_titre or nouveau_genre:
            self.mediatheque.modifier_media(id_media, titre=nouveau_titre, genre=nouveau_genre)
            self._set_status(f"Media {id_media} modifie avec succes.")
            self.afficher_catalogue()

    def _supprimer_media(self):
        """Supprime le media selectionne."""
        selection=self.tree_catalogue.selection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez selectionner un media.")
            return
        valeurs=self.tree_catalogue.item(selection[0])["values"]
        id_media=int(valeurs[0])
        titre=valeurs[2]

        if messagebox.askyesno("Confirmation", f"Supprimer '{titre}' ?"):
            resultat=self.mediatheque.supprimer_media(id_media)
            if resultat:
                self._set_status(f"Media '{titre}' supprime.", couleur=DANGER)
            else:
                messagebox.showerror("Erreur", "Ce media est actuellement emprunte.")
            self.afficher_catalogue()

    # ==================================================================
    # EMPRUNTS
    # ==================================================================

    def afficher_emprunts(self):
        """Affiche la page des emprunts."""
        frame=self.frames["emprunts"]
        for w in frame.winfo_children():
            w.destroy()
        
        tk.Label(frame, text="Gestion des Emprunts", font=("Segoe UI", 20, "bold"),
                bg=BG_DARK, fg=TEXT_PRIMARY).pack(pady=(30, 5), padx=30, anchor=tk.W)
        
        frame_outils=tk.Frame(frame, bg=BG_DARK)
        frame_outils.pack(fill=tk.X, padx=30, pady=10)
            
        for texte, couleur, commande in [
            ("Nouvel emprunt", SUCCESS, self._nouvel_emprunt),
            ("Ajouter emprunteur", ACCENT, self._ajouter_emprunteur),
            ("Effectuer retour", WARNING, self._effectuer_retour),
        ]:
            tk.Button(frame_outils, text=texte, font=("Segoe UI", 10, "bold"),
                    bg=couleur, fg=TEXT_PRIMARY, bd=0, padx=15, pady=8,
                    cursor="hand2", command=commande).pack(side=tk.LEFT, padx=5)
            frame_table=tk.Frame(frame, bg=BG_DARK)
            frame_table.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
            
            cols=("ID","Media","Emprunteur","Date emprunt","Date retour","Statut")
            self.tree_emprunts=ttk.Treeview(frame_table, columns=cols, show="headings")
            self._styler_treeview(self.tree_emprunts)
            
            largeurs=[50,200,180,120,120,120]
            for col, larg in zip(cols, largeurs):
                self.tree_emprunts.heading(col, text=col)
                self.tree_emprunts.column(col, width=larg)
            
            scroll=ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree_emprunts.yview)
            self.tree_emprunts.configure(yscrollcommand=scroll.set)
            self.tree_emprunts.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            
            self._remplir_emprunts()

    def _remplir_emprunts(self):
        """Remplit le tableau des emprunts."""
        self.tree_emprunts.delete(*self.tree_emprunts.get_children())
        for emprunt in self.mediatheque.emprunts:
            if emprunt.rendu:
                statut="Rendu"
                tag="rendu"
            elif emprunt.est_en_retard():
                statut="Retard"
                tag="retard"
            else:
                statut="En cours"
                tag="en_cours"
            self.tree_emprunts.insert("", tk.END, values=(
                emprunt.id,
                emprunt.media.titre,
                f"{emprunt.emprunteur.prenom} {emprunt.emprunteur.nom}",
                str(emprunt.date_emprunt),
                str(emprunt.date_retour_prevue),
                statut
            ), tags=(tag,))
        self.tree_emprunts.tag_configure("retard", foreground=DANGER)
        self.tree_emprunts.tag_configure("rendu", foreground=SUCCESS)
        self.tree_emprunts.tag_configure("en_cours", foreground=WARNING)

    def _nouvel_emprunt(self):
        """Ouvre une fenetre pour enregistrer un emprunt."""
        fenetre=tk.Toplevel(self)
        fenetre.title("Nouvel emprunt")
        fenetre.configure(bg=BG_DARK)
        fenetre.geometry("400x380")
        fenetre.grab_set()

        tk.Label(fenetre, text="Enregistrer un Emprunt", font=("Segoe UI", 14, "bold"),
                bg=BG_DARK, fg=TEXT_PRIMARY).pack(pady=20)

        medias_dispo=[m for m in self.mediatheque.catalogue if m.disponible]
        if not medias_dispo:
            messagebox.showinfo("Info", "Aucun media disponible.", parent=fenetre)
            fenetre.destroy()
            return

        tk.Label(fenetre, text="Media :", font=("Segoe UI", 10),
                bg=BG_DARK, fg=TEXT_SECONDARY).pack(anchor=tk.W, padx=30)
        media_var=tk.StringVar()
        media_combo=ttk.Combobox(fenetre, textvariable=media_var, width=35,
                                values=[f"{m.id} - {m.titre}" for m in medias_dispo])
        media_combo.pack(padx=30,pady=5)

        tk.Label(fenetre, text="Emprunteur :", font=("Segoe UI", 10),
                 bg=BG_DARK, fg=TEXT_SECONDARY).pack(anchor=tk.W, padx=30)
        emprunteur_var=tk.StringVar()
        emprunteur_combo=ttk.Combobox(fenetre, textvariable=emprunteur_var, width=35,
                                    values=[f"{e.id} - {e.prenom} {e.nom}"
                                            for e in self.mediatheque.emprunteurs])
        emprunteur_combo.pack(padx=30, pady=5)

        tk.Label(fenetre, text="Duree (jours) :", font=("Segoe UI", 10),
                bg=BG_DARK, fg=TEXT_SECONDARY).pack(anchor=tk.W, padx=30)
        duree_entry=tk.Entry(fenetre, font=("Segoe UI", 11), bg=BG_INPUT,
                            fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY, bd=0, width=10)
        duree_entry.insert(0, "14")
        duree_entry.pack(padx=30, pady=5, ipady=5, anchor=tk.W)

        def confirmer():
            try:
                id_media=int(media_var.get().split("-")[0])
                id_emprunteur=int(emprunteur_var.get().split("-")[0])
                duree=int(duree_entry.get())
                media=next(m for m in self.mediatheque.catalogue if m.id==id_media)
                emprunteur=next(e for e in self.mediatheque.emprunteurs if e.id==id_emprunteur)
                emprunt=self.mediatheque.enregistrer_emprunt(emprunteur, media, duree)
                if emprunt:
                    self._set_status(f"Emprunt enregistre:'{media.titre}'.")
                    fenetre.destroy()
                    self._remplir_emprunts()
                    self._actualiser_badge_retards()
            except Exception as e:
                messagebox.showerror("Erreur", str(e), parent=fenetre)

        tk.Button(fenetre, text="Confirmer", font=("Segoe UI", 11, "bold"),
                  bg=SUCCESS, fg=TEXT_PRIMARY, bd=0, padx=20, pady=8,
                  cursor="hand2", command=confirmer).pack(pady=20)

    def _effectuer_retour(self):
        """Effectue le retour du media selectionne."""
        selection=self.tree_emprunts.selection()
        if not selection:
            messagebox.showwarning("Attention", "Veuillez selectionner un emprunt.")
            return
        valeurs=self.tree_emprunts.item(selection[0])["values"]
        id_emprunt=int(valeurs[0])
        if messagebox.askyesno("Confirmation", f"Confirmer le retour de '{valeurs[1]}' ?"):
            resultat=self.mediatheque.effectuer_retour(id_emprunt)
            if resultat:
                self._set_status(f"Retour de '{valeurs[1]}' enregistre.", couleur=SUCCESS)
                self._remplir_emprunts()
                self._actualiser_badge_retards()
            else:
                messagebox.showerror("Erreur", "Ce media a deja ete rendu.")

    def _ajouter_emprunteur(self):
        """Ouvre une fenetre pour ajouter un emprunteur."""
        fenetre=tk.Toplevel(self)
        fenetre.title("Ajouter un emprunteur")
        fenetre.configure(bg=BG_DARK)
        fenetre.geometry("400x320")
        fenetre.grab_set()

        tk.Label(fenetre, text="Ajouter un Emprunteur", font=("Segoe UI", 14, "bold"),
                 bg=BG_DARK, fg=TEXT_PRIMARY).pack(pady=20)

        champs={}

        def ajouter_champ(label, cle):
            tk.Label(fenetre, text=label, font=("Segoe UI", 10),
                    bg=BG_DARK, fg=TEXT_SECONDARY).pack(anchor=tk.W, padx=30)
            entry=tk.Entry(fenetre, font=("Segoe UI", 11), bg=BG_INPUT,
                            fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY, bd=0, width=35)
            entry.pack(padx=30, pady=5, ipady=5)
            champs[cle]=entry

        ajouter_champ("Nom *", "nom")
        ajouter_champ("Prenom *", "prenom")
        ajouter_champ("Email *", "email")

        def confirmer():
            try:
                id_emprunteur=len(self.mediatheque.emprunteurs)+1
                nom=champs["nom"].get().strip()
                prenom=champs["prenom"].get().strip()
                email=champs["email"].get().strip()
                emprunteur=Emprunteur(id_emprunteur, nom, prenom, email)
                self.mediatheque.ajouter_emprunteur(emprunteur)
                self._set_status(f"Emprunteur '{prenom} {nom}' ajoute avec succes.")
                fenetre.destroy()
            except ValueError as e:
                messagebox.showerror("Erreur", str(e), parent=fenetre)

        tk.Button(fenetre, text="Confirmer", font=("Segoe UI", 11, "bold"),
                  bg=SUCCESS, fg=TEXT_PRIMARY, bd=0, padx=20, pady=8,
                  cursor="hand2", command=confirmer).pack(pady=20)

    # ==================================================================
    # RECHERCHE
    # ==================================================================

    def afficher_recherche(self):
        """Affiche la page de recherche."""
        frame=self.frames["recherche"]
        for w in frame.winfo_children():
            w.destroy()

        tk.Label(frame, text="Recherche de Medias", font=("Segoe UI", 20, "bold"),
                 bg=BG_DARK, fg=TEXT_PRIMARY).pack(pady=(30, 5), padx=30, anchor=tk.W)

        frame_search=tk.Frame(frame, bg=BG_DARK)
        frame_search.pack(fill=tk.X, padx=30, pady=15)

        tk.Label(frame_search, text="Critere :", font=("Segoe UI", 10),
                 bg=BG_DARK, fg=TEXT_SECONDARY).pack(side=tk.LEFT)

        self.critere_var=tk.StringVar(value="titre")
        for texte, valeur in [("Titre", "titre"), ("Auteur/Artiste", "auteur"), ("Genre", "genre")]:
            tk.Radiobutton(frame_search, text=texte, variable=self.critere_var, value=valeur,
                           bg=BG_DARK, fg=TEXT_PRIMARY, selectcolor=BG_CARD,
                           font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=10)

        frame_input=tk.Frame(frame, bg=BG_DARK)
        frame_input.pack(fill=tk.X, padx=30, pady=5)

        self.recherche_var=tk.StringVar()
        self.recherche_var.trace("w", lambda *a: self._executer_recherche())

        entry=tk.Entry(frame_input, textvariable=self.recherche_var,
                        font=("Segoe UI", 12), bg=BG_INPUT, fg=TEXT_PRIMARY,
                        insertbackground=TEXT_PRIMARY, bd=0, width=40)
        entry.pack(side=tk.LEFT, ipady=8, padx=(0, 10))

        tk.Button(frame_input, text="Rechercher", font=("Segoe UI", 10, "bold"),
                  bg=ACCENT, fg=TEXT_PRIMARY, bd=0, padx=15, pady=8,
                  cursor="hand2", command=self._executer_recherche).pack(side=tk.LEFT)

        frame_table=tk.Frame(frame, bg=BG_DARK)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        cols=("ID","Type","Titre","Genre","Annee","Statut")
        self.tree_recherche=ttk.Treeview(frame_table, columns=cols, show="headings")
        self._styler_treeview(self.tree_recherche)

        largeurs=[50,100,250,150,80,100]
        for col, larg in zip(cols, largeurs):
            self.tree_recherche.heading(col, text=col)
            self.tree_recherche.column(col, width=larg)

        scroll=ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree_recherche.yview)
        self.tree_recherche.configure(yscrollcommand=scroll.set)
        self.tree_recherche.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def _executer_recherche(self):
        """Execute la recherche en temps reel."""
        terme=self.recherche_var.get().strip()
        if not terme:
            return
        critere=self.critere_var.get()
        if critere=="titre":
            resultats=self.mediatheque.rechercher_par_titre(terme)
        elif critere=="auteur":
            resultats=self.mediatheque.rechercher_par_auteur(terme)
        else:
            resultats=self.mediatheque.rechercher_par_genre(terme)

        self.tree_recherche.delete(*self.tree_recherche.get_children())
        for media in resultats:
            statut="Disponible" if media.disponible else "Emprunte"
            tag="disponible" if media.disponible else "emprunte"
            self.tree_recherche.insert("", tk.END, values=(
                media.id, type(media).__name__,
                media.titre, media.genre, media.annee, statut
            ), tags=(tag,))
        self.tree_recherche.tag_configure("disponible", foreground=SUCCESS)
        self.tree_recherche.tag_configure("emprunte", foreground=DANGER)

    # ==================================================================
    # HISTORIQUE
    # ==================================================================
    
    def afficher_historique(self):
        """Affiche l'historique des emprunts."""
        frame=self.frames["historique"]
        for w in frame.winfo_children():
            w.destroy()

        tk.Label(frame, text="Historique des Emprunts", font=("Segoe UI", 20, "bold"),
                bg=BG_DARK, fg=TEXT_PRIMARY).pack(pady=(30, 5), padx=30, anchor=tk.W)

        retards=[e for e in self.mediatheque.emprunts if e.est_en_retard()]
        couleur_info=DANGER if retards else SUCCESS
        texte_info=f"  {len(retards)} emprunt(s) en retard detecte(s)" if retards else "Aucun retard detecte"

        tk.Label(frame, text=texte_info, font=("Segoe UI", 11, "bold"),
                bg=BG_DARK, fg=couleur_info).pack(padx=30, anchor=tk.W, pady=5)

        frame_table=tk.Frame(frame, bg=BG_DARK)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        cols=("ID", "Media", "Emprunteur", "Date emprunt", "Date retour prevue", "Date retour effective", "Statut")
        tree=ttk.Treeview(frame_table, columns=cols, show="headings")
        self._styler_treeview(tree)

        largeurs=[40,160,150,110,130,140,100]
        for col, larg in zip(cols, largeurs):
            tree.heading(col, text=col)
            tree.column(col, width=larg)

        for emprunt in self.mediatheque.emprunts:
            if emprunt.rendu:
                statut="Rendu"
                tag="rendu"
            elif emprunt.est_en_retard():
                statut="Retard"
                tag="retard"
            else:
                statut="En cours"
                tag="en_cours"

            tree.insert("", tk.END, values=(
                emprunt.id,
                emprunt.media.titre,
                f"{emprunt.emprunteur.prenom} {emprunt.emprunteur.nom}",
                str(emprunt.date_emprunt),
                str(emprunt.date_retour_prevue),
                str(emprunt.date_retour_effective) if emprunt.date_retour_effective else "-",
                statut
            ), tags=(tag,))

        tree.tag_configure("retard", foreground=DANGER)
        tree.tag_configure("rendu", foreground=SUCCESS)
        tree.tag_configure("en_cours", foreground=WARNING)

        scroll=ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # ==================================================================
    # EXPORT
    # ==================================================================

    def afficher_export(self):
        """Affiche la page d'export."""
        frame=self.frames["export"]
        for w in frame.winfo_children():
            w.destroy()

        tk.Label(frame, text="Exporter les Donnees", font=("Segoe UI", 20, "bold"),
                 bg=BG_DARK, fg=TEXT_PRIMARY).pack(pady=(30, 5), padx=30, anchor=tk.W)

        tk.Label(frame, text="Choisissez le format d'export souhaite.",
                font=("Segoe UI", 11), bg=BG_DARK, fg=TEXT_SECONDARY).pack(padx=30, anchor=tk.W)

        frame_cartes=tk.Frame(frame, bg=BG_DARK)
        frame_cartes.pack(fill=tk.X, padx=30, pady=30)

        exports=[
            ("Catalogue CSV", "Export du catalogue en format CSV", SUCCESS, self._export_csv),
            ("Catalogue JSON", "Export du catalogue en format JSON", ACCENT, self._export_json),
            ("Emprunts CSV", "Export de l'historique des emprunts en CSV", WARNING, self._export_emprunts),
        ]

        for titre, desc, couleur, commande in exports:
            carte=tk.Frame(frame_cartes, bg=BG_CARD, padx=25, pady=20, cursor="hand2")
            carte.pack(side=tk.LEFT, padx=10, pady=5)

            tk.Label(carte, text=titre, font=("Segoe UI", 13, "bold"),
                    bg=BG_CARD, fg=couleur).pack(anchor=tk.W)
            tk.Label(carte, text=desc, font=("Segoe UI", 9),
                    bg=BG_CARD, fg=TEXT_SECONDARY).pack(anchor=tk.W, pady=5)
            tk.Button(carte, text="Exporter", font=("Segoe UI", 10, "bold"),
                    bg=couleur, fg=TEXT_PRIMARY, bd=0, padx=15, pady=6,
                    cursor="hand2", command=commande).pack(anchor=tk.W, pady=5)
            
    def _export_csv(self):
        try:
            chemin=export_csv(self.mediatheque)
            messagebox.showinfo("Succes", f"Export CSV effectue :\n{chemin}")
            self._set_status("Export CSV effectue avec succes.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def _export_json(self):
        try:
            chemin=export_json(self.mediatheque)
            messagebox.showinfo("Succes", f"Export JSON effectue :\n{chemin}")
            self._set_status("Export JSON effectue avec succes.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def _export_emprunts(self):
        try:
            chemin=export_emprunts_csv(self.mediatheque)
            messagebox.showinfo("Succes", f"Export emprunts CSV effectue :\n{chemin}")
            self._set_status("Export emprunts CSV effectue avec succes.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

# =====================================================================
# LANCEMENT
# =====================================================================

if __name__=="__main__":
    app=App()
    app.mainloop()





    