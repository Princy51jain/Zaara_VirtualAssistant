import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    # this is speak func which speak when inp given
    engine.say(audio)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)
    engine.runAndWait()


def WishMe():
    # it greets user acc to time
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif 12 < hour <= 5:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    speak("Your highness, I am Zaara. Please tell me how may I help you.")
    print("Your highness, I am Zaara. Please tell me how may I help you.")


def takeCommand():
    # It takes microphone input from the user and returns string output
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising your words...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Please say that again...")
        print("None")
    return query


if __name__ == '__main__':
    speak("Hello Princy")
    WishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            print("According to wikipedia: ")
            print(result)
            speak(result)

        elif "open google" in query:
            print("Zaara : Opening Google...")
            webbrowser.open("google.com")

        elif "open youtube" in query:
            print("Zaara : Opening Youtube...")
            webbrowser.open("youtube.com")

        elif "open python playlist" in query:
            print("Zaara : Opening Python playlist...")
            webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

        elif "open stack overflow" in query:
            print("Zaara : Opening Stack Overflow...")
            webbrowser.open("stackoverflow.com")

        elif "open pie charm" in query:
            print("Zaara : Opening Pycharm for you...")
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.4\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif "open code" in query:
            print("Zaara : Opening Visual Studio Code...")
            codePath = "C:\\Users\\princ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Zaara : Your Highness the time is {strTime}")
            speak(f"Your Highness the time is {strTime}")

        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print("Zaara : Playing songs for you...")
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))

        elif "news" in query:
            try:
                print("Zaara : Opening news")
                os.startfile("exercise9.py")
            except Exception as e:
                print("Zaara : Sorry, I can't open news for you")
                speak("Sorry, I can't open news for you")

        elif "exit" in query or "quit" in query:
            print("Zaara : Thanks for your time")
            speak("quitting...bye-bye")
            exit()
