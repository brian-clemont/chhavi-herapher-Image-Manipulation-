import numpy as np 
import matplotlib.pyplot as plt
import cv2

min= 0
max=260
class Dilation:
    def convertDilate(self,original_image):
        self.orig = original_image
        gray_scale = cv2.cvtColor(self.orig,cv2.COLOR_BGR2GRAY)
        cv2.imshow('original',self.orig)
        kernel = np.ones((5,5), np.uint8)
        dilation = cv2.dilate(gray_scale, kernel, iterations=1)
        cv2.imshow('Erosion', dilation)
        plt.title("dilation Graph")
        plt.xlabel("Intesity of Pixels")
        plt.ylabel("Count of pixels")
        plt.hist(dilation.ravel(),256,[min,max])
        cv2.waitKey(0)
        plt.waitforbuttonpress()
        cv2.destroyAllWindows()
        plt.close()