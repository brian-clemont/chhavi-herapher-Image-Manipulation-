import numpy as np
import matplotlib.pyplot as plt
import cv2


class Crop:
    def cropImage(self, original_image):
        self.orig = original_image
        r = cv2.selectROI("Select Crop Region", self.orig, 0)        
        imCrop = self.orig[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        cv2.imshow("Cropped Image", imCrop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
