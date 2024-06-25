import numpy as np
from PIL import Image


emoji_names = [
    "Smile",
    "Smile_Closed_Eyes",
    "Smile_teeth",
    "Smile_X",
    "Smile_worry",
    "Smile_basic",
    "Smile_kiss",
    "Smile_blush",
]

emoji_size = (20, 20)
emoji_images = []

def load_emoji_images():
    img = np.asarray(Image.open('concatenated_emojis5.png').convert("L"))
    emoji_per_row = img.shape[1] / emoji_size[1]
    for i in range(len(emoji_names)):
        y = int((i // emoji_per_row) * emoji_size[0])
        x = int((i % emoji_per_row) * emoji_size[1])
        logos_matrix = img[y:(y + emoji_size[1]), x:(x + emoji_size[0])] / 255
        logos_vector = logos_matrix.flatten()
        emoji_images.append(logos_vector)

load_emoji_images()
