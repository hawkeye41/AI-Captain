import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

"""def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("hello sir,GOOD MORNING!")
    elif hour>=12 and hour<<18:
        talk("hello sir,good afternoon!")
    else:
        talk("hello sir, good evening!")
    talk("i am captain sir, please tell me how i help you")"""

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'captain' in command:
                command = command.replace('captain', '')
                print(command)
    except:
        pass
    return command

def run_captain():
    command = take_command()
    print(command)




    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is the' in command:
        person = command.replace('who is the', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'google' in command:
      webbrowser.open("google.com")
    elif 'youtube' in command:
        webbrowser.open("youtube.com")


    else:
        talk('please say the command again')


while True:
    run_captain()

