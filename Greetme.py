import datetime
import pyttsx3

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")
    speak("Please tell me, how can I assist you?")
