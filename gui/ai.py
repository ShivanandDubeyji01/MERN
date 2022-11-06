#from curses.ascii import alt
from cProfile import label
from threading import Timer
from time import time
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
import random
from  requests import get
import wikipedia
import sys
import smtplib
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
'''def Takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recongnizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said : {query}")
    except Exception as e:
        speak("Say that Again Please....")
        return "none"'''
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <= 12:
        speak("GOOD MORNING")
    elif hour >12 and hour<18:
        speak("Good Afternoon")
    else :
        speak("Good Morning")
    speak("I am jarvis Sir Please tell me how can i help you")

class MainThread(QThread):
    def __init__(self):

        super(MainThread,self).__init__()
    def run(self):
        #self.query=self.takeCommand(self)
        self.takeCommand()
    def takeCommand(self):
    #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query

    def taskExecution(self):

        #if __name__ == "__main__":
        wish()
        while True:
        #if 1:
            self.query = self.takeCommand().lower()

            if "open notepad" in self.query:
                npath ="C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)
            elif "open command prompt" in self.query:
                kpath="C:\\WINDOWS\\system32\\cmd.exe"
                os.startfile(kpath)
            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("What should I search on google")
                cm = self.takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif "open camera" in self.query:
                vid = cv2.VideoCapture(0)
                while (True):

                    # Capture the video frame
                    # by frame
                    ret, frame = vid.read()

                    # Display the resulting frame
                    cv2.imshow('frame', frame)

                    # the 'q' button is set as the
                    # quitting button you may use any
                    # desired button of your choice
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                # After the loop release the cap object
                vid.release()
                # Destroy all the windows
                cv2.destroyAllWindows()
                '''while True:
                    ret, img = cap.read()
                    cv2.imshow("webcam",img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                    cap.release()
                    cv2.destroyAllWindows()'''

            elif "play music" in self.query:
                music_dir = "C:\\Users\Shivanand\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))
            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"Your address id {ip}")
            elif "wikipedia" in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                #print(results)
                speak(results)
            elif "I love you" in self.query:
                speak("I Love YOU too")


            elif "no thanks" in self.query:
                speak("Thanks for using me sir,have a good day")
                sys.exit()
            speak("Sir do you have any other work")
    

    #Takecommand()

    #speak("Hello ji")
startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
    

    '''def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

        def startTask(self):
            self.ui.movie =QtGui.QMovie("../../../../WALLPAPERS/pythonpics/7LP8.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie =QtGui.QMovie("../../../../WALLPAPERS/pythonpics/T8bahf.gif")
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start()
            timmer=QTimer(self)
            timmer.timeout.connect(self.showtime)
            Timer.start(1000)
            startExecution.start()
        def showtime(self):
            current_time=QTime.currentTime()
            current_date=QDate.currentDate()
            label_time = current_time.toString('hh:mm:ss')
            label_date =current_date.toString(Qt.ISODate)
            self.ui.textBrowser.setText(label_date)
            self.ui.textBrowser_2.setText(label_time)''' 
app=QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())          

            
