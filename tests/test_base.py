def test_creation_vinyle():
    """Verifie qu'un vinyle est cree correctement."""
    vinyle= Vinyle(2,"Thriller","Pop",1982,"Michael Jackson",9)
    assert vinyle.titre=="Thriller"
    assert vinyle.artiste=="Michael Jackson"
    assert vinyle.disponible==True

def test_creation_jeu_video():
    """Verifie qu'un vinyle est cree correctement."""
    jeu= JeuVideo(3,"FIFA 24","Sport",2023,"PS5",4)
    assert jeu.titre=="FIFA 24"
    assert jeu.artiste=="PS5"
    assert jeu.disponible==True

def test_emprunt_media_deja_emprunte():
    livre= Livre(1, "Dune", "Science-Fiction", 1965, "Frank Herbert","978-0441013593")
    livre.emprunter()
    try:
        livre.emprunter()
        assert False
    except ValueError:
        assert True

def test_emprunteur_max_emprunts():
    emprunteur=Emprunter(1, "ASSOGBA", "Leonie", "Leonie@gmail.com")
    livre1= Livre(1, "Dune","Science-Fiction",1965,"Frank Herbert","978")
    livre2= Livre(2, "Python","Information",2020,"Auteur2","123")
    livre3= Livre(3, "Java","Informatique",2019,"Auteur3","456")
    emprunteur.ajouter_emprunt(livre1)
    emprunteur.ajouter_emprunt(livre2)
    emprunteur.ajouter_emprunt(livre3)
    assert emprunteur.peut.emprunter()== False