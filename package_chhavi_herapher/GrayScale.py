import numpy as np
import matplotlib.pyplot as plt
import cv2

min = 0
max = 260


class GrayScale:
    def convertGray(self, original_image):
        self.orig = original_image
        gray_scale = cv2.cvtColor(self.orig, cv2.COLOR_BGR2GRAY)
        cv2.imshow('original', self.orig)
        plt.title("Grayscale Graph")
        plt.xlabel("Intesity of Pixels")
        plt.ylabel("Count of pixels")
        plt.hist(gray_scale.ravel(), 256, [min, max])
        cv2.imshow('Grayscale', gray_scale)
        cv2.waitKey(0)
        plt.waitforbuttonpress()
        cv2.destroyAllWindows()
        plt.close()
