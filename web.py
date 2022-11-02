import webbrowser as wb
import speech_recognition as sr
import pyttsx3

#Определение микрофона
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
speak_engine = pyttsx3.init()

#Синтезатор речи
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

#Поисковая система    
def search(srch):
    wb.open(f'https://www.google.ru/search?q={srch}')

#преобразование запроса в текст
with m as source:
    audio = r.listen(source)
srch = r.recognize_google(audio, language = 'ru-RU')
search(srch)
