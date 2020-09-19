import datetime
import os
import time
import cv2
from cv2 import face_LBPHFaceRecognizer
import pandas as pd
import sm
#-------------------------
def recognize_attendence():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    #recognizer=cv2.face_FisherFaceRecognizer.create()
    #recognizer=cv2.face_FisherFaceRecognizer.create()
    #recognizer =cv2.face_LBPHFaceRecognizer() # cv2.createLBPHFaceRecognizer()
    #recognizer.read("trainner.yml")
    recognizer.read("trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df=pd.read_csv("data1.csv")
    #df=pd.DataFrame(df1,columns=['Id','Name'])
    #print(df)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            #Id,conf=recognizer.predict(gray[x:x+w,y:y+h])
            if conf < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
            else:
                Id = 'unknow'
                tt = str(Id)
            if(conf > 75):
                noOfFile = len(os.listdir("E:/project/Imagesunknown"))
                cv2.imwrite("E:/project/Imagesunknown/Img"+str(noOfFile)+".jpg", im[y:y+h, x:x+w])
            cv2.putText(im, str(tt), (x, y+h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    #sm.mail(fileName)
    attendance.to_csv(fileName, index=False)
    #attendance.to_csv(fileName, index=False)
    sm.mail(fileName)
    cam.release()
    cv2.destroyAllWindows()
    #sm.mail1(fileName)
    print("Attendance Successfull")
#recognize_attendence()
#print(filename)