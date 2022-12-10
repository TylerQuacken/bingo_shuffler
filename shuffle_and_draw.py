import cv2
import glob
import random
from IPython import embed

data_path = "./images/"
images = []
for img in glob.glob(data_path + "*.png"):
    n = cv2.imread(img)
    images.append(n)

random.shuffle(images)

cv2.namedWindow("foo", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("foo", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

for image in images:
    cv2.imshow("foo", image)
    key = cv2.waitKey()

    if key == 27 or key == 113:
        break

cv2.destroyWindow("foo")