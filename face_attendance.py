# import the necessary libraries
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import pickle

path = 'training_images' # folder path where our training images are stored, image name must start with person name
images = []
person_names = []
dir_list  = os.listdir(path) # list all files and directories in the path
for file in dir_list: # traverse all image files in the path directory
    current_image = cv2.imread(f'{path}/{file}') # loads an image from the specified file
    images.append(current_image)
    person_names.append(os.path.splitext(file)[0])

def getFaceEncodings(images):
    face_encoding_list = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encoding = face_recognition.face_encodings(image)[0]
        face_encoding_list.append(face_encoding)
    return face_encoding_list

known_face_encodings = getFaceEncodings(images)

def checkAttendance(name):
    with open('Attendance.csv','r+') as f: # create and open a file for reading and writing
        attendance_list = f.readlines()
        name_list = []
        for line in attendance_list:
            entry = line.split(' ')
            name_list.append(entry[0])
        if name not in name_list: # check if the attendee name is already in attendance list
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.write(f'{name} {date} {time}\n') # write attendee name and datetime
        
camera  = cv2.VideoCapture(0) # open default camera for capturing video
while True:
    ret, frame  = camera.read() # returns the next video frame
    if frame is None:
          continue
    resized_frame = cv2.resize(frame,(0,0),None,0.25,0.25) # resize frame by 1/4 for faster processing
    resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB) # convert image to RGB
    # finds face locations and their encodings in the frame
    face_locations_list = face_recognition.face_locations(resized_frame)
    face_encodings_list = face_recognition.face_encodings(resized_frame, face_locations_list)
    for face_encoding, face_location in zip(face_encodings_list,face_locations_list):
        matched_face_encodings = face_recognition.compare_faces(known_face_encodings, face_encoding) # compares face encoding with known face encodings
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding) # returns an array of the distance of all images in training_images directory
        try:
            match_index = np.argmin(face_distances) # The index of the minimum face distance will be the matching face distance
        except ValueError:
            continue
        if matched_face_encodings[match_index]:
            name = person_names[match_index].upper().lower()
            top, right, bottom, left = face_location
            top, right, bottom, left = top*4, right*4, bottom*4, left*4 # scales back up face locations
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2) # draw a bounding box
            # draw a name label
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,255,0), cv2.FILLED) 
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1, (255,255,255), 1)
            checkAttendance(name) # call after finding the matching name
            camera.release()
            break
    cv2.imshow('webcam', frame) # display the captured frame
    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to exit the loop
        break

cv2.destroyAllWindows() # closes all windows
