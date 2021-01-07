# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:33:04 2020

@author: senthil vikram
"""

import json
import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import subprocess
from ecapture import ecapture as ec
from PyDictionary import PyDictionary
import os
import time
import datetime

dict = PyDictionary()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1])

webbrowser.get()
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
webbrowser.get(chrome_path)

newVoiceRate = 145  # controls the speaking speed
engine.setProperty('rate', newVoiceRate)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hours = datetime.datetime.now().hour
    if hours >= 0 and hours < 12:
        speak("Hello there!,Good Morning")
        print("Hello there!,Good Morning")
    elif hours >= 12 and hours < 18:
        speak("Hello there!,Good Afternoon")
        print("Hello there!,Good Afternoon")
    else:
        speak("Hello there!,Good Evening")
        print("Hello there!,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception:
            speak("Pardon me")
            return "none"
        return statement


print('Loading Smiley...')
speak("Loading Smiley")
greet()

if __name__ == '__main__':

    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "mother" in statement:
            speak('Your mother is Sukadha')
            print('Your mother is Sukadha')
            break

        if "open folder " in statement:
            statement = statement.replace("open folder ", "")
            speak('Opening explorer')
            print('Opening explorer')
            # os.system("explorer")
            os.startfile(r"C:\Users\senth\Desktop\Coursera")
            break

        if "sister" in statement:
            newVoiceRate = 110  # controls the speaking speed
            engine.setProperty('rate', newVoiceRate)
            speak('Your sister is Sanjana. Vadu pedda varashtaaou gaadu. vadu oka wirinchi gaadu kooda. naukoo peddagaa teliyadu sorry naukoo mi sister oka worst varashtaaou inkaa virinchi gadu ani maatramei telusu')
            print('Your sister is Sanjana Virishtildol gadaravadu vadiyalaravadou')
            newVoiceRate = 145  # controls the speaking speed
            engine.setProperty('rate', newVoiceRate)

        if "goodbye smiley" in statement or "ok bye smiley" in statement or "stop smiley" in statement:
            speak('See you soon!,Good bye')
            print('See you soon!,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'meaning of' in statement:
            statement = statement.replace("meaning of", "")
            statement = statement.replace("what ", "")
            statement = statement.replace("is ", "")
            statement = statement.replace("the ", "")
            statement = statement.replace(" ", "")
            print(statement)
            meaning = dict.meaning(statement)
            sent1 = "Here is the meaning of " + statement + \
                " as " + str(list(meaning.keys())[0])
            sent2 = list(list(meaning.values())[0])[0]

            print(sent1)
            newVoiceRate = 160
            engine.setProperty('rate', newVoiceRate)
            speak(sent1)
            print(sent2)
            newVoiceRate = 125
            engine.setProperty('rate', newVoiceRate)
            speak(sent2)
            newVoiceRate = 145
            engine.setProperty('rate', newVoiceRate)
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab(
                "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What is the city name?")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin is " +
                      str(current_temperature) +
                      "\n humidity percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am smiley version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Senthil Vikram")
            print("I was built by Senthil Vikram")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search youtube' in statement:
            statement = statement.replace("search youtube ", "")
            # webbrowser.open_new_tab(statement)
            webbrowser.open(
                "https://www.youtube.com/results?search_query=%s" % statement)
            time.sleep(5)
            speak("Here are your search results in youtube")
            time.sleep(5)

        elif 'search stackoverflow' in statement or 'search stack overflow' in statement:
            print(statement)
            statement = statement.replace("search stackoverflow ", "")
            statement = statement.replace("search stack overflow ", "")
            # webbrowser.open_new_tab(statement)
            webbrowser.open(
                "https://stackoverflow.com/search?q=%s" % statement)
            time.sleep(5)
            speak("Here are your search results in stack overflow")
            time.sleep(5)

        elif 'search' in statement:
            statement = statement.replace("search ", "")
            # webbrowser.open_new_tab(statement)
            webbrowser.open("https://google.com/search?q=%s" % statement)
            time.sleep(5)
            speak("Here are your search results in google")
            time.sleep(5)

        # elif 'ask' in statement:
        #     speak('I can answer to computational and geographical questions and what question do you want to ask now')
        #     question=takeCommand()
        #     app_id="R2K75H-7ELALHR35X"
        #     client = wolframalpha.Client('R2K75H-7ELALHR35X')
        #     res = client.query(question)
        #     answer = next(res.results).text
        #     speak(answer)
        #     print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
