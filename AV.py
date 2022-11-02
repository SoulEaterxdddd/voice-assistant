# Голосовой ассистент1.0 BETA
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime


#Настройки браузера
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

#Словарь ключевых слов
opts = {
    "alias": ('ва','голосовой помощник','голосовой ассистент','ассистент','voice assistant','помощник'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты','щутку'),
        "weather":('погода','скажи погоду','какая сейчас погода'),
        "search":('найди','найди в интернете','поищи в интернете','запрос')
    }
}


# функция синтеза речи
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    # Рапознавание голоса и превращение его в строку
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращение
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    # На случай если голос не распознался
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

#Определение со словарем и выбор функции
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("1234567890")

    elif cmd == 'weather':
	# Модуль погоды
        print('Какой ваш город ?')
        import Weather

    elif cmd == 'search':
	# Веб запрос
        print('Какой ваш запрос ?')
        import web

    else:
	# Команда не распознана
        print('Команда не распознана, повторите!')



# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Приветствие
speak("Добрый день, Голосовой помощник на связи")
speak("Слушаю команду")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # Прослушка шумов
