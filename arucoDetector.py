import cv2
import cv2.aruco as aruco
import winsound

print(cv2.__version__)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Cannot open camera ")
    exit()
    
# Create an ArUco dictionary (here we use DICT_4X4_50)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

while True:
    ret, frame = camera.read()

    # Detect ArUco markers
    corners, ids, _ = detector.detectMarkers(frame)

    # Draw the detected ArUco markers
    if ids is not None:
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        winsound.Beep(500, 200)  # Play beep when ArUco marker is detected

    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Display the frame with ArUco markers
    cv2.imshow('Cam 1', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
