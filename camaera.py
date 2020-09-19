import cv2
import numpy as np
cap = cv2.VideoCapture(0)
frame_width=int(cap.get(3))r_fourcc('M','J','P','G'),10,(frame_width,frame_height))
while(True):    #cap.isOpened()
    retr, frame = cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('a') :
        break
cap.release()
out.release()
cv2.destroyAllWindows()
f=np.array(frame)
print(np.size(f))