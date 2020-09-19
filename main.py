import os
import check_camera
import Capture_Image
import Train_Image
import Recognize
import sm
# creating the title bar function


def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Auto Mail")
    print("[6] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                checkCamera()
                break
            elif choice == 2:
                Capture_Image.takeImages()
                mainMenu()
                #CaptureFaces()
                break
            elif choice == 3:
                Train_Image.TrainImages()
                mainMenu()
                #Trainimages()
                break
            elif choice == 4:
                Recognize.recognize_attendence()
                mainMenu()
                #RecognizeFaces()
                break
            elif choice == 5:
                mail()
                #os.system("py automail.py")
                break
                mainMenu()
            elif choice == 6:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-4")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")
    exit


# ---------------------------------------------------------
# calling the camera test function from check camera.py file

def checkCamera():
    check_camera.camera()
    key = input("Enter any key to return main menu")
    mainMenu()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()


# -----------------------------------------------------------------
# calling the train images from train_images.py file

def Trainimages():
    Train_Image.TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()
# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file
def mail():
    sm.mail()
    key=input("Enter any key for main menu")
    mainMenu()


def RecognizeFaces():
    Recognize.recognize_attendence()
    key = input("Enter any key to return main menu")
    mainMenu()



# ---------------main driver ------------------
mainMenu()
