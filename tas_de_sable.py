#########################################
# groupe n°5 - MIASHS TD2
# Gabriel PHILIPPE
# Aya Saghraoui
# Wanis Chouaib
# Furkan Toraman
# https://github.com/uvsq22101009/projet_tas_de_sable/blob/main/README.md
######################################### 

# import des librairies
import tkinter as tk
from random import randint

# définition des constantes (écrites en majuscule)


# définition des variables globales
grille = [[0,0,0],[0,0,0],[0,0,0]]
couleur = {1:"grey", 2:"purple", 3:"blue", 4:"green", 5:"yellow", 6:"orange", 7:"red"}


# définition des fonctions (chaque fonction devra contenir une docstring)
def create_grille():
    """
    Crée une grille aléatoire.

    Returns
    -------
    list
    """
    global grille
    for i in range (len(grille)):
        for j in range (len(grille)):
            grille[i][j] = randint(0,7)
    print(grille)
    
    

def empty_grille():
    """
    Crée une grille vide.

    Returns
    -------
    None
    """
    global grille
    grille = [[0,0,0],[0,0,0],[0,0,0]]
    
def instable(x, y):
    """
    Regarde si la case x, y est instable ou non.

    Parameters
    ----------
    x : int
        ligne
    y : int
        colonne

    Returns
    -------
    bool
    """
    global grille
    if grille[x][y] >= 4:
        return True
    return False

def add(x, y):
    """
    Ajoute un grain de sable sur les cases voisines de x, y.

    Parameters
    ----------
    x : int
        ligne
    y : int
        colonne

    Returns
    -------
    None
    """
    global grille
    try:
        grille[x-1][y]+=1
    except:
        pass

    try:
        grille[x+1][y]+=1
    except:
        pass

    try:
        grille[x][y-1]+=1
    except:
        pass

    try:
        grille[x][y+1]+=1
    except:
        pass
    

def avalanche(x, y):
    """
    Enclenchera l'avalanche si la case x,y est instable.

    Parameters
    ----------
    x : int
        ligne
    y : int
        colonne

    Returns
    -------
    None
    """
    global grille
    add(x, y)
    grille[x][y]-=4


# programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel à la boucle de gestion des événements
racine = tk.Tk() 
racine.title('tas de sable')

#Explication des codes couleurs,
#plus il y a de grains plus la couleur est agressive
print("Association d'une couleur à une valeur d’une configuration :")
print("1 grain = gris")
print("2 grains = violet")
print("3 grains = bleu")
print("4 grains = vert")
print("5 grains = jaune")
print("6 grains = orange")
print("7 grains = rouge")
                                        
canvas = tk.Canvas(racine, bg="black", 
                   height=500, width=500)
canvas.grid(row=1, column=1)

Configuration = tk.Button(text="Configuration aléatoire", 
                    height=1, width=15,
                    font=("Helvetica", "10"),
                    command=create_grille
                  )
Configuration.grid(row=0, column=1, padx=200)

#ligne horizontale
canvas.create_line((0, 500/3), (500, 500/3), fill="gray5", width=5)
canvas.create_line((0, 500/3*2), (500, 500/3*2), fill="gray5", width=5)
#ligne verticale
canvas.create_line((500/3, 0), (500/3, 500), fill="gray5", width=5)
canvas.create_line((500/3*2, 0), (500/3*2, 500), fill="gray5", width=5)


racine.mainloop() 

