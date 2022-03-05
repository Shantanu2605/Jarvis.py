import secrets
import random
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import requests
import wolframalpha
from colorama import Fore
import pyjokes
from ecapture import ecapture as ec
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#300 LINES OF CODE!! + 85 MB STORAGE

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

api_address= "https://newsapi.org/v2/top-headlines?country=in&apiKey=caf70454c2ad4c9f9154c05cb6f3e2b1"
api2_address= "https://newsapi.org/v2/top-headlines?country=us&apiKey=caf70454c2ad4c9f9154c05cb6f3e2b1"
api3_address= "https://newsapi.org/v2/top-headlines?country=au&apiKey=caf70454c2ad4c9f9154c05cb6f3e2b1"
json_data= requests.get(api_address).json()
json_data1= requests.get(api2_address).json()
json_data2= requests.get(api3_address).json()
ar= []
def news():
    for i in range(3):
        ar.append("Number " + str(i+1)+ ", " + json_data["articles"][i]["title"]+".")
        ar.append("Number " + str(i+2)+ ", " + json_data1["articles"][i]["title"]+".")
        ar.append("Number " + str(i+3) + ", " + json_data2["articles"][i]["title"] + ".")

        return ar

def temperature():
    api= "http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=c537febf3883b416549674aed73affcc"
    json_data3= requests.get(api).json()
    temperature= round(json_data3["main"]["temp"]-273,1)
    return temperature
def des():
    api= "http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid="
    json_data3= requests.get(api).json()
    description= json_data3["weather"][0]["description"]
    return description
def humidity():
    api = "http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid="
    json_data3 = requests.get(api).json()
    humidity= json_data3["main"]["pressure"]
    return humidity

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    d10= ['I am Jarvis. How may I help you!','Jarvis O point in your service sir!',
          'Why did you remembered me today ?','I am Jarvis, online and ready for your command!!']
    speak(random.choice(d10))

def closeapp():
    speak("Ok sir")
    if "browser" in query:
     os.system("TASKKILL /F /IM msedge.exe")
    elif "app" in query or "zoom":
     os.system("TASKKILL /F /IM Zoom.exe")
    elif "google" in query:
     os.system("TASKKILL /F /IM msedge.exe")
    elif "pycharm" in query:
     os.system("TASKKILL /F /IM pycharm64.exe")
    elif "close microsoft word" in query:
        os.system("TASKKILL /F /IM WINWORD.EXE")
    elif "close this" in query or "close it" in query:
      os.system("TASKKILL /F /IM msedge.exe")
      os.system("TASKKILL /F /IM Zoom.exe")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail', '189')
    server.sendmail('@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        features= "html.parser"
        if 'wikipedia' in query or 'search about' in query or 'tell me about' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                query = query.replace("search about", "")
                query= query.replace("tell me about", "")
                query= query.replace("Jarvis", "")
                results = wikipedia.summary(f'{query}', sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Due to this error, I am unable to process the command")

        elif 'exit' in query or 'quit' in query or 'bye' in query or 'go to sleep' in query:
            d4= ['Quitting sir, thank you for your time, You can call me any time if you want any help',
                 'Ok sir, I will be always ready for your command','Ok sir, I am going to sleep now']
            speak(random.choice(d4))
            exit()

        elif "where is" in query:
            query = query.replace("where is", "")
            query = query.replace("Jarvis", "")
            query = query.replace("tell me", "")
            location = query
            speak(f"You asked for the location of {query}")
            webbrowser.open("https://maps.google.com/?q=" + location + "")


        elif 'wow' in query or 'amazing' in query or 'incredible' in query or 'good' in query or'handsome' in query:
            d5= ['Thanks Boss','Thank You Sir, its my pleasure to help you!!']
            speak(random.choice(d5))

        elif 'calculate' in query:
            query= query.replace("calculate", "")
            query= query.replace("divided by", "/")
            query= query.replace("multiplied by", "*")
            query= query.replace("subtract","-")
            query= query.replace("add","+")
            webbrowser.open("https://www.google.com/search?q=calculate+" + query + "&oq=calculate+7*8&aqs=chrome..69i57.7092j0j9&sourceid=chrome&ie=UTF-8")
            speak("Here are the results")

        elif 'open microsoft word' in query:
            speak("Ok sir! As you wish!!!!")
            codepath2= "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(codepath2)

        elif 'date' in query:
            date= datetime.date.today()
            speak(f"Sir, today is {date}")

        elif 'close' in query:
            closeapp()


        elif 'meaning of' in query or 'means' in query:
            query= query.replace("meaning of","")
            query= query.replace("Jarvis","")
            query= query.replace("tell me the","")
            webbrowser.open("https://www.google.com/search?q=meaning+of+" + query +"&oq=meaning+of+&aqs=chrome..69i57.4962j0j1&sourceid=chrome&ie=UTF-8")
            speak(f"Here is the meaning of {query}")

        elif 'take a photo' in query or 'camera' in query:
            speak("Currently I am unable to take photos, but maybe sometime later....")

        elif 'open youtube' in query:
            speak("Ok sir!")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Ok sir!")
            webbrowser.open("google.com")

        elif '.com' in query or '.in' in query:
            webbrowser.open(query)
            speak("Opening" + query)

        elif 'your age' in query or 'how old are you' in query:
            speak("Sorry!! but I don't tell anyone my age")

        elif 'stupid' in query or 'fake' in query or 'dumb' in query or 'idiot' in query or 'useless' in query:
            speak("I am trying to help you, I am still at learning stage, so mind your words!")

        elif 'your friend' in query or 'your family' in query:
            speak("You are my friend, you are my family, you're everything for me sir!")

        elif 'mam' in query:
            d1= ['Okay then, you are not my boss, I should have understood in the beginning',
                 'Ohh! you are not my boss! sorry but, I wont do any task for you',
                 'The system is being used by a stranger, no access to you!!']
            speak(random.choice(d1))
            print(Fore.LIGHTRED_EX + "ACCESS DENIED")
            print(Fore.LIGHTRED_EX + "YOU CAN'T USE JARVIS")
            exit()

        elif 'who are you' in query or 'your name' in query:
            d2= ['I already told you that my name is Jarvis','I am your Assistant Jarvis',
                 'Ohh!! How can you forget that? I am Jarvis, your personal voice assistant']
            speak(random.choice(d2))

        elif 'joke' in query:
            joke= pyjokes.get_joke()
            print(joke)
            speak(joke)
            speak("hahahahaha")

        elif 'news' in query or 'updates' in query:
            speak("Sure sir, here are the three latest updates from the world")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        elif 'who made you' in query or 'who created you' in query:
            speak("How can I forget that,  Shantanu created me, he spent his very important time on working on me")
        elif 'what can you do' in query or 'your features' in query:
            speak('I can do the following things for you')
            print("1-I can tell you everything!")
            print("2-Play a Music")
            print("3-Open any random website, but only say the url of that website to avoid confusion")
            print("4-Can send an email from your id")
            print("5-Can tell you the latest updates around the world")
            print("6-I have a bag of jokes, which I can share with you anytime!")
            print("7-Can tell you the weather")
            print("8-Can tell you the exact location of a place")
            print("9- Can arrange a meeting for you, either on Zoom or Meet")
            print("10- You can directly access a secure website for games")
            print("And many more!")
            time.sleep(4)

        elif "weather" in query:
             weather= temperature()
             description= des()
             humidity= humidity()
             print("Temperature:", weather, "Celsius")
             print("State of atmosphere: ", description)
             print("Humidity:" ,humidity)
             speak(f"In Delhi, the temperature is {weather} celsius,  atmospheric condition is {description} and humidity is {humidity}")

        elif 'how are you' in query:
            dialouge= ['Absolutely fine sir!','Good sir! And you?', 'I am good what about you sir ?']
            speak(random.choice(dialouge))

        elif 'video' in query:
            speak("What kind of videos do you want to watch ?")
            print("Hints: Movie,  Gaming, Cartoons, Scientific Facts, News")
            ans= takeCommand()
            if 'movie' in ans:
                webbrowser.open("https://www.youtube.com/channel/UClgRkhTL3_hImCAmdLfDE4g")
            elif 'gaming' in ans:
                webbrowser.open("https://www.youtube.com/gaming")
            elif 'Cartoons' in ans:
                webbrowser.open("https://www.cartoonnetworkhq.com")
            elif 'facts' in ans:
                webbrowser.open("https://www.youtube.com/c/FactTechz")
            elif 'News' in ans:
                webbrowser.open("https://www.youtube.com/channel/UCYfdidRxbB8Qhf0Nx7ioOYw")
            elif 'Sports' in ans:
                webbrowser.open("https://www.youtube.com/channel/UCYfdidRxbB8Qhf0Nx7ioOYw")
            else:
                ans= ans.replace("I want to watch","")
                ans= ans.replace("Jarvis","")
                webbrowser.open("https://www.youtube.com/results?search_query=" + ans)
                speak("Searching on Youtube...")



        elif 'music' in query or 'play song' in query:
            speak("Ok sir, here is a song for you!")
            SONGS= ['https://music.youtube.com/watch?v=RKioDWlajvo','https://music.youtube.com/watch?v=34d2f8TYkaE',
                    'https://music.youtube.com/watch?v=sKK6MOdXrG0','https://music.youtube.com/watch?v=kJQP7kiw5Fk',
                    'https://music.youtube.com/watch?v=PjTU0DmBWiU']
            webbrowser.open(random.choice(SONGS))

        elif 'zoom' in query:
         codePath1 = ("C:\\Users\\AJAY KUMAR SINGH\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk")
         speak("Ok sir, Opening Zoom Meetings")
         os.startfile(codePath1)



        elif 'game' in query:
            speak("Ok sir! Opening a gaming website for you!")
            games= ['poki.com','kizi.com','pacogames.com','gahe.com']
            webbrowser.open(random.choice(games))

        elif 'meeting' in query or 'meet' in query or 'video call' in query:
            speak("Opening a secure web portal for online meetings")
            webbrowser.open("meet.google.com")
        elif 'download' in query:
            webbrowser.open("play.google.com")
            speak("You can download everything through this website!!!")

        elif 'movie' in query:
            webbrowser.open("netflix.com")
            speak("You can watch movies, series and many more on this website, Enjoy!!!")


        elif 'sorry' in query:
            speak("No worries, you don't need to say this")

        elif 'wait' in query or 'stop' in query:
            speak("Alright!! Take your time!")
            time.sleep(5)

        elif 'search on google' in query:
            speak("Ok sir")
            query= query.replace("that", "")
            query= query.replace("Jarvis", "")
            query= query.replace("search on google", "")
            query= query.replace("about", "")
            webbrowser.open("https://www.google.com/search?q=" + query + "&oq=search&aqs=chrome..69i57j0i271l3j69i60l2.1242j0j1&sourceid=chrome&ie=UTF-8")

        elif 'search on youtube' in query:
            speak("Ok sir!")
            query= query.replace("search on youtube","")
            query= query.replace("about" , "")
            query= query.replace("Jarvis" , "")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query or 'send an email' in query:
            try:
                speak("Enter the email of the person whom you want to send message")
                to = input("Email address: ")
                speak("What do you want to say ?")
                content= input("Add your message: ")
                speak("Are you sure you want to send this email ?")
                ans1= takeCommand()
                if 'yes' in ans1:
                    sendEmail(to, content)
                    speak("Sir, Email has been sent!")
                else:
                    speak("Ok sir, this email won't be sent")
            except Exception as e:
                print(e)
                speak("Due to some error, I'm unable to send this email.")

        elif 'thank you' in query or 'thanks' in query:
            speak("No problem Sir!")



        elif 'hey' in query or 'hello' in query or 'hi' in query:
            speak("Hello Sir!")
            speak("May I help you with something ? ")
            print("To know what Jarvis can do, just ask him what can he do!")

        else:
            speak("Didn't get that")
            time.sleep(0.5)
            webbrowser.open("https://www.google.com/search?q="+query+"&oq=rieng&aqs=chrome..69i57.621j0j1&sourceid=chrome&ie=UTF-8")
            speak("Did you mean this ?")