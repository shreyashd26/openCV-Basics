import cv2
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("camra not loaded")

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'mp4v')
recorded = cv2.VideoWriter("Video.mp4", codec, 20, (frame_width,frame_height))

while True:
    ret, frame = camera.read()
    if ret is False:
        print("frame could not be recorded")
        break
    recorded.write(frame)
    cv2.imshow("You Are Live", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video Is saved Successfully..")
        break

camera.release()
cv2.destroyAllWindows()