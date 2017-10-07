import numpy as np
import matplotlib.pyplot as plt
import cv2

min = 0
max = 260


class ThresHold:
    def convertThresh(self, original_image):
        self.orig = original_image
        gray_scale = cv2.cvtColor(self.orig, cv2.COLOR_BGR2GRAY)
        cv2.imshow('original', self.orig)
        gaus = cv2.adaptiveThreshold(
            gray_scale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        cv2.imshow('Threshold', gaus)
        plt.xlabel("Intesity of Pixels")
        plt.ylabel("Count of pixels")
        plt.title("Threshold Graph")
        plt.hist(gaus.ravel(), 256, [min, max])
        cv2.waitKey(0)
        plt.waitforbuttonpress()
        cv2.destroyAllWindows()
        plt.close()
