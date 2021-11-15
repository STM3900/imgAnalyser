# Script réalisé avec amour par Théo Migeat ~

# Import des bibliothèques
from PIL import Image
import pprint
import json

# Variable d'initialisation
img = Image.open('img.png')  # Chemin vers l'image étant dans le dossier
pix = img.load()

# Le décalage correspond à la position ou l'image sera réalisée sur le drapeau
decalageDesertX = 200
decalageDesertY = 150

# Affichage d'informations dans la console
print("Taille de l'image : {} pixels".format(img.size))
print("Décalage X : {}".format(decalageDesertX))
print("Décalage Y : {}".format(decalageDesertY))

# Déclaration de la largeur et de la longueur de l'image
width = img.size[0]
height = img.size[1]

# Dictionnaire qui contiendra pour chaque pixel sa couleur
colorTab = {}

# Remplissage du dictionnaire
for i in range(width):
    for j in range(height):
        color = pix[i, j]
        colorFiltered = '#%02x%02x%02x' % (
            color[0], color[1], color[2])  # Conversion en Héxadécimal
        colorTab["{}:{}".format(i + decalageDesertX,
                                j + decalageDesertY)] = (colorFiltered)  # Le décalage prend effet ici

# Dictionnaire qui contiendra les pixels correspondant à une couleur
finalDict = {}

# Remplissage du dictionnaire
for key, value in colorTab.items():
    if value not in finalDict:
        finalDict[value] = [key]
    else:
        finalDict[value].append(key)

# Affichage en console du dictionnaire
pprint.pprint(finalDict)

# Écriture du dictionnaire dans un fichier texte
f = open("data.txt", "w+")

for key, value in finalDict.items():
    f.write('%s:%s\n\n' % (key, value))

f.close()

# Écriture du dictionnaire dans un fichier json
with open('data.json', 'w') as convert_file:
    convert_file.write("[" + json.dumps(finalDict) + "]")
