import pyttsx3
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello Lakshya, this is the first test.")
time.sleep(0.2)
speak("And this is the second test.")
