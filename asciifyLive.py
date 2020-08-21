def show_webcam():
    from cv2 import flip, resize, VideoCapture
    from numpy import asarray, sum
    from os import system
    chars = asarray(list(' .,:;irsXA253hMHGS#9B&@'))
    cam = VideoCapture(0)
    try:
        while True:
            img = cam.read()[1]
            img = sum(
                flip(resize(
                    img, (120, 64),
                    interpolation=0
                ), 0), axis=2
            )
            mi, ma = img.min(), img.max()
            img = (
                    ((img - mi) / (ma - mi)) * 22
            ).astype(int)
            toPrint = '\n'.join(
                [''.join(r) for r in chars[img]]
            )
            system('cls')
            print(toPrint)
    except KeyboardInterrupt:
        cam.release()


show_webcam()