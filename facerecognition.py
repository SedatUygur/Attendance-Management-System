import cv2
import numpy as np
import face_recognition
image_bgr = face_recognition.load_image_file('elon_musk.jpg') # loads image in the form of BGR
image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB) # convert image into RGB
cv2.imshow('bgr', image_bgr) # show image in the form of BGR
cv2.imshow('rgb', image_rgb) # show image in the form of RGB
cv2.waitKey(0)
