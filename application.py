#Importation de la librairie
import os 
import hashlib
from tkinter import *
from tkinter.filedialog import *
import sqlite3
from tkinter import ttk

# Pour initialiser tkinter, nous devons créer un widget root Tk
root = Tk()

root.title("Rename")
# root.iconbitmap('E:\\Project\\Nutrition\\Nutri.ico')
#root.iconbitmap('E:\\Project\\Nutrition\\nutrition.ico')
#root.iconbitmap("nutrition.ico")
# width x height
root.geometry("700x700")

# Ajout d'une barre de menu
menubar = Menu(root)
root.config(menu=menubar)

# Menu Fichier
menufichier = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fichier", menu=menufichier)
menufichier.add_command(label="Ouvrir")
menufichier.add_separator()
menufichier.add_command(label="Préférences")
menufichier.add_command(label="Quitter", command=root.destroy) 

# Menu Edition
menuedition = Menu(menubar,tearoff=0)
menubar.add_cascade(label= "Edition", menu=menuedition)

#menuedition.add_separator()

#Menu Graphique
menugraphique = Menu(menubar,tearoff=0)
menubar.add_cascade(label= "Graphique", menu=menugraphique)

# Menu Help
menuhelp = Menu(menubar,tearoff=0)
menubar.add_cascade(label= "Aide", menu=menuhelp)
menuhelp.add_command(label="FAQ")
menuhelp.add_command(label="A propos")

#Fin de la configuration de l'interface.
root.mainloop()