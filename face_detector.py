# Jakub Wawak
#2021
# kubawawak@gmail.com

import cv2
import sys
import os

class Face_Detect:

    # constructor
    def __init__(self,draw_flag):
        self.cascPath = cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        self.imagePath = ""
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.faces = None
        self.draw_flag = draw_flag
        self.photo_loaded = False

    #function for loading photo
    def load_image(self,image_Path):
        if os.path.exists(image_Path):
            self.image = cv2.imread(image_Path)
            self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.photo_loaded = True
        else:
            print("No photo with given path found ("+image_Path+")")

    # face detection
    def detect(self):
        if self.photo_loaded:
            self.faces = self.faceCascade.detectMultiScale(
                    self.gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                    )
            print ("Found {0} faces!".format(len(self.faces)))

            if self.draw_flag == 1:
                # Draw a rectangle around the faces
                print("Preparing window to show")
                for (x, y, w, h) in self.faces:
                    cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow("Faces found", self.image)
                cv2.waitKey(0)

            return len(self.faces)

    
