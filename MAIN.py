import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4)
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
            return query
        except speech_recognition.UnknownValueError:
            speak("Sorry, I didn't catch that. Please say that again.")
            return "none"
        except speech_recognition.RequestError:
            speak("I'm unable to reach Google's servers right now.")
            return "none"
        except Exception as e:
            print(f"Error: {e}")
            return "none"

if __name__ == "__main__":  # Corrected syntax issue
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from Greetme import greetMe  # Assuming greetMe exists
            greetMe()
 
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")
                    break
                elif"hello" in query:
                    speak("hello sir . How are u ?")
                elif"i am fine" in query:
                    speak("that's great sir")
                elif"how are you" in query:
                    speak("perfect sir") 
                elif"good morning" in query:
                    speak("Good morning, sir! Hope your day is full of success and joy") 
                elif"good afternoon" in query:
                    speak("Good afternoon, sir! How's your day going?")
                elif"good night" in query:
                    speak("Good night, sir! Wishing you sweet dreams")
elif "google" in query:
    from SearchNow import searchGoogle
    searchGoogle(query)
elif "youtube" in query:
    from SearchNow import searchYoutube
    searchYoutube(query)
elif "wikipedia" in query:
    from SearchNow import searchWikipedia
    searchWikipedia(query) 

                 

    #               elif "good morning" in query:
    #     speak("Good morning, sir! Hope your day is full of success and joy.")

    # elif "good afternoon" in query:
    #     speak("Good afternoon, sir! How's your day going?")

    # elif "good night" in query:
    #     speak("Good night, sir! Wishing you sweet dreams.")   
                
           
                
            
    #           elif "welcome" in query:
    #     speak("Thank you, sir! I'm always here to help.")  
    #             elif"how are u " in query:
    #                 speak("i am very fine sir ?") 
                
    #                

    # elif "what's your name" in query:
    #     speak("I'm your virtual assistant,  sir! JARVIS Here to help whenever you need.")                    
