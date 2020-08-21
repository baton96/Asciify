import os

import cv2
import numpy as np

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))


def show_webcam():
    cam = cv2.VideoCapture(0)
    try:
        while True:
            img = cam.read()[1]
            img = np.sum(
                cv2.flip(cv2.resize(
                    img, (120, 64),
                    interpolation=cv2.INTER_NEAREST
                ), 0), axis=2
            )
            mi, ma = img.min(), img.max()
            img = (
                    ((img - mi) / (ma - mi)) * 22
            ).astype(int)
            toPrint = '\n'.join(
                [''.join(r) for r in chars[img]]
            )
            os.system('cls')
            print(toPrint)
    except:
        cam.release()


show_webcam()
