import cv2

img = input("enter the location of the image =")

image = cv2.imread(img)
print("image loaded suceessfully")
while True:
    ch = input("enter your choice: \n1.convert the image to greyscale\n2.save the image \n3.show the image \n")

    if ch == '1':
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("colour changed successfully")
        c = input("Do you want to :\n1.view the greyscale image \n2.save the greyscale image\n")
        if c == '1':
            cv2.imshow("Grey image", grey)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif c == '2':
            cv2.imwrite("colorchanged2gray.jpg", grey)
        
    elif ch == '2':
        cv2.imwrite("editedimage.jpg",image)
        print("image is saved successfully")
        
    elif ch == '3':
        cv2.imshow("window", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("enter any number to break the loop")
        break
    






