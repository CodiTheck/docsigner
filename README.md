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

#### Positionnement absolue de l'image
Pour positionner l'image sur la page du document, il faut utiliser les arguments `-x` ou `--margin-left` et `-y` ou `--margin-bottom`.
```sh
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png -x 400 -y 10 -o ./output.pdf

# OU
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png --margin-left=400  --margin-bottom=15 -o ./output.pdf

```

Par défaut `x` et `y` valent tous `(32, 32)`.

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

#### Positionnement relatif d'une image
Pour positionner une image une page de document de façon relative, il faut spécifier les arguments suivants:
1. `--bottom-center` pour positionner en bas au centre;
2. `--bottom-right` pour positionner en bas à droite;
3. `--bottom-left` pour positionner en bas à gauche;
4. `--top-center` pour positionner en haut au centre;
5. `--top-right` pour positionner en haut à droite;
6. `--top-left` pour positionner en haut à gauche;
7. `--center-right` pour positionner au centre à droite;
8. `--center-left` pour positionner au centre à gauche;
9. `--center` pour positionner au centre de la page.

Par défaut, le programme positionne l'image en bas à droite de la page (`--bottom-right`). Pour customiser un peu plus
le positionnement, il est posible de spécifier en plus une position absolue pour essayer de déplacer l'image. Prenons,
l'exemple de la commande suivante :

```sh
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png -n 2 -o ./output.pdf --top-right -x 120 -y 50

```
Cette commande place l'image en `haut à droite` de la page `numéro 2` du document PDF `input.pdf` et la décale de `120px`
vers la gauche (valeur de `-x`) et de `50px` vers le bas (valeur de `-y`). Ces modifications sont ensuite enrégistrées dans le
document `output.pdf` pour ne pas impacter le document d'origine `input.pdf`.


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
