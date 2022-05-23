# Doc Signer
Program to sign a document from an image file inserted in it.

## Installation
Executer la commande suivante pour installer les dépendance :
```sh
pip install -r requirements.txt
```
La version de Python utilisée est : `3.10.4`.

## Utilisation
Je te propose deux interfaces pour utiliser ce module.

### En ligne de commande
- Pour signer un fichier Word :
```sh
python docsg.py -t word -i ./input.docx -s ./qrcode.png -w 128 -e 128 -o ./output.docx

# OU
python docsg.py -t=word -i=./input.docx -s=./qrcode.png -w=128 -e=128 -o=./output.docx

# OU
python docsg.py --type=word --in=./input.docx --simg=./qrcode.png --width=128 --height=128 --out=./output.docx

```
- Pour signer un fichier PDF :

```sh
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png -w 128 -e 128 -o ./output.pdf

# OU
python docsg.py -t=pdf -i=./input.pdf -s=./qrcode.png -w=128 -e=128 -o=./output.pdf

# OU
python docsg.py --type=pdf --in=./input.pdf --simg=./qrcode.png --width=128 --height=128 --out=./output.pdf

```


1. `-t` ou `--type` pour préciser le type du document. Ses valeurs possibles sont `word` et `pdf`.
2. `-i` ou `--in` pour définir le chemin vers le fichier du document qu'on veux signer.
3. `-s` ou `--simg` pour définir le chemin vers le fichier de l'image qui représente la signature.
4. `-w` ou `--width` pour définir la largeur de l'image qui représente la signature.
5. `-h` ou `--height` pour définir la hauteur de l'image qui représente la signature.
6. `-o` ou `--out` pour définir le chemin vers le fichier qui va représente le document signé.

Les paramètres de dimensionnement de l'image de la signature ne sont pas à renseigner obligatoirement. Les
valeurs par défaut de ces dimensions sont `150 x 150`.

#### Positionnement de l'image
Pour positionner l'image sur la page du document, il faut utiliser les arguments `-x` ou `--margin-left` et `-y` ou `--margin-bottom`.
```sh
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png -x 400 -y 10 -o ./output.pdf

# OU
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png --margin-left=400  --margin-bottom=15 -o ./output.pdf

```

Par défaut `x` et `y` valent tous `(10, 10)`.

> **NOTE**: Cette fonctionnalité optionnalle de positionnement ne marche que pour l'option PDF.

#### Selection d'un numéro de page
Pour selectionner le numéro de page sur laquelle on veux positionner l'image, on utilise le paramètre `-n` ou `--page-number`.
```sh
# on veut positionner sur la 2ème page du document.
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png -n 2 -o ./output.pdf

# OU
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png --page-number=2 -o ./output.pdf
```

Par défaut le programme positionne l'image sur la `dernière page` du document.

> **NOTE**: Cette fonctionnalité optionnalle ne marche pas encore pour les document WORD.

### En code python
```python
from docsg import dsg

# Pour signer un fichier Word
input_file  = "infile.docx";
output_file = "outfile.docx";
sign_img    = "sign.png";
dsg.sign(input_file, output_file, sign_img, dsg.DocType.WORD, (80, 80));

# Pour signer un fichier PDF
input_file  = "infile.pdf";
output_file = "outfile.pdf";
sign_img    = "sign.png";
dsg.sign(input_file, output_file, sign_img, dsg.DocType.PDF, (224, 224));


```

Enjoy !
