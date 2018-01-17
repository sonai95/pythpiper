import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something!')
    audio = r.listen(source)

import webbrowser
url = 'http://google.com//search?q='
x=r.recognize_google(audio)
x.replace(' ','+')
webbrowser.open(url+x)