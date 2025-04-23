
import requests
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def send_alert(message):
    token = config["telegram_token"]
    chat_id = config["chat_id"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram Error:", e)
