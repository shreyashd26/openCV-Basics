import cv2

image = cv2.imread(r"C:\Users\batma\OneDrive\Desktop\opencv\PROJECTS\python_image.jpg")

if image is None:
    print("error loading the image")
else:    
    h, w, c = image.shape
    print(f"height={h}, weidth = {w}, colors={c}") 
    
    cv2.imshow("original image", image )
    #resized_image 
    resized = cv2.resize(image,(300,300))
    cv2.imshow("resized image", resized)
    cv2.imwrite("resized_.jpg", resized)
    #gray_image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("greyscale_image.jpg", gray_image)
    cv2.imwrite("gray_image.jpg", gray_image)
    #Gaussian_blur
    gaussian = cv2.GaussianBlur(image, (5,5),0)
    cv2.imshow("gaussian_blur_image",gaussian)
    cv2.imwrite("gaussian_blur.jpg", gaussian)

    cv2.waitKey(0)
    cv2.destroyAllWindows()