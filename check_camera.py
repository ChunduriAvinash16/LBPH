import cv2
def camera():
    cap = cv2.VideoCapture(0)
    while(True):
        #capture frame-by-frame
        retr,frame  = cap.read()
        #operations on the frame come here
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #display the resulting frame
        cv2.imshow('frame', gray)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # when everything is done
    cap.release()
    cv2.destroyAllWindows()
#camera()