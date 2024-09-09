from attendance_helper import AttendanceHelper

attendance_helper = AttendanceHelper()

images_folder = 'training_images' # folder path where our training images are stored, image name must start with person name
images, person_names = attendance_helper.appendImagesAndPeople(images_folder)

known_face_encodings = attendance_helper.getFaceEncodings(images)

attendance_helper.captureVideo(known_face_encodings, person_names, 0, 0.25, (0,255,0), (255,255,255), 1, 1, 'webcam', 'q')
