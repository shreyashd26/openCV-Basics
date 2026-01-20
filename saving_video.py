import cv2 

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.avi",codec , 20, (frame_width,frame_height))

while True:
    ret, frame = camera.read()
    
    if ret is False:
        print("could not load the video")
    
    recorder.write(frame)
    cv2.imshow("recording_video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video saved successfully")
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()
