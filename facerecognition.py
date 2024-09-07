import cv2
import numpy as np
import face_recognition
image_bgr = face_recognition.load_image_file('elon_musk.jpg') # loads image in the form of BGR
image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB) # converts image into RGB
face_location = face_recognition.face_locations(image_rgb)[0] # finds face location
copy_image_rgb = image_rgb.copy()
#cv2.rectangle(image, start_point, end_point, color, thickness) 
cv2.rectangle(copy_image_rgb, (face_location[3], face_location[0]),(face_location[1], face_location[2]), (255,225,25), 2) # draws rectangle
cv2.imshow('copy', copy_image_rgb)
cv2.imshow('elon',image_rgb)
cv2.waitKey(0)
