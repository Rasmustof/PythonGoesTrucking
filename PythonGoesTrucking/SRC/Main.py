import numpy as np
import cv2
import time
from mss import mss

mon = {'top': 0, 'left': 0, 'width': 1280, 'height': 720}
sct = mss()


def process_img(image):
    original_image = image
    processed_img = cv2.Canny(original_image, threshold1=200, threshold2=300)
    return processed_img


def main():
    last_time = time.time()
    while (True):
        screen = np.array(sct.grab(mon))
        #print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()
