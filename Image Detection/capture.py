import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cnt = 0
while(True):
    cnt = cnt+1
    ret, frame = cap.read()
    cv2.imwrite('images/%i.png' %(cnt), frame)
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()