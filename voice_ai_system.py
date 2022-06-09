# Importing python packages for implementation of Agent
import speech_recognition
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests

# Indication of starting the agent - giving a formal indication on console screen
print('Loading your AI personal assistant - Max')

# Using SAPI as an agent - SAPI is an API used for speech recognition
agent=pyttsx3.init('sapi5')
# Getting the voice for an agent to respond our queries
voices=agent.getProperty('voices')
agent.setProperty('voice','voices[0].id')

# Function to speak so that the agent can respond
def speak(text):
    agent.say(text)
    agent.runAndWait()

# Function to greet the user from an agent for better interaction
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

# Function for taking command from user to an agent so that agent can take the command as an input
def takeCommand():
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio=r.listen(source) # activating listening mode of the agent

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said : {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again") # if agent is unable to interpret our query
            return "None"
        return statement

speak("Loading your AI personal assistant Max")
wishMe()

# Implementing rules for an agent to take decision when user giving input (AGENT BASED MODELLING)
if __name__=='__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        # For exit of an agent to stop interacting with user and responding
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Max is shutting down,Good bye')
            print('your personal assistant Max is shutting down,Good bye')
            break

        # Agent will search the content in wikipedia
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Agent will open youtube for us
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        # Agent will open google for us
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        # Agent will open gmail for us
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        # Agent will inform the temperature for a particular location
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_temperature_celcius = (round ((current_temperature - 273.15), 2))
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in Celsius unit is " +
                      str(current_temperature_celcius) +
                      "\n Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in Celsius unit = " +
                      str(current_temperature_celcius) +
                      "\n Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        # Agent will tell the time
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        # Agent tells his own abilities and who he is
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Max version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow, predict time, search wikipedia, predict weather' 
                  'in different cities, get top headline news from BBC and you can ask me computational or geographical questions too!')

        # Agent tells his creater or name of discovering him
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Mr. Karthik")
            print("I was built by Mr. Karthik")

        # Agent opens stack overflow to do some programming
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        # Agent will show the news from BBC to get latest updates
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.co.uk/news")
            speak('Here are some headlines from the BBC,Happy reading')
            time.sleep(6)

        # Agent performs search operation in web browser
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        # Agent computes or gives geographical responses according to user query
        elif "computational" in statement or "geographical" in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        # Agent will shutdown PC to make sure if we exit from all applications
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
