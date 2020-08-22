import numpy as np
from PIL import Image, ImageDraw, ImageFont

charWidth, charHeight = ImageFont.load_default().getsize(chr(32))
img = Image.open('img.png')
size = (
    int(img.size[0] * (charHeight / charWidth)),
    int(img.size[1])
)
img = img.resize(size)
arr = np.array(img)
newImg = Image.new(
    'RGBA',
    (charWidth * size[0], charHeight * size[1]),
    (0, 0, 0, 0)
)
draw = ImageDraw.Draw(newImg)
for i, line in enumerate(arr):
    for j, pixel in enumerate(line):
        color = '#%02x%02x%02x%02x' % tuple(pixel)
        draw.text((charWidth * j, charHeight * i), '@', color)
newImg.save('asciiColor.png')
