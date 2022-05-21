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
python docsg.py -t word -i ./input.docx -s ./qrcode.png -o ./output.docx

# OU
python docsg.py -t=word -i=./input.docx -s=./qrcode.png -o=./output.docx

# OU
python docsg.py --type=word --in=./input.docx --simg=./qrcode.png --out=./output.docx

```
- Pour signer un fichier PDF :

```sh
python docsg.py -t pdf -i ./input.pdf -s ./qrcode.png -o ./output.pdf

# OU
python docsg.py -t=pdf -i=./input.pdf -s=./qrcode.png -o=./output.pdf

# OU
python docsg.py --type=pdf --in=./input.pdf --simg=./qrcode.png --out=./output.pdf

```


1. `-t` ou `--type` pour préciser le type du document. Ses valeurs possibles sont `word` et `pdf`.
2. `-i` ou `--in` pour définir le chemin vers le fichier du document qu'on veux signer.
3. `-s` ou `--simg` pour définir le chemin vers le fichier de l'image qui représente la signature.
4. `-o` ou `--out` pour définir le chemin vers le fichier qui va représente le document signé.


### En code python
```python
from docsg import dsg

# Pour signer un fichier Word
input_file  = "infile.docx";
output_file = "outfile.docx";
sign_img    = "sign.png";
dsg.sign(input_file, output_file, sign_img, dsg.DocType.DOCX);

# Pour signer un fichier PDF
input_file  = "infile.pdf";
output_file = "outfile.pdf";
sign_img    = "sign.png";
dsg.sign(input_file, output_file, sign_img, dsg.DocType.PDF);


```

Enjoy !
