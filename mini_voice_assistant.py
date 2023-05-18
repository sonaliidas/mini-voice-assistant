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
engine.say('Hi, I am Pipi')
engine.say('What can I do for you')
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
            if 'pipi' in command:
                command = command.replace('pipi', '')
                print(command)
    except:
        pass
    return command

def run_pipi():
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
        searchresult = command.replace('tell me about', '')
        info = wikipedia.summary(searchresult, 2)
        print(info)
        talk(info)
    elif 'do you love me' in command:
        talk('Everyone loves you and so do i')
    elif 'i love you' in command:
        talk('I love you too')
    elif 'who do you love the most' in command:
        talk('Myself')
    elif 'who is sonali' in command:
        talk('She the one who created me and I adore her for that you can know more about her from her github dashboard or her social profiles')
    elif 'do you love sonali' in command:
        talk('Ofcourse I love her')
    elif 'make me laugh' in command:
        talk(pyjokes.get_joke())
    elif 'sad' in command:
        talk('Let me make you laugh')
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk("You're welcome")
    elif 'i want to sleep' in command:
        talk('Ya you can take a power nap')
    elif 'you sleep' in command:
        talk('If you want me to sleep just say sleep well')
    elif 'sleep well' in command:
        talk('Thank you Bye')
    elif 'bye' in command:
        talk('Yup Bye')
    else:
        talk('Please say that again')
try:
    while True:
        run_pipi()
except:
    print('See you again. Take care.')
    talk('See you again. Take care.')
    pass
