import csv
import cv2
import pandas as pd
# counting the numbers
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
# Take image function
def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        sampleNum = 0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #faces = detector.detectMultiScale(gray, 1.3, 5)
            faces=detector.detectMultiScale(gray,1.2,5)
            for(x,y,w,h) in faces:
                #cv2.circle(img,x,y,(0,255,0))
                cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255),5)
                #incrementing sample number
                sampleNum = sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("E:/project/traningimages/img"+name + "."+Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                #display the frame
                cv2.imshow('frame', img)
                print(sampleNum)
            #wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        #writer=pd.DataFrame(columns=['Id','Name'])
        with open('data1.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if(is_number(Id)):
            print("Enter Alphabetical Name")
        if(name.isalpha()):
            print("Enter Numeric ID")
#takeImages()