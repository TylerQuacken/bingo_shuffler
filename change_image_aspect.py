import cv2
import glob
import random
import numpy as np
from IPython import embed
from tqdm import tqdm

data_path = "./images/"
images = []
for img in glob.glob(data_path + "*.png"):
    n = cv2.imread(img)
    images.append(n)

new_aspect = 2736/1824
new_height = 650
new_width = int(new_height * new_aspect)
i = 0

for image in tqdm(images):
    resized = np.zeros([new_height, new_width, 3])
    width = image.shape[1]
    height = image.shape[0]

    start_y = (new_height - height)//2
    start_x = (new_width - width)//2

    resized[start_y:start_y+height, start_x:start_x+width] = image

    cv2.imwrite(f"new_images/bingo_{i}.png", resized)
    i += 1

