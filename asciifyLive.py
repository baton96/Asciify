import numpy as np
import cv2
import os

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        img = cam.read()[1]
        img = np.sum(
            cv2.flip(cv2.resize(
                img,
                (
                    # This should be hardcoded
                    # sth like 480*.25=120
                    # sth like 640*.1=64
                    int(img.shape[0] * .25),
                    int(img.shape[1] * .1)
                ),
                interpolation=cv2.INTER_NEAREST
            ), 0),
            axis=2
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
# show_webcam()
# Get hardcoded cam-image-size from here
print(cv2.VideoCapture(0).read()[1].shape)