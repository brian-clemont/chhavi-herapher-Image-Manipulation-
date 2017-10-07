import numpy as np
import matplotlib.pyplot as plt
import cv2

min = 0
max = 260


class Contrast:

    def autoContrast(self, original_image):
        self.orig = original_image
        cv2.imshow('original', self.orig)
        # CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8, 8))
        # convert from BGR to LAB color space
        lab = cv2.cvtColor(self.orig, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)  # split on 3 different channels
        l2 = clahe.apply(l)  # apply CLAHE to the L-channel
        lab = cv2.merge((l2, a, b))  # merge channels
        # convert from LAB to BGR
        contrast_img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        cv2.imshow('Increased contrast', contrast_img)
        plt.title("Contrast Graph")
        plt.xlabel("Intesity of Pixels")
        plt.ylabel("Count of pixels")
        plt.hist(contrast_img.ravel(), 100, [min, max])
        cv2.waitKey(0)
        plt.waitforbuttonpress()
        cv2.destroyAllWindows()
        plt.close()
