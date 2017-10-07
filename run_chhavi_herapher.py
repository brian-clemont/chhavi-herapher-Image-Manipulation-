import numpy as np
import cv2
import sys
from package_chhavi_herapher import DialogImage
from package_chhavi_herapher import GrayScale
from package_chhavi_herapher import ThresHold
from package_chhavi_herapher import Erosion
from package_chhavi_herapher import Dilation
from package_chhavi_herapher import Flipping
from package_chhavi_herapher import Contrast
from package_chhavi_herapher import Crop

dialogImage = DialogImage()
img_path = DialogImage.file_path
original_img = cv2.imread(img_path)
print("CHHAVI HERAPHER")

while True:
    n = raw_input("1.Turn Grayscale\n2.Threshold\n3.Erosion\n4.Dilation\n5.Flipping\n6.Contrast\n7:Cropping\nq: Quit\n")
    if n == '1':
        gray_scale_obj = GrayScale()
        gray_scale_obj.convertGray(original_img)
        print("executed grayscale")

    if n == '2':
        threshold_obj = ThresHold()
        threshold_obj.convertThresh(original_img)
        print("Executed threshold")

    if n == '3':
        erosion_obj = Erosion()
        erosion_obj.convertErode(original_img)
        print("Executed Erosion")

    if n == '4':
        dilation_obj = Dilation()
        dilation_obj.convertDilate(original_img)
        print("Executed Dilation")
    if n == '5':
        flippin_obj = Flipping()
        f = raw_input("\n\tA:Horizontal Flip\n\tB:Vertical Flip")
        if f == 'A':
            flippin_obj.horizontal_flip(original_img)
        if f == 'B':
            flippin_obj.vertical_flip(original_img)
        print("Executed flipping")
    if n == '6':
        contrast_obj = Contrast()
        contrast_obj.autoContrast(original_img)
        print("Executed Contrast")
    if n == '7':
        crop_obj = Crop()
        crop_obj.cropImage(original_img)
        print("Executed Cropping")

    if n == 'q':
        print ("Application closed")
        sys.exit()
