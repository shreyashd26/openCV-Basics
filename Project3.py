import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("failed to load the camera..")

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter("canny_video.avi", codec, 20,( frame_width,frame_height))


while True:
    ret, frame = camera.read()
    if ret is False:
        print("failed to laod the image")
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("original video", gray)
    canny = cv2.Canny(frame, 50,150)
    recorded.write(canny)
    cv2.imshow("canny video", canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("video recorded successfully...")
        break
camera.release()
cv2.destroyAllWindows()
