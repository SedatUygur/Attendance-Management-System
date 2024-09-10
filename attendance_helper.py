# import the necessary libraries
import glob
import cv2
import face_recognition
import numpy as np
from PIL import Image
import os
from datetime import datetime
import pickle
import unicodedata

class AttendanceHelper:
    def __init__(self):
        pass
    # appendImagesAndPeople function is used for getting images and people in given path
    def appendImagesAndPeople(self, path):
        images = []
        personNames = []
        dir_list  = os.listdir(path) # list all files and directories in the path
        for file in dir_list: # traverse all image files in the path directory
            currentImage = cv2.imread(f'{path}/{file}') # loads an image from the specified file
            images.append(currentImage)
            imageFileName = os.path.splitext(file)[0]
            personName = imageFileName.split('_')[0] if "_" in imageFileName else imageFileName
            personNames.append(personName)
        return images, personNames
    # getFaceEncodings function is used for getting face encodings
    def getFaceEncodings(self, images):
        face_encoding_list = []
        for image in images:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            face_encoding = face_recognition.face_encodings(image)[0]
            face_encoding_list.append(face_encoding)
        return face_encoding_list
    # checkAttendance function is used for marking the attandance in csv
    def checkAttendance(self, name, date, time):
        with open('Attendance.csv','r+') as f: # create and open a file for reading and writing
            attendance_list = f.readlines()
            name_list = []
            for line in attendance_list:
                entry = line.split(' ')
                name_list.append(entry[0])
            if name not in name_list: # check if the attendee name is already in attendance list
                f.write(f'{name} {date} {time}\n') # write attendee name and datetime
    # captureVideo function is used for capturing video from camera, matching face, marking attendance in csv and saving attendee's image and video
    def captureVideo(self, known_face_encodings, person_names, camera_id, scale_factor, box_color, text_color, font_scale, line_thickness, window_name, exit_key):
        selected_person = ""
        now = datetime.now()
        time = now.strftime('%I:%M:%S:%p')
        date = now.strftime('%d-%B-%Y')
        scale_up_factor = int(1 / scale_factor)
        camera  = cv2.VideoCapture(camera_id) # open camera for capturing video
        if (camera.isOpened() == False):  
            print("Error while opening camera")
        frame_width = int(camera.get(3))
        frame_height = int(camera.get(4))
        frame_size = (frame_width, frame_height)
        video = cv2.VideoWriter("{0}{1}.mp4".format('attendance_videos/error/', date), cv2.VideoWriter_fourcc(*'mp4v'), 10, frame_size) # write video file
        while True:
            ret, frame  = camera.read() # returns the next video frame
            if frame is None:
                continue
            video.write(frame) # write initial frame into the video
            resized_frame = cv2.resize(frame,(0,0),None,scale_factor,scale_factor) # resize frame by 1/4 for faster processing
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
                    selected_person = name
                    top, right, bottom, left = face_location
                    top, right, bottom, left = top*scale_up_factor, right*scale_up_factor, bottom*scale_up_factor, left*scale_up_factor # scales back up face locations
                    cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2) # draw a bounding box
                    # draw a name label
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), box_color, cv2.FILLED) 
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, font_scale, text_color, line_thickness)
                    cv2.imwrite('{}{}_{}.{}'.format("attendance_images/", name, date, "png"), frame)
                    self.checkAttendance(name, date, time) # call after finding the matching name
                    video.write(frame) # write the matched frame into the video
                    #self.saveVideo(name, date, frame_size)
                    break
            cv2.imshow(window_name, frame) # display the captured frame
            if cv2.waitKey(1) & 0xFF == ord(exit_key): # press q to exit the loop
                break
        camera.release()
        video.release()
        cv2.destroyAllWindows() # closes all windows
        #rename video
        if selected_person:
            old_video = os.path.join("attendance_videos/error/", "{0}.mp4".format(date))
            new_video = os.path.join("attendance_videos/success/", "{0}_{1}.mp4.".format(selected_person, date))
            os.replace(old_video, new_video)

        return selected_person
    # saveVideo function is used for saving attendee's video
    def saveVideo(self, name, date, size):
        video_folder = 'attendance_videos/'
        video = cv2.VideoWriter("{0}{1}{2}.mp4".format(video_folder, name, date), cv2.VideoWriter_fourcc(*'mp4v'), 10, size)
        image_format = "{}{}".format(os.getcwd(), "/attendance_images/*.png")
        filenames = glob.glob(image_format, recursive=True)
        for filename in filenames:
            img = cv2.imread(filename)
            video.write(img)
        video.release()

    # is_number function is used for checking whether text is number or not
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
    
        try:
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
    
        return False
    # getImagesAndLabels function is used for getting images and labels in given path
    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        # creating empty ID list
        Ids = []
        # now looping through all the image paths and loading the
        # Ids and the images saved in the folder
        Id = 0
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # setting the Id
            Id += 1
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
