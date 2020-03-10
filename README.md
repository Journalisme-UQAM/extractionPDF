# extractionPDF
Trois tutoriels en forme de scripts sur les façons d'extraire le texte de fichiers PDF à l'aide de python

---

## Façon 1 - Tika
Le script [**pdf1-tika.py**](pdf1-tika.py) explique comment il est possible d'extraire le texte de fichiers PDF «natifs» à l'aide de la bibliothèque [_**Tika**_](https://github.com/chrismattmann/tika-python). Celle-ci exige cependant que vous ayez installé [*Java*](https://java.com/en/download/help/download_options.xml) sur votre ordinatruc.<br>
En guise d'exemple, le script extrait le texte de ce [rapport du Bureau de la vérificatrice générale](https://www.vgq.qc.ca/Fichiers/Publications//rapport-annuel//1987-1988//fr_Rapport1987-1988.pdf).

## Façon 2 - Textact
Le script [**pdf2-textract.py**](pdf2-textract.py) indique pour sa part comment faire la même chose, mais à l'aide de la bibliothèque [**_textract_**](https://textract.readthedocs.io). Cette dernière ne fonctionne malheureusement que sous MacOS&nbsp;X et son installation peut prendre beaucoup de temps. Mais textract permet aussi d'extraire des fichiers Word (.doc et .docx), du texte provenant d'images (elle fait donc de la reconnaissance optique de caractères) et même des livres électroniques (.epub).<br>
En guise d'exemple, le script extrait le texte de ce [résumé de l'étude d'impact sur l'environnement du projet GNL Québec publié en février 2020](http://www.ree.environnement.gouv.qc.ca/dossiers/3211-10-021/3211-10-021-20.pdf).

## Façon 3 - pyTesseract
Le script [**pdf3-tesseract.py**](pdf3-tesseract.py) donne enfin la marche à suivre pour extraire le texte de fichiers PDF de type «image» qui font généralement chier les journalistes. On y parvient au moyen de la **reconnaissance optique de caractères** et de [**_Tesseract_**](https://github.com/tesseract-ocr/tesseract) ou, plus précisément, de la bibliothèque [_**pytesseract**_](https://pypi.org/project/pytesseract/). Les résultats sont généralement assez bons.<br>
En guise d'exemple, ici, le script extrait le texte de cette [réponse de la Sûreté du Québec à une demande d'accès à l'information](https://www.sq.gouv.qc.ca/wp-content/uploads/2019/10/2019-10-23-stats-vols-identite-fraudes-identite.pdf).
