# Jakub Wawak
#2021
# kubawawak@gmail.com

import cv2
import imutils
import numpy as np
import pytesseract
import os
class Numberplate_Detect:

    def __init__(self,path):
        self.img = cv2.imread(path,cv2.IMREAD_COLOR)
        self.img = cv2.resize(self.img, (600,400) )

        if os.path.exists(path):
            print("Path was found")

        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY) 
        self.gray = cv2.bilateralFilter(self.gray, 13, 15, 15) 

        self.edged = cv2.Canny(self.gray, 30, 200) 
        self.contours = cv2.findContours(self.edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contours = imutils.grab_contours(self.contours)
        self.contours = sorted(self.contours, key = cv2.contourArea, reverse = True)[:10]
        self.screenCnt = None

    def run(self):
        for c in self.contours:
            
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            if len(approx) == 4:
                self.screenCnt = approx
                break

        if self.screenCnt is None:
            print ("No contour detected")
            detected = 0
        else:
            detected = 1

        if detected == 1:
            cv2.drawContours(self.img, [self.screenCnt], -1, (0, 0, 255), 3)

            mask = np.zeros(self.gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[self.screenCnt],0,255,-1,)
            new_image = cv2.bitwise_and(self.img,self.img,mask=mask)

            (x, y) = np.where(mask == 255)
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            Cropped = self.gray[topx:bottomx+1, topy:bottomy+1]
            text = pytesseract.image_to_string(Cropped, config='--psm 11')
            print("Detected license plate Number is:",text)
            return text
        else:
            return "none"