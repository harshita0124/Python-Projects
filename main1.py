import numpy as np
from PIL import Image

array_image = np.random.randint(0, 256, (64, 64), dtype = np.uint8)

image = Image.fromarray(array_image, mode = "L" )

image.save("test2.png")