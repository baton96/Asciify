from PIL import Image, ImageFont
import numpy as np

'''
from collections import defaultdict
font = ImageFont.load_default()
weights = defaultdict(list)
for i in range(32, 127):
    weights[np.mean(font.getmask(chr(i)))] += [chr(i)]
chars = np.asarray([v[0] for v in weights.values()])
'''

fontSize = ImageFont.load_default().getsize(chr(32))
chars = np.asarray(list(' .,-;*?vIJV7&%#A@80$'))
# ratio = fontSize[1] / fontSize[0]
ratio = 11 / 6
img = Image.open('img.png')
img = np.sum(
    img.resize(
        (int(img.size[0] * ratio), int(img.size[1]))
    ),
    axis=2
)
mi, ma = img.min(), img.max()
img = (
        ((img - mi) / (ma - mi)) * (chars.size - 1)
).astype(int)
with open('asciiText.txt', 'w') as f:
    f.write(
        '\n'.join(
            [''.join(r) for r in chars[img]]
        )
    )
