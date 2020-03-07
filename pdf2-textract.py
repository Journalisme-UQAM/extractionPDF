# coding utf-8

import requests ### pour se connecter en HTTP
import textract ### bibliothèque pour traiter une multitude de types de fichiers, mais sous Mac seulement (ou Linux), malheureusement...
### Je ne voulais pas vous montrer cet outil en classe, car l'installer est complexe.
### Mais une fois installé il permet d'extraire du texte d'une multitude de types de fichiers (selon sa documentation [https://textract.readthedocs.io]):
### .doc et .docx; .odt; .png, .jpg et .gif; .epub; etc...

### Pour fonctionner, textract nécessite donc plusieurs modules complémentaires, et de la patience
### Sous MacOS, il faut d'abord installer Homebrew (https://brew.sh/index_fr)
### Puis il faut entrer les commandes suivantes dans le terminal:
### brew cask install xquartz
### brew install poppler antiword unrtf tesseract swig (cette étape est longue et permet à textract de devenir un véritable couteau suisse de l'extraction de texte)
### pip install textract (en dernier lieu)

### Vous êtes maintenant prêt(e)s à extraire des infos d'un fichier PDF

### ÉTAPE 1 - définir le PDF qu'on souhaite traiter.
### Cette étape peut aussi être placée dans une boucle si on souhaite traiter plusieurs PDFs.
urlRapport = "http://www.ree.environnement.gouv.qc.ca/dossiers/3211-10-021/3211-10-021-20.pdf" ### exemple avec le résumé de l'étude d'impact sur l'environnement du projet GNL Québec rendu public en février 2020.

### ÉTAPE 2 - se connecter au serveur où se trouve le PDF (en prenant soin de se présenter)
entetes = {
    "User-Agent":"Jean-Hugues Roy : Prof. journalisme, UQAM - Salutations au ministre, Benoît Charette, qui est également mon député"
}

req = requests.get(urlRapport, headers = entetes)

### ÉTAPE 3 - il faut écrire le fichier PDF, qui se trouve dans le «content» de la commande «requests» qu'on a fait à l'étape 2, sur notre ordi.
### On lui donne un nom de notre choix. Il n'est pas interdit de choisir un nom plus court.
### On le fait en mode «wb» pour «write binary».
with open("monSupercalifragilistiqueFichierPDF.pdf", "wb") as fichier:
	fichier.write(req.content)

### ÉTAPE 4 - on utilise le «parser» de Tika pour analyser le contenu du PDF et le mettre dans une variable.
### Pour ce faire, on ouvre le fichier qu'on a enregistré à l'étape 3 et on l'ouvre en mode «rb» pour «read binary».
contenuPDF = textract.process("monSupercalifragilistiqueFichierPDF.pdf", method="pdfminer")

### ÉTAPE 5 - la variable dans laquelle on a placé le contenu du PDF est une variable de type texte.
### On peut donc faire simplement un «print» pour y accéder
print(contenuPDF) ### Vous pouvez ensuite sauvegarder ce texte dans un fichier CSV ou TXT, par exemple, pour utilisation future en traitement du langage naturel