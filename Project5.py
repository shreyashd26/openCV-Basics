import cv2 

camera = cv2.VideoCapture(0) #provides access to camera 

if not camera.isOpened(): #ignores the error if error is occured
    print("problem loading the camera")

while True:
    ret, frame = camera.read()  #whatever the camera reads, it is stored in the frame and ret checks if it is true or false
    if ret is False:
        print("failed to capture the frame ")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts the frame to grayscale
    blur = cv2.GaussianBlur(gray, (7,7), 0)   #converts the grayscale to gaussian blur
    edges = cv2.Canny(blur, 50, 150)   #converts the gaussian blur to edge view
    contours,_ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #finds the edges to create contours
    for cnt in contours:    #for every contour in contours                            #retr_external-ignores the contours inside the contour
        area = cv2.contourArea(cnt)  #finds the area of the contour                   #chain_approx..- it is used for efficiency
        if area < 800:  
            continue   #skips the contours with area<800
        peri = cv2.arcLength(cnt, True)   #used to find the length of the shape
        approx = cv2.approxPolyDP(cnt, 0.01*peri, True)  #it simplifies the contour line selecting only the corner points 
        cv2.drawContours(frame, [approx],-1, (0,255,0), 2)  #it draws the contour line on the frame 
 #       
        x,y,w,h = cv2.boundingRect(cnt) #it creats a bounding rectangle for the text 
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
             aspect_ratio = w/h
             if 0.95 < aspect_ratio < 1.05:  
                shape = "Square"
             else:
                shape = "Rectangle" 
        elif len(approx) > 4:
            shape = "Circle"
        else:
            shape = "Unknown"
       #syntax for put_text = cv2.putText(frame, shape, loaction, font,font size, color, thickness)
        cv2.putText(frame,shape, (x,y - 10),cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 2) 
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #close the loop after the 'q' key is pressed 
        print("camera closed ")
        break
camera.release()   #free the camera 
cv2.destroyAllWindows()   #destroy all the windows after closing the camera
