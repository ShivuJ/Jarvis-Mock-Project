import pyttsx3 # python text to speech install from command pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes # pip install pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Ma'am")
    elif hour >= 12 and hour<16:
        speak("Good afternoon Ma'am")
    elif hour >= 16 and hour<22:
        speak("Good evening Ma'am")
    else:
        speak("Good night Ma'am")
    speak("Welcome back")
    time()
    date()
    speak("jarvis at your service. Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Shivani/Pictures/Screenshots/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_jokes())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'chrome' in query:
            speak("what should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown-l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s/t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = "C:\\Users\\Shivani\\Desktop\\Every folder\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            
        elif 'remember that' in query:
            speak("what should I remember?")
            data = takeCommand()
            speak("you said to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" +remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()
            
        elif 'offline' in query:
            quit()