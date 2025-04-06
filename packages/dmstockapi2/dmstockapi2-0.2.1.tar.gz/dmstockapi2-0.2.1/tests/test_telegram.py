import requests
import os


def send_telegram_msg(text=""):
    token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url=url, json={"chat_id": chat_id, "text": text})


def test():
    send_telegram_msg("test telegram message")
