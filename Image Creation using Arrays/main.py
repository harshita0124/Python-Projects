import numpy as np
from PIL import Image

# 0 -> black
# 255 -> white

array_image = np.array([[0, 0, 0, 0, 0, 0],
                        [255, 255, 255, 255, 255, 255],
                        [0, 0, 0, 255, 255, 255],
                        [255, 255, 255, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [255, 255, 255, 255, 255, 255],
                        [255, 255, 255, 255, 255, 0],
                        [0, 0, 255, 255, 255, 255],
                        [0, 0, 0, 0, 0, 0]], dtype = np.int32)

image = Image.fromarray(array_image, mode = "L")

image.save("test1.png")

