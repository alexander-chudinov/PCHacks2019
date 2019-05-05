from imutils import paths
import argparse
import cv2
 
def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()
 
for imagePath in sorted(paths.list_images("images")):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	text = "Not Blurry"
	if fm < 120:
		text = "Blurry"
	#cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
		#cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	#cv2.imshow("Image", image)
	key = cv2.waitKey(0)