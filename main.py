# Script réalisé avec amour par Théo Migeat ~

# Import des bibliothèques
from PIL import Image
import pprint

# Variable d'initialisation
img = Image.open('img.png')  # Chemin vers l'image étant dans le dossier
pix = img.load()

# Le décalage correspond à la position ou l'image sera réalisée sur le drapeau
decalageDesertX = 200
decalageDesertY = 208

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
