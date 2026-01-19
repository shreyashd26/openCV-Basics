import cv2

img = input("enter the image address=")

image = cv2.imread(img)
while True:
    ch = int(input("enter your choice:\n1.Add a text on the image\n2.draw a line \n3.draw a rectangle" \
    "9\n4. draw a circle\nENTER ANY KEY TO EXIT THE LOOP"))
    if ch == 1:
        text = input("enter the text=")
        x = int(input("enter the value of x ="))
        y = int(input("enter the value of y ="))
        cv2.putText(image, text, (x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,255,255), 2)
        cv2.imshow("after text image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif ch == 2:
        x1 = int(input("enter the value of x1="))
        y1 = int(input("enter the value of y1="))
        x2 = int(input("enter the value of x2="))
        y2 = int(input("enter the value of y2="))
        cv2.line(image,(x1,y1),(x2,y2),(0,255,255),7)
        cv2.imshow("line image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif ch == 3:
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))

        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))

        cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,255),7)
        cv2.imshow("line image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif ch == 4:
        x = int(input("enter the value of the centre point x="))
        y = int(input("enter the value of the centre point y="))
        radius = int(input("enter the radius of the circle="))
        cv2.circle(image, (x,y), radius, (0,255,255),7)
        cv2.imshow("circle in image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else :
        break

