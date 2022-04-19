import webbrowser as wb
import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
m = sr.Microphone(device_index=1)
speak_engine = pyttsx3.init()

def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def search(srch):
    wb.open(f'https://www.google.ru/search?q={srch}')

#
with m as source:
    audio = r.listen(source)
srch = r.recognize_google(audio, language = 'ru-RU')
search(srch)




