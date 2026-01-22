import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("failed to laod the camera")

while True:
    ret, frame = camera.read()
    if ret is False:
        print("failed to load the frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (13,13), 0)
    cv2.imshow("gaussian ", gaussian)
    canny = cv2.Canny(gaussian, 50,150)
    cv2.imshow("canny video", canny)
    contours,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    save = cv2.drawContours(frame, contours, -1, (0,255,0), 2)
    cv2.imshow("contours video", save)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("video runned successfully..")
        break
camera.release()
cv2.destroyAllWindows()