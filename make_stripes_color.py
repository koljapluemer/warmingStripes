import csv
import math
from PIL import Image, ImageDraw
import random
import matplotlib
import matplotlib.cm as cm

temps = []

# A1: 7016 x 9933

#08306b rgb 8, 48, 107
#cb181d rgb 230, 57, 62


with open('bavaria_short.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        temps.append(float(row[1]))

w, h = 7016, 9933
# shape = [(40, 40), (w - 10, h - 10)]

# creating new Image object
img = Image.new("RGB", (w, h))

# create rectangle image
img1 = ImageDraw.Draw(img)

start = 0
iterator = int(7016 / len(temps))
lowest = min(temps)
highest = max(temps)

temps.reverse()
print(f"First temperature {temps[0]}")
year = 1881

minima = min(temps)
maxima = max(temps)

norm = matplotlib.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
mapper = cm.ScalarMappable(norm=norm, cmap=cm.plasma)


for temp in temps:
    fill = tuple([round(x * 255) for x in mapper.to_rgba(temp)])
    print(str(year) + ":")
    print(fill)
    img1.rectangle(
        [(start, 0), (start + iterator, h)],
        fill=fill
    )




    if year % 10 == 0:
        img1.text((start+ 5, 50), str(year) ,(255,255,255))

    start += iterator
    year += 1

img.save("fullsize_color.png")
