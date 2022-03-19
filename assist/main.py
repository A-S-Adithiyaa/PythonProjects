import pyttsx3
import datetime
import speech_recognition as sr
import wolframalpha
import time
import json
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests
from bs4 import BeautifulSoup


assistProps = json.load(open('assistProperties.json'))
bot_name = "Nano"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[assistProps['g']].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    
    return query


def change_props():
    assistProps = json.load(open('assistProperties.json'))
    v = input("Can you suggest me a name?")
    assistProps['v'] = v

    g = int(input("do you want a male(0) or female voice(1)? : "))
    assistProps['g'] = g

    bot_name = assistProps['v']
    engine.setProperty('voice', voices[assistProps['g']].id)
    wishMe(bot_name)

    assistProps = json.dumps(assistProps)
    with open("assistProperties.json", "w") as f:
        f.write(assistProps)
        f.close()


def wishMe(bot_name):
    statement = "I am, " + bot_name + ". Hope you are doing great!"
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir, " + statement)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir, " + statement)
    else:
        speak("Good Evening Sir, " + statement)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(assistProps["email"], assistProps["password"])
    server.sendmail(assistProps["email"], to, content)
    server.close()


if __name__ == '__main__':
    wishMe(bot_name)
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'change properties' in query:
            change_props()
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            time.sleep(5)

        elif 'open google' in query:
            webbrowser.open("google.com")
            time.sleep(5)

        elif 'play music' in query:
            music_dir = "D:\Musics"
            songs = os.listdir(music_dir)
            num = random.randint(0, len(songs))
            speak(f"Playing {songs[num]} now")
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'current time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the current time is {time}")
            speak(f"Sir, the current time is {time}")

        elif 'open code editor' in query:
            path = r"C:\Users\Adithiyaa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
            os.startfile(path)

        elif 'answer this' in query:
            ques = query
            client = wolframalpha.Client(assistProps["wolframalpha"])
            res = client.query(ques)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'news' in query:
            url = 'https://timesofindia.indiatimes.com/home/headlines'
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            # headlines = soup.find('body').find_all('h3')
            headlines = soup.find_all("span", {"class": "w_tle"})
            for i in range(5):
                print(headlines[i+1].text.strip())
                speak(headlines[i+1].text.strip())

        elif 'send mail' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                # content = "Hello, i am assist!"
                to = assistProps["to"]
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir, i could not send the mail")

        elif 'exit the program' in query:
            print("GoodBye Sir")
            speak("GoodBye Sir")
            break