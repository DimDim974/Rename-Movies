###################################################
##Auteur : Dimitri Sautron
##Description : Destinés à pour renommer des films 
##				essentiellements
##Version : 1.1.5
##Date de création : 14/11/2015
##Fichier : Main
###################################################
#Bug v1.0.5:
# 		*Renommage des répertoires en plus des fichiers corrections effectuée.
#
#
#
###################################################
import tkinter
import os
print("=== Renommage en masse.py ===")
fenetre = tkinter.Tk()

from tkinter.filedialog import *

NomFichier = 'data.dat'
MyDate = 'list2.dat'

# se place a l'emplacement C:\Users\%USERNAME% 
os.chdir(os.path.expanduser("~" ))
Fichier2 = open(MyDate,'r')
LSup=Fichier2.read().split()
Fichier2.close()

Emplacement = askdirectory(title="Ouvrir un dossier films",initialdir=os.chdir(os.path.expanduser("~" )))
# lecture dans le fichier avec la méthode read()
##Lister les fichiers et répertoires avec listdir
for element in os.listdir(Emplacement):
	if os.path.isfile(os.path.join(Emplacement,element)):
		#print(element)
##Renommer tout les fichiers sous une normalisation général pour un meilleur traitement 
		texte = ("%s" % element)
	#Première liste des fichiers
	#print(texte)
	Tableau = (texte.replace(" ","."))
	
##Fractionner une chaine en listes
	Tableau = (texte.split('.'))
	
	
	#Ajouter le point avant l'extension !!
	list1=(len(Tableau))
	Tableau.insert(list1-1,".")
	for list in LSup:
		if list in Tableau:
			Tableau.remove(list)
			
	#Copie des deux derniers chaines
	EndTab = Tableau[((len(Tableau))-2)] + Tableau[((len(Tableau))-1)]
	
	#Suppression du dernier deux fois, suppression des deux derniers chaines
	Tableau.pop((len(Tableau))-1)
	Tableau.pop((len(Tableau))-1)
	
##Concacténation de listes
	TableauFixe = Tableau
	TableauFixeII =(' '.join(TableauFixe) + ''.join(EndTab))
	
##Renamme en masse	
	TableauFixeIII = Emplacement+'/'+TableauFixeII
	texte = Emplacement+'/'+texte
	texte.strip(('?!\t'))
	TableauFixeIII.strip(('?!\t'))
	
	print(TableauFixeIII)
	print(texte)
	os.rename(texte, TableauFixeIII)
	
## Ouvrir un fichier 
	Fichier = open(NomFichier,'a')

# écriture dans le fichier avec la méthode write()
	Fichier.writelines(TableauFixeII + "\n")
	
Fichier.close()	
