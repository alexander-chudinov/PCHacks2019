from imutils import paths
import cv2
import datetime
 
def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

file = open("data.txt", "a")
for imagePath in sorted(paths.list_images("images")):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    if fm < 175:
        file.write(str(datetime.datetime.now())+";")
        cv2.imshow("Image", image)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
file.close()