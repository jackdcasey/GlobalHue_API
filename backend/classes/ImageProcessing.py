from classes.PhotoSource import PhotoSource

from cv2 import cv2
import numpy as np

import os

def getAverageColor(filename: str) -> str:

    if not os.path.exists(filename): raise FileNotFoundError

    img = cv2.imread(filename)
    img = cv2.resize(img, (150, 150))

    pixels = np.float32(img.reshape(-1, 3))

    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)

    dominant = palette[np.argmax(counts)]
    dominant_hex = [format(int(c), 'x').zfill(2) for c in dominant]
    dominant_str = f"#{''.join(dominant_hex[::-1])}"

    return dominant_str