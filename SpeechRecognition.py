import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('6GK3HG-LJKJEYREVT')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-IN')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('Opening YouTube')
            webbrowser.open('www.youtube.com')
            
        elif 'open notepad' in query:
            speak('Opening Notepad')
            os.system('notepad')
            
        elif 'open recycle bin' in query:
            speak('Opening Recycle Bin')
            os.startfile('C:\$Recycle.Bin')
            
        elif 'open command prompt' in query or 'open cmd' in query:
            speak('Opening Command Prompt')
            os.system('start cmd')      

        elif 'open paint' in query or 'open ms paint' in query:
            speak('Opening Paint')
            os.startfile('C:\Windows\System32\mspaint.exe')

        elif 'open chrome' in query or 'open google chrome' in query:
            speak('Opening Google Chrome')
            webbrowser.get('C:/Program Files (x86)/Google/Application/Chrome/chrome.exe %s').open('https://www.google.com')

        elif 'open computer' in query or 'open my computer' in query or 'open this pc' in query:
            speak('Opening Computer')
            os.startfile('This PC')

        elif 'what is date today' in query or 'tell me the date' in query:
            speak('The Date is')
            os.system('date')

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('Opening Gmail')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello')

        elif 'home' in query or 'bye' in query:
            speak('Bye, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'E:/Music/'
            music = ['5 Taara-(Mr-Jatt.com)', 'Do You Know-(Mr-Jatt.com)','KANGNA TERA']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.startfile(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command!')
        

