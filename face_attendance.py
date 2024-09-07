# import the necessary libraries
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import pickle

path = 'training_images' # folder path where our training images are stored, image name must start with person name
images = []
personNames = []
dir_list  = os.listdir(path) # list all files and directories in the path
for file in dir_list: # traverse all image files in the path directory
    current_image = cv2.imread(f'{path}/{file}') # loads an image from the specified file
    images.append(current_image)
    personNames.append(os.path.splitext(file)[0])

def getFaceEncodings(images):
    face_encoding_list = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encoding = face_recognition.face_encodings(image)[0]
        face_encoding_list.append(face_encoding)
    return face_encoding_list

face_encoded_images = getFaceEncodings(images)

def checkAttendance(name):
    with open('Attendance.csv','r+') as f: # create and open a file for reading and writing
        attendance_list = f.readlines()
        name_list = []
        for line in attendance_list:
            entry = line.split(',')
            name_list.append(entry[0])
        if name not in name_list: # check if the attendee name is already in attendance list
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name} {date} {time}') # write attendee name and datetime
        
camera  = cv2.VideoCapture(0) # create a video capture object for the camera
while True:
    ret, img  = camera.read() # read the frames
    if img is None:
          continue
    edited_image = cv2.resize(img , (0,0), None, 0.25,0.25) # resize image by 1/4 for better fps
    edited_image = cv2.cvtColor(edited_image, cv2.COLOR_BGR2RGB) # convert image to RGB
    face_locations_list = face_recognition.face_locations(edited_image)
    face_encodings_list = face_recognition.face_encodings(edited_image, face_locations_list)
    for face_encoding, face_location in zip(face_encodings_list,face_locations_list):
        matched_faces = face_recognition.compare_faces(face_encoded_images, face_encoding)
        face_distances = face_recognition.face_distance(face_encoded_images, face_encoding) # returns an array of the distance of all images in training_images directory
        try:
            match_index = np.argmin(face_distances) # The index of the minimum face distance will be the matching face
        except ValueError:
            continue
        print(match_index)
        if matched_faces[match_index]:
            name = personNames[match_index].upper().lower()
            y1,x2,y2,x1 = face_location
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4 # face bounding box coordinates must be multiplied by 4 to overlay on output frame
            cv2.rectangle(img ,(x1,y1),(x2,y2),(0,255,0),2) # draw a bounding box
            cv2.rectangle(img , (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img , name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2) # put the matching name on the output frame
            checkAttendance(name) # call after finding the matching name
            camera.release()
            break
    cv2.imshow('webcam', img) # display the captured frame
    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to exit the loop
        cv2.destroyAllWindows()
        break
