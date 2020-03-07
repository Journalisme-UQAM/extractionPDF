# coding utf-8

import requests ### pour se connecter en HTTP (comme d'hab)
import pytesseract ### ce module vous permet de faire de la reconnaissance optique de caractères sur des fichiers PDF de type «image». 
### Pour l'installer, faire simplement «pip install pytesseract» dans votre terminal.

### Pour vous en servir, vous aurez également besoin de deux autres bibliothèques

### Pillow, pour gérer des images en python
### Vous faites d'abord «pip install pillow» dans votre terminal
### Et ajoutez la ligne suivante en début de script:
from PIL import Image

### Vous devrez aussi installer pdf2image avec... vous l'aurez deviné, «pip install pdf2image»
### Puis, ajoutez la ligne suivante à votre script
from pdf2image import convert_from_path

### ÉTAPE 1 - définir le PDF qu'on souhaite traiter.
### Cette étape peut aussi être placée dans une boucle si on souhaite traiter plusieurs PDFs.
urlRapport = "https://www.sq.gouv.qc.ca/wp-content/uploads/2019/10/2019-10-23-stats-vols-identite-fraudes-identite.pdf"

### ÉTAPE 2 - se connecter au serveur où se trouve le PDF (en prenant soin de se présenter)
entetes = {
    "User-Agent":"Jean-Hugues Roy : Prof. journalisme, UQAM - Salutations à Martin Prud'homme!"
}

req = requests.get(urlRapport, headers = entetes)

### ÉTAPE 3 - il faut écrire le fichier PDF, qui se trouve dans le «content» de la commande «requests» qu'on a fait à l'étape 2, sur notre ordi.
### On lui donne un nom de notre choix. Il n'est pas interdit de choisir un nom plus court.
### On le fait en mode «wb» pour «write binary».
with open("monSupercalifragilistiqueFichierPDF.pdf", "wb") as fichier:
	fichier.write(req.content)

### ÉTAPE 4 - on utilise «convert_from_path» de pdf2image pour briser le pdf en autant de pages qu'il contient, car on ne pourra traiter qu'une image à la fois.
### On peut placer ces pages dans une variable de type liste qu'on peut appeler «feuillets»
feuillets = convert_from_path("monSupercalifragilistiqueFichierPDF.pdf", 500)

### ÉTAPE 5 - on va initialiser une variable de type «string» pour recueillir les textes qu'on va extraire une page à la fois à l'étape suivante
texteComplet = ""

### ÉTAPE 6 - on crée une boucle pour traiter toutes les pages générées à l'étape 4
for feuillet in feuillets:
	feuillet.save("pagePDF.jpg","JPEG")
	texte = str(pytesseract.image_to_string(Image.open("pagePDF.jpg"))) ### C'est ici que la reconnaissance optique des caractères est effectuée et que les caractères reconnus sont placés dans la variable "texte"
	texteComplet += texte + " "

print(texteComplet) ### Vous pouvez ensuite sauvegarder ce texte dans un fichier CSV ou TXT, par exemple, pour utilisation future en traitement du langage naturel
