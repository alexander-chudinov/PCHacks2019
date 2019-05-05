from imutils import paths
import argparse
import cv2
import datetime
 
def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

img_num = 0
file = open("data.txt", "a")
for imagePath in sorted(paths.list_images("images")):
	img_num = img_num+1
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	if fm < 120:
		file.write(str(datetime.datetime.now())+";")
	key = cv2.waitKey(0)
file.close()