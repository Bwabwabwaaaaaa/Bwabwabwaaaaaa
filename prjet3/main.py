import pygame
pygame.init()

######### VARIABLES GLOBALES

# Police d'écriture  (nom police, taille police)
font = pygame.font.Font(None, 36)

# Dimensions & affichage de la fenêtre 
largeur_fenetre, hauteur_fenetre = 700, 700  # Taille de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Nom de la fenêtre
pygame.display.set_caption("Trame jeu de plateau")

# Dictionnaire qui charge les images du jeu (facultatif)
images = {
        "X": pygame.image.load("images/x.png"),
        "O": pygame.image.load("images/o.png"),
        "cavalier": pygame.image.load("images/cavalier.png")
    }


######### FONCTIONS
def afficher_matrice(fenetre, matrice, position, taille_plateau, images=None):
    """
    Affiche une matrice sous forme de grille sur une fenêtre pygame, en affichant soit du texte, soit des images.

    Paramètres :
    ------------
        fenetre (pygame.Surface) : La surface sur laquelle la matrice sera affichée.
    
        matrice (list[list]) : Matrice représentant le plateau de jeu.

        position (tuple) : Coordonnées (x, y) du coin supérieur gauche d'où la matrice sera affichée.

        taille_plateau (tuple) : Dimensions (largeur, hauteur) de la zone où la matrice doit être affichée.
        
        images (dict): Paramètre optionnel, Dictionnaire associant des valeurs de la matrice à des images correspondantes.

    """
    global font
    
    nblig = len(matrice)
    nbcol = len(matrice[0])
    position_x, position_y = position
    largeur_plateau, hauteur_plateau = taille_plateau
    
    #Calcul de la taille d'une case 
    taille_case = min(largeur_plateau // nbcol, hauteur_plateau // nblig)
    
    for i in range(nblig):
        for j in range(nbcol):
            x, y = position_x + j * taille_case, position_y + i * taille_case
            
            #On dessine le carré autour de la case (fenetre, couleur, (left, top, width, height), épaisseur bordure)
            pygame.draw.rect(fenetre, (0, 0, 0), (x, y, taille_case, taille_case), 2)  
            
            #On récupère la valeur à afficher dans la case
            valeur = matrice[i][j]
            
            #Si c'est une image, on la récupère dans le dictionnaire, on la redimensionne et on l'affiche aux bonnes coordonnées
            if images and valeur in images:
                image = pygame.transform.scale(images[valeur], (taille_case, taille_case))
                fenetre.blit(image, (x, y))
                
            #Sinon c'est du texte
            else:
                # (texte à afficher, antialiasing, couleur
                texte = font.render(str(valeur), True, (0, 0, 0))
                #On crée un rextangle pour afficher le texte et on l'écrit au centre
                text_rect = texte.get_rect(center=(x + taille_case // 2, y + taille_case // 2))
                fenetre.blit(texte, text_rect)

def detecter_case_cliquee(matrice, position_plateau, taille_plateau, pos_souris):
    """
    Détecte quelle case de la matrice a été cliquée en fonction des coordonnées de la souris.

    Paramètres :
    ------------
        matrice (list[list]) : Matrice représentant le plateau de jeu.

        position_plateau (tuple) : Coordonnées (x, y) du coin supérieur gauche du plateau.
        
        taille_plateau (tuple) : Dimensions (largeur, hauteur) du plateau de jeu.

        pos_souris (tuple) : Coordonnées (x, y) du curseur de la souris lors du clic.

    Returns :
    ----------
        (tuple ou None) : Retourne un tuple (ligne, colonne) correspondant à la case cliquée, ou None si le clic est en dehors du plateau.
    """
    taille_matrice = len(matrice)
    position_x, position_y = position_plateau
    largeur_plateau, hauteur_plateau = taille_plateau
    taille_case = min(largeur_plateau // len(matrice[0]), hauteur_plateau // taille_matrice)
    
    x_souris, y_souris = pos_souris
    #On commence par vérifier si le clic de la souris a bien eu lieu sur le plateau
    if position_x <= x_souris < position_x + largeur_plateau and position_y <= y_souris < position_y + hauteur_plateau:
        # On calcule sur quelle ligne et quelle colonne le clic a eu lieu en fonction de la taille des cases
        colonne = (x_souris - position_x) // taille_case
        ligne = (y_souris - position_y) // taille_case
        return ligne, colonne
    return None

#def nbr_requin(matrice, x, y):
    #case = matrice[x][y]
    #nb = 0
    #for i in range (-1,2):
        

case1 = { 'bombe': True, 'decouverte' : False , 'marqué' : False, 'image': "cavalier" 'bombe_near': }

######### FONCTION PRINCIPALE DU JEU  
def jeu():
    global images
    
    matrice_exemple = [
        [case1['image'], "1", "X","a"],
        ["o", "2", "x","a"],
        ["o", "2", "x","a"],
        ["x", "cavalier", 13,"cavalier"],
        ["o", "2", "x","a"],
        ["o", "2", "x","a"],
        ["x", "cavalier", 13,"cavalier"]
        
        
    ]
    
    position_plateau = (0, 100)  # Position du plateau dans la fenêtre
    taille_plateau = (500, 800)  # Dimensions du plateau
    fin = False
    while fin == False:
        # Gestion des évènements 
        for event in pygame.event.get():
            # Clic sur la croix de la fenêtre
            if event.type == pygame.QUIT:
                fin = True
            # Clic dans la fenêtre
            elif event.type == pygame.MOUSEBUTTONDOWN:
                case = detecter_case_cliquee(matrice_exemple, position_plateau, taille_plateau, event.pos)
                if case:
                    print("Vous avez cliqué sur la case aux coordonnées", case)
                    
        # Affichage des éléments dans la fenêtre 
        fenetre.fill((255, 255, 255)) # Couleur de fond 
        afficher_matrice(fenetre, matrice_exemple, position_plateau, taille_plateau, images)
                   
        # Mise à jour de l'affichage 
        pygame.display.flip()

jeu()
pygame.quit()