
import pyttsx3
import pywhatkit #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
from googletrans import Translator
import requests
from bs4 import BeautifulSoup 
from tkinter import *
from PIL import ImageTk,Image
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Maggie. Please tell me how may I help you")

def takeCommand():
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

def temp():
    search = "temperature" 
    url = "https://www.google.com/search?q=" + search
    r =requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    speak("The temperature is "+temperature)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        #OPEN YT
        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")
        
        #OPEN GOOGLE
        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("google.com")
        
        #OPEN INSTAGRAM
        elif 'open instagram' in query:
            speak("opening instagram...")
            webbrowser.open("instagram.com")
        
        #OPEN FACEBOOK
        elif 'open facebook' in query:
            speak("opening facebook...")
            webbrowser.open("facebook.com")
        
        elif 'open classroom' in query:
            speak("opening google classroom...")
            webbrowser.open("classroom.google.com")
         
        elif "tell me your name" in query:
            speak("I am Maggie. Your deskstop Assistant")    

        elif 'open gmail' in query:
            speak("opening gmail...")
            webbrowser.open("mail.google.com/mail/u/0/")  

        elif 'open mail' in query:
            webbrowser.open("mail.google.com/mail/u/0/")

        elif 'open gmail' in query:
            speak("opening gmail...")
            webbrowser.open("mail.google.com/mail/u/0/")
        
        elif 'open geek for geek' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open soundcloud' in query:
            webbrowser.open("soundcloud.com")
        
        elif 'opn spotify' in query:
            webbrowser.open("open.spotify.com")
        
        elif 'open gaana' in query:
            webbrowser.open("gaana.com")
        
        elif 'open apple music' in query:
            webbrowser.open("music.apple.com/us/browse")

        elif 'open itunes' in query:
            webbrowser.open("apple.com/in/itunes/")
        
        elif 'open shazam' in query:
            webbrowser.open("shazam.com")

        elif 'open youtube music' in query:
            webbrowser.open("music.youtube.com/")
        
        elif 'open amazon' in query:
            webbrowser.open("amazon.in")

        elif 'open prime' in query:
            webbrowser.open("primevideo.com")
        
        elif 'open amazon prime' in query:
            webbrowser.open("primevideo.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")
        
        elif 'open disney hotstar' in query:
            webbrowser.open("hotstar.com")
        
        elif 'open swiggy' in query:
            webbrowser.open("swiggy.com")

        elif 'open zomato' in query:
            speak("opening zomato...")
            webbrowser.open("zomato.com")

        elif 'open uber' in query:
            webbrowser.open("https://uber.com")

        elif 'open ola' in query:
            webbrowser.open("olacabs.com")
        
        elif 'open discord' in query:
            webbrowser.open("discord.com")

        elif 'open 1 3 3 7 x' in query:
            webbrowser.open("1337x.tw")
        
        elif 'open yahoo' in query:
            webbrowser.open("in.search.yahoo.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")
            
        elif 'open shadi.com' in query:
            webbrowser.open("www.shaadi.com")    
        
        elif 'open w3school' in query:
            speak("opening w3school...")
            webbrowser.open("w3schools.com")
          
        elif 'Atharva College Of Enginnering' in query:
            webbrowser.open("atharvacoe.ac.in")
        
        elif 'Visual Studio code ' in query:
            codepath = "C:\\Users\\PRATHMESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)         
            
        elif 'play music' in query:
             music_dir = "D:\\music"  
             music = os.listdir(music_dir)
             os.startfile(os.path.join(music_dir,music[0])) 
                
        #TIME
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        #GOOGLE SEARCH
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("google search"," ")
            query = query.replace("google"," ")
            speak("This are the results of the following search")
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query,3)
                speak(result)
            except:
                speak(" ")
        
        #REMINDER
        elif 'remind me to' in query:    
            rememberMsg = query.replace("remind me to", " ")
            speak("You told me to remind you that : "+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()
        
        #REMINDER2
        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            speak("You told me that" + remember.read())
       
        #TEMPERATURE
        elif 'temperature' in query:
            temp()
         
        # this will exit and terminate the program
        elif "bye" in query:
            speak("Alright Have a great day")
            exit()    

