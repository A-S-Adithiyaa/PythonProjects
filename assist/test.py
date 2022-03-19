import pyttsx3
import speech_recognition as sr
import json


assistProps = json.load(open('assistProperties.json'))

bot_name = "N-A-N-O, Nano"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[assistProps['g']].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :\t{query}")
    except Exception as e:
        return 'None'

    return query


def change_props():
    v = input("Can you suggest me a name?")
    assistProps['v'] = v

    g = int(input("do you want a male(0) or female voice(1)? : "))
    assistProps['g'] = g

    assistProps = json.dumps(assistProps)
    with open("assistProperties.json", "w") as f:
        f.write(assistProps)
        f.close()


if __name__ == '__main__':
    speak("Hello World, I am " + bot_name)
    
    while(True):
        if 