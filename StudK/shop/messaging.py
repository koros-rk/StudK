import requests


def send_telegram(text: str):
    token = "5591836025:AAHrg09-IB4gfYym2u6P5O_aXJ1wl-duNik"
    url = "https://api.telegram.org/bot"
    channel_id = "-1001607111458"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")
