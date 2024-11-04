import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')    
engine.setProperty('voice', voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("GOOD MORNING SIR")
    elif hour > 12 and hour <16:
        speak("GOOD AFFTERNOON SIR")
    else:
        speak("GOOD EVENING SIR")

def sendEmail (to, content):
    server  = smtplib.SMTP( 'smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)
   
    try:
        query  =r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        query = query.lower()
    except Exception as e:
        print("Please say again ...... ")
        return "None"
    
   
    return query



if __name__=="__main__" :  
    wishme() 

    speak(" I AM JARVIS. HOW CAN I HELP YOU")
    while True:
        query = take_command() 
        if 'how are you' in query :
            speak('I am fine sir whats about you')
            print 
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia.com", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opening")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is open")

        elif 'play music' in query:
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("start playing music")

        elif 'time' in query:
            strTime = datetime.datetime.now()
            print(strTime.time())
            speak(f"Sir , the time is {strTime.time()}")

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            speak("stack overfflow is opening")

        elif 'open free code camp' in query :            
            webbrowser.open('freecodecamp.org')
            speak("free code camp is opening")

        elif 'open code' in query:
            code_path = r"C:\Users\Kamal\Desktop\Visual Studio Code.lnk"
            os.startfile(code_path)

        elif 'email to receiver name' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "receiver's email id"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")