from classes.PhotoSource import PhotoSource

from cv2 import cv2
import numpy as np
import requests, ffmpeg

import os

def getAverageColor(img: np.ndarray) -> str:

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

def getImageArrayFromFile(filename: str) -> np.ndarray:

    if not os.path.exists(filename): raise FileNotFoundError

    return cv2.imread(filename)

def getImageArrayFromUrl(url: str, kind: str) -> np.ndarray:

    if kind == "Image":

        resp = requests.get(url)
        image = np.asarray(bytearray(resp.content), dtype="uint8")

        return cv2.imdecode(image, -1)

    if kind == "Stream":

        out, _ = (
            ffmpeg
            .input(url)
            .output('pipe:', format='image2', vcodec='mjpeg', vframes=1)
            .run(capture_stdout=True)
        )

        image = np.asarray(bytearray(out) ,dtype=np.uint8)
        return cv2.imdecode(image, -1)

