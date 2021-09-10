import csv
import math
from PIL import Image, ImageDraw
import random

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

for temp in temps:
    red = int( (230 - 8) * ((temp - lowest) / (highest - lowest)) + (8))
    green = int( (24 - 57) * ((temp - lowest) / (highest - lowest)) + (48))
    blue = int( (62 - 107) * ((temp - lowest) / (highest - lowest)) + (107))
    # color = random.choice([(8, 48, 107), (203, 24, 26)])
    img1.rectangle(
        [(start, 0), (start + iterator, h)],
        fill=(red,green,blue)
    )



    if year % 10 == 0:
        img1.text((start+ 5, 50), str(year) ,(255,255,255))

    start += iterator
    year += 1

img.save("fullsize_numbered.png")
