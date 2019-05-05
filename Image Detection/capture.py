import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cnt = 0
while(True):
	cnt = cnt+1
    # Capture frame-by-frame
	ret, frame = cap.read()
    # do what you want with frame
    #  and then save to file
	cv2.imwrite('images/%i.png' %(cnt), frame)
	if cv2.waitKey(100) & 0xFF == ord('q'): # you can increase delay to 2 seconds here
		break

cap.release()
cv2.destroyAllWindows()