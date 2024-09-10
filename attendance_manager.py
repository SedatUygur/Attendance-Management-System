# importing libraries
import tkinter as tk
from tkinter import messagebox
import cv2
import os
import csv
import numpy as np
import pandas as pd

from attendance_helper import AttendanceHelper

attendance_helper = AttendanceHelper()

window = tk.Tk() # creates Tcl interpreter
window.title("Attendance Manager") # sets title bar
window.configure(background='white') # sets background color as white
# spans the widget and extend in one more row or column
window.grid_rowconfigure(0, weight=1) 
window.grid_columnconfigure(0, weight=1)
# sets main label
message = tk.Label(window, text="Attendance Management System", bg="green", fg="white", width=50, height=3, font=('times', 30, 'bold'))
message.place(x=100, y=20)
# sets No label and its text
no_label = tk.Label(window, text="No", width=20, height=2, fg="green", bg="white", font=('times', 15, ' bold '))
no_label.place(x=310, y=200)

no_text = tk.Entry(window, width=20, bg="white", fg="green", font=('times', 15, ' bold '))
no_text.place(x=600, y=215)
# sets Name label and its text
name_label = tk.Label(window, text="Name", width=20, fg="green", bg="white", height=2, font=('times', 15, ' bold '))
name_label.place(x=320, y=300)

name_text = tk.Entry(window, width=20, bg="white", fg="green", font=('times', 15, ' bold '))
name_text.place(x=600, y=315)

# Take Photos is a function used for creating the sample of the images which is used for training the model. It takes 5 Images of every new user
def TakePhotos():
    # No and Name is used for recognising the image
    Id = (no_text.get())
    name = (name_text.get())
 
    # Checking if the ID is numeric and name is Alphabetical
    if(AttendanceHelper.is_number(Id) and name.isalpha()):
        # Opening the primary camera if you want to access the secondary camera you can mention the number as 1 inside the parenthesis
        cam = cv2.VideoCapture(0)
        # Specifying the path to haarcascade file
        harcascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        # Creating the classier based on the haarcascade file.
        detector = cv2.CascadeClassifier(harcascadePath)
        # Initializing the sample number(No. of images) as 0
        sampleNum = 0
        while(True):
            # Reading the video captures by camera frame by frame
            ret, img = cam.read()
            # Converting the image into grayscale as most of the processing is done in gray scale format
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
            # It converts the images in different sizes (decreases by 1.3 times) and 5 specifies the number of times scaling happens
            faces = detector.detectMultiScale(gray, 1.3, 5)

            # For creating a rectangle around the image
            for (x, y, w, h) in faces:
                # Specifying the coordinates of the image as well as color and thickness of the rectangle.
                # Incrementing sample number for each image
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                # Saving the captured face in the dataset folder training_images as the image needs to be trained are saved in this folder
                cv2.imwrite(r"training_images\ " + name + "_" + Id + '_' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # Display the frame that has been captured and drawn rectangle around it.
                cv2.imshow('frame', img)
            # Wait for 100 milliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # Break if the sample number is more than 4
            elif sampleNum > 4:
                break
        # Releasing the resources
        cam.release()
        # Closing all the windows
        cv2.destroyAllWindows()
        # Displaying message for the user
        res = "Photos taken successfully for " + name
        # Creating the entry for the user in a csv file
        row = [Id, name]
        with open(r'training_details\training_details.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            # Entry of the row in csv file
            writer.writerow(row)
        csvFile.close()
        messagebox.showinfo("Info", res)
    else:
        if not(AttendanceHelper.is_number(Id)):
            res = "Enter Numeric Id" 
            messagebox.showerror("Error", res)
        if not(name.isalpha()):
            res = "Enter Alphabetical Name"
            messagebox.showerror("Error", res)
 
# Training the images saved in training image folder
def TrainImages():
    # Local Binary Pattern Histogram is an Face Recognizer algorithm inside OpenCV module used for training the image dataset
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Specifying the path for HaarCascade file
    harcascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    # Creating detector for faces
    detector = cv2.CascadeClassifier(harcascadePath)
    # Saving the detected faces in variables
    faces, Ids = AttendanceHelper.getImagesAndLabels("training_images")
    # Saving the trained faces and their respective ID's in a model named as "trainer.yml".
    recognizer.train(faces, np.array(Ids))
    recognizer.save(r"training_image_labels\trainer.yml")
    # Displaying the message
    res = "Trained images successfully"
    messagebox.showinfo("Info", res)

# For testing phase
def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Reading the trained model
    recognizer.read(r"training_image_labels\trainer.yml")
    harcascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    # Getting the name from "training_details.csv"
    df = pd.read_csv(r"training_details\training_details.csv", encoding='unicode_escape')
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if(conf < 50):
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id)+"-"+aa
            else:
                Id = 'Unknown'
                tt = str(Id)
            if(conf > 75):
                noOfFile = len(os.listdir("unknown_images"))+1
                cv2.imwrite(r"unknown_images\image" +
                            str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h),
                        font, 1, (255, 255, 255), 2)
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()
# For checking attendance
def CheckAttendance():
    images_folder = 'training_images' # folder path where our training images are stored, image name must start with person name
    
    images, person_names = attendance_helper.appendImagesAndPeople(images_folder) # getting images and people in given path
    known_face_encodings = attendance_helper.getFaceEncodings(images) # getting face encodings

    selected_person = attendance_helper.captureVideo(known_face_encodings, person_names, 0, 0.25, (0,255,0), (255,255,255), 1, 1, 'webcam', 'q') # marking attendance in csv and saving attendance image and video

    if selected_person:
        msg = selected_person + " was successfully registered to the system"
        messagebox.showinfo("Info", msg)
    else:
        msg = "The participant could not be registered in the system"
        messagebox.showerror("Error", msg)

takePhotosBtn = tk.Button(window, text="Take Photos", command=TakePhotos, fg="white", bg="green", width=15, height=3, activebackground="Red", font=('times', 15, ' bold '))
takePhotosBtn.place(x=100, y=500)

checkAttendanceBtn = tk.Button(window, text="Check Attendance", command=CheckAttendance, fg="white", bg="green", width=15, height=3, activebackground="Red", font=('times', 15, ' bold '))
checkAttendanceBtn.place(x=350, y=500)

trainImagesBtn = tk.Button(window, text="Train Images", command=TrainImages, fg="white", bg="green", width=15, height=3, activebackground="Red", font=('times', 15, ' bold '))
trainImagesBtn.place(x=600, y=500)

testImagesBtn = tk.Button(window, text="Test Images", command=TrackImages, fg="white", bg="green", width=15, height=3, activebackground="Red", font=('times', 15, ' bold '))
testImagesBtn.place(x=850, y=500)

quitButton = tk.Button(window, text="Quit", command=window.destroy, fg="white", bg="green", width=15, height=3, activebackground="Red", font=('times', 15, ' bold '))
quitButton.place(x=1100, y=500)
 
window.mainloop()
