import cv2 as cv
import winsound
import os
import face_recognition_models

FAMILIAR_FACES_DIR = 'knownfaces'
STRANGERS = "unkownfaces"
DEGREE = 0.6
FRAME_THICC = 3
font_thickness = 2
model = "cnn"

known = []
names = []

for name in os.listdir(FAMILIAR_FACES_DIR):
    for filename in os.listdir(f"{FAMILIAR_FACES_DIR}"):
        image = face_recognition_models.load_image_file(f"{FAMILIAR_FACES_DIR}/{name}/{filename}")
        encoding = face_recognition_models.face_encodings(image)[0]
        known.append(encoding)
        names.append(name)

for file in os.listdir(STRANGERS):
    print(file)
    image = face_recognition_models.load_image_file(f"{STRANGERS}/{file}")
    locations = face_recognition_models.face_locations(image, model=model)
    encodings = face_recognition_models.face_encodings(image, locations)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition_models.compare_faces(known, face_encoding, DEGREE)
        match = None
        if True in results:
            match = known[results.index(True)]
            print(f"Match found: {match}")

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])

            color = [0, 255, 50]
            cv.rectangle(image, top_left, bottom_right, color, FRAME_THICC)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)
            cv.rectangle(image, top_left, bottom_right, color, cv.FILLED)
            cv.putText(image, match, (face_location[3]+10, face_location[2]+15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), font_thickness)
    cv.imshow(file, image)
    cv.waitKey(10000)




#camera = cv.VideoCapture(0)

#if not camera.isOpened():
 #   print("Cannot open camera ")
  #  exit()

#while True:

 #   ret, frame = camera.read()
 #   ret, frame2 = camera.read()
 #   #camera.set(cv.CAP_PROP_BUFFERSIZE, 2)
 #   difference = cv.absdiff(frame, frame2)
 #   grey = cv.cvtColor(difference, cv.COLOR_RGB2GRAY)
 #   blurry_img = cv.GaussianBlur(grey, (5, 5), 0)
 #   _, threshold = cv.threshold(blurry_img, 20, 255, cv.THRESH_BINARY)
 #   dilation = cv.dilate(threshold, None, iterations=3)
 #   bound, _ = cv.findContours(dilation, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
 #   for movement in bound:
 #       if cv.contourArea(movement) < 1200:
 #           continue
 #       else:
 #           x_axis, y_axis, width, height = cv.boundingRect(movement)
 #           cv.rectangle(frame, (x_axis, y_axis), (x_axis+width, y_axis+height), (255, 0, 50), 2)
 #           winsound.Beep(500, 200)
 #   if not ret:
 #       print("Cant receive frame. Exiting...")
 #       break

 #   cv.imshow('Cam 1', frame)

 #   if cv.waitKey(1) == ord('q'):
 #       break

#camera.release()
#cv.destroyAllWindows()