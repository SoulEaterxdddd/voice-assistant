import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
import requests

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    speak(location + " " + info + " " + weather + " Градуса по цельсию")

with m as source:
    audio = r.listen(source)
city = r.recognize_google(audio, language = 'ru-RU')
city = city+" weather"
weather(city)
