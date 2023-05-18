import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hi, I am tara')
engine.say('What can i do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tara' in command:
                command = command.replace('tara', '')
                print(command)
    except:
        pass
    return command

def run_tara():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        serchresult = command.replace('tell me about', '')
        info = wikipedia.summary(serchresult, 2)
        print(info)
        talk(info)
    elif 'love' in command:
        talk('i love you sonali')
    elif 'make me laugh' in command:
        talk(pyjokes.get_joke())
    elif 'sad' in command:
        talk('Let me make you laugh')
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk("You're welcome")
    elif 'bye' in command:
        talk('Bye')
    else:
        talk('Please say that again')
try:
    while True:
        run_tara()
except:
    print('See you again. Take care.')
    talk('See you again. Take care.')
    pass
