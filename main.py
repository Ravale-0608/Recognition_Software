import cv2 as cv
import winsound

camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("Cannot open camera ")
    exit()

while True:

    ret, frame = camera.read()
    ret, frame2 = camera.read()
    difference = cv.absdiff(frame, frame2)
    grey = cv.cvtColor(difference, cv.COLOR_RGB2GRAY)
    blurry_img = cv.GaussianBlur(grey, (5, 5), 0)
    _, threshold = cv.threshold(blurry_img, 20, 255, cv.THRESH_BINARY)
    dilation = cv.dilate(threshold, None, iterations=3)
    bound, _ = cv.findContours(dilation, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for movement in bound:
        if cv.contourArea(movement) < 3000:
            continue
        else:
            x_axis, y_axis, width, height = cv.boundingRect(movement)
            cv.rectangle(frame, (x_axis, y_axis), (x_axis+width, y_axis+height), (255, 0, 50), 2)
            winsound.Beep(500, 200)
    if not ret:
        print("Cant receive frame. Exiting...")
        break

    cv.imshow('Cam 1', frame)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()