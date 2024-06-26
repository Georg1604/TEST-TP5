import numpy as np
from PIL import Image


logos_names = [
    "Donald Trump",
    "Barack Obama",
    "Javier Milei",
    "Kim Jong Un",
    "Lionel Messi",
    "Adolf Hitler",
    "Kendrick Lamar",
    "Joe Biden",
]

logos_size = (100, 100)
logos_images = []

def load_logos_images():
    img = np.asarray(Image.open('concatenated_emojisX.png').convert("L"))
    logoss_per_row = img.shape[1] / logos_size[1]
    for i in range(len(logos_names)):
        y = int((i // logoss_per_row) * logos_size[0])
        x = int((i % logoss_per_row) * logos_size[1])
        logos_matrix = img[y:(y + logos_size[1]), x:(x + logos_size[0])] / 255
        logos_vector = logos_matrix.flatten()
        logos_images.append(logos_vector)

load_logos_images()
