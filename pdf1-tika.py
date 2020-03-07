# coding utf-8

import requests ### pour se connecter en HTTP
import tika ### bibliothèque pour traiter des PDFs «natifs» tant sous Mac, sous Linux, que sous Windows
### Faites «pip install tika» dans votre terminal si vous ne l'avez pas déjà.
### Importez aussi le module suivant:
from tika import parser

### ÉTAPE 1 - définir le PDF qu'on souhaite traiter.
### Cette étape peut aussi être placée dans une boucle si on souhaite traiter plusieurs PDFs.
urlRapport = "https://www.vgq.qc.ca/Fichiers/Publications//rapport-annuel//1987-1988//fr_Rapport1987-1988.pdf" ### exemple avec un rapport du Bureau de la Vérificatrice générale du Québec

### ÉTAPE 2 - se connecter au serveur où se trouve le PDF (en prenant soin de se présenter)
entetes = {
    "User-Agent":"Jean-Hugues Roy : Prof. journalisme, UQAM - Salutations à Mme Guylaine Leclerc!"
}

req = requests.get(urlRapport, headers = entetes)

### ÉTAPE 3 - il faut écrire le fichier PDF, qui se trouve dans le «content» de la commande «requests» qu'on a fait à l'étape 2, sur notre ordi.
### On lui donne un nom de notre choix. Il n'est pas interdit de choisir un nom plus court.
### On le fait en mode «wb» pour «write binary».
with open("monSupercalifragilistiqueFichierPDF.pdf", "wb") as fichier:
	fichier.write(req.content)

### ÉTAPE 4 - on utilise le «parser» de Tika pour analyser le contenu du PDF et le mettre dans une variable.
### Pour ce faire, on ouvre le fichier qu'on a enregistré à l'étape 3 et on l'ouvre en mode «rb» pour «read binary».
contenuPDF = parser.from_file(open("monSupercalifragilistiqueFichierPDF.pdf", 'rb'))

### ÉTAPE 5 - la variable dans laquelle on a placé le contenu du PDF est un dictionnaire.
### Il y a une clé «metadata» qui contient plusieurs informations, comme par exemple:
print(contenuPDF["metadata"]["Author"])
print(contenuPDF["metadata"]["pdf:charsPerPage"])

### Le texte du PDF en tant que tel se trouve dans la clé «content»:
texte = contenuPDF["content"]
print(texte) ### Vous pouvez ensuite sauvegarder ce texte dans un fichier CSV ou TXT, par exemple, pour utilisation future en traitement du langage naturel