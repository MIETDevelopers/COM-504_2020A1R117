import pyttsx3 #pip install pyttsx3
import speech_recognition as sr#
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from tkinter import *
from PIL import ImageTk,Image
global first
first=True
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def starter():
    global first
    if first==True:
        wishMe()
        first=False
    evaluate()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")    

def takeCommand():
    #It takes microphone input from the user and returns string output

   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        cha.set("Listening...")
        print("Listening...")
        l1.update()
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...") 
        cha.set("Recognizing...")
        l1.update()  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        cha.set("")
        l1.update()


    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        cha.set("Please say that again")
        l1.update() 
        return "None"
  
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('2020a1r117@mietjammu.in', 'password')
    server.sendmail('hrithik.koul.7@gmail.com', to, content)
    server.close()

  
def evaluate():
    
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'play music' in query:
            music_dir = r'C:\Users\MyPc\Desktop\Family\KASHMIRI\New folder'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'jarvis exit please' in query:
            quit()
       

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\MyPc\AppData\Local\Programs\Microsoft VS Code\code.exe"
            os.startfile(codePath)
        
        elif 'email to hrithik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "hrithik.koul.7@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

root=Tk()
b1=Button(command=starter)
im=Image.open("mic.jpg")
image=ImageTk.PhotoImage(im)

b1.config(image=image)

b1.pack()
cha=StringVar()
l1=Label(root,text="",textvariable=cha)
cha.set("Tap to speak?")
l1.pack()

root.mainloop()