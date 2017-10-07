import numpy as np
import matplotlib.pyplot as plt
import cv2

min = 0
max = 260

class Erosion:
    def convertErode(self, original_image):
        self.orig = original_image
        gray_scale = cv2.cvtColor(self.orig, cv2.COLOR_BGR2GRAY)
        cv2.imshow('original', self.orig)
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(gray_scale, kernel, iterations=3)
        cv2.imshow('Erosion', erosion)
        plt.title("Erosion Graph")
        plt.xlabel("Intesity of Pixels")
        plt.ylabel("Count of pixels")
        plt.hist(erosion.ravel(), 256, [min, max])
        cv2.waitKey(0)
        plt.waitforbuttonpress()
        cv2.destroyAllWindows()
        plt.close()
