import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import sys

listener = sr.Recognizer()

def engine_talk(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def weather(city):
    api_key = "eb7c8571ff5639f7e559db354c3a627e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        kelvin_temp = data["main"]["temp"]
        celsius_temp = kelvin_temp - 273.15
        return f"{round(celsius_temp, 1)} degree Celsius"
    return "City not found"

def user_commands():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"🗣 Command: {command}")
    except:
        pass
    return command

def run_alexa():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '').strip()
        engine_talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk(f"Current time is {time}")
    elif 'who is' in command:
        name = command.replace('who is', '').strip()
        info = wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'weather' in command:
        engine_talk("Please tell me the name of the city or state ")
        city = user_commands()
        temp_info = weather(city)
        engine_talk(temp_info)
    elif 'stop' in command:
        engine_talk("Goodbye Lakshya")
        sys.exit()
    else:
        engine_talk("Sorry, I did not understand.")

while True:
     run_alexa()


