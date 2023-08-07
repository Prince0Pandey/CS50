import sys
from PIL import Image

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "35.costumes.gif", save_all = True, append_images = [images[1]], duration = 200, loop = 0
)

''' how to run the code
    python 34.costumes.py 32.costume1.gif 33.costume2.gif
'''