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
LENGTH = 500
HEIGHT = 500

# définition des variables globales
grille = [[0,0,0],[0,0,0],[0,0,0]]
couleur = {0:"white", 1:"grey", 2:"purple", 3:"blue", 4:"green", 5:"yellow", 6:"orange", 7:"red"}
liste_config = [[[0,0,0],[0,0,0],[0,0,0]]] #cette variable commencera aussi par la grille vide

# définition des fonctions (chaque fonction devra contenir une docstring)
def random_grille():
    """
    Crée une grille aléatoire et l'affiche.

    Returns
    -------
    None
    """
    global grille
    global liste_config
    for i in range (len(grille)):
        for j in range (len(grille)):
            grille[i][j] = randint(0,7)
    #print(grille)
    color()
    liste_config.append(grille)


def empty_grille():
    """
    Crée une grille vide.

    Returns
    -------
    None
    """
    global grille
    global liste_config
    grille = [[0,0,0],[0,0,0],[0,0,0]]
    color()
    liste_config.append(grille)

def config_choisie():
    """
    Crée une grille choisie par l'utilisateur.

    Returns
    -------
    None
    """
    global grille
    global liste_config
    for i in range(len(grille)):
        for j in range(len(grille)):
            nombre=int(input("Chiffre : "))
            grille[i][j]=nombre
    color()
    liste_config.append(grille)

def config_prec():
    """
    Prend la grille précédente.

    Returns
    -------
    None
    """
    global grille
    global liste_config
    grille=liste_config[-1]
    color()
    liste_config.append(grille)

#Ligne 1
def color():
    """
    Affiche la couleur de toutes les cases
    """
    carre1 = canvas.create_rectangle(0,0,LENGTH/3,HEIGHT/3, width=5, fill=couleur[grille[0][0]])
    carre2 = canvas.create_rectangle(LENGTH/3,0,LENGTH/3*2,HEIGHT/3, width=5, fill=couleur[grille[0][1]])
    carre3 = canvas.create_rectangle(LENGTH/3*2,0,LENGTH,HEIGHT/3, width=5, fill=couleur[grille[0][2]])
    carre4 = canvas.create_rectangle(0,HEIGHT/3,LENGTH/3,HEIGHT/3*2, width=5, fill=couleur[grille[1][0]])
    carre5 = canvas.create_rectangle(LENGTH/3,HEIGHT/3,LENGTH/3*2,HEIGHT/3*2, width=5, fill=couleur[grille[1][1]])
    carre6 = canvas.create_rectangle(LENGTH/3*2,HEIGHT/3,LENGTH,HEIGHT/3*2, width=5, fill=couleur[grille[1][2]])
    carre7 = canvas.create_rectangle(0,HEIGHT/3*2,LENGTH/3,HEIGHT, width=5, fill=couleur[grille[2][0]])
    carre8 = canvas.create_rectangle(LENGTH/3,HEIGHT/3*2,LENGTH/3*2,HEIGHT, width=5, fill=couleur[grille[2][1]])
    carre9 = canvas.create_rectangle(LENGTH/3*2,HEIGHT/3*2,LENGTH,HEIGHT, width=5, fill=couleur[grille[2][2]])
    return carre1,carre2,carre3,carre4,carre5,carre6,carre7,carre8,carre9
    
    

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
    if instable(x,y)==True:
        add(x, y)
        grille[x][y]-=4
    else:
        pass


# programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel à la boucle de gestion des événements
racine = tk.Tk() 
racine.title('tas de sable')

#Explication des codes couleurs,
#plus il y a de grains plus la couleur est agressive
print("Association d'une couleur à une valeur d’une configuration :")
print("0 grain = blanc")
print("1 grain = gris")
print("2 grains = violet")
print("3 grains = bleu")
print("4 grains = vert")
print("5 grains = jaune")
print("6 grains = orange")
print("7 grains = rouge")
                                        
canvas = tk.Canvas(racine, bg="black", 
                   height=500, width=500)
canvas.grid(row=1, column=1, columnspan=4)

Configuration_alea = tk.Button(text="Configuration aléatoire", 
                    height=1, width=15,
                    font=("Helvetica", "10"),
                    command=random_grille
                  )
Configuration_alea.grid(row=0, column=1)

Vide = tk.Button(text="Configuration vide", 
                    height=1, width=15,
                    font=("Helvetica", "10"),
                    command=empty_grille
                  )
Vide.grid(row=0, column=2)

Configuration_choisie = tk.Button(text="Configuration vide", 
                    height=1, width=15,
                    font=("Helvetica", "10")
                  )
Configuration_choisie.grid(row=0, column=3)

Configuration_precedente = tk.Button(text="Configuration vide", 
                    height=1, width=15,
                    font=("Helvetica", "10")
                  )
Configuration_precedente.grid(row=0, column=4)


#ligne horizontale
canvas.create_line((0, 500/3), (500, 500/3), fill="gray5", width=5)
canvas.create_line((0, 500/3*2), (500, 500/3*2), fill="gray5", width=5)
#ligne verticale
canvas.create_line((500/3, 0), (500/3, 500), fill="gray5", width=5)
canvas.create_line((500/3*2, 0), (500/3*2, 500), fill="gray5", width=5)


racine.mainloop() 

#print(grille)