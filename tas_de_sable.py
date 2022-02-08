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
for i in range (len(grille)):
    for j in range (len(grille)):
        grille[i][j] = randint(0,9)

# définition des fonctions (chaque fonction devra contenir une docstring)


# programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel à la boucle de gestion des événements

