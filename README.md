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
valeurs par défaut de ces dimensions sont `128 x 128`.

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
