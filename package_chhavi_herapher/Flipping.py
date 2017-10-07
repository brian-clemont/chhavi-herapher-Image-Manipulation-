import numpy as np
import matplotlib.pyplot as plt
import cv2

class Flipping:
    def horizontal_flip(self, original_image):
        self.orig = original_image
        cv2.imshow('original', self.orig)
        horizontal_img = cv2.flip(self.orig, 0)
        cv2.imshow('Horizontal Flip', horizontal_img) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def vertical_flip(self, original_image):
        self.orig = original_image
        cv2.imshow('original', self.orig)
        horizontal_img = cv2.flip(self.orig, 1)
        cv2.imshow('Vertical Flip', horizontal_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
