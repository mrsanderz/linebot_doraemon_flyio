from flask import Flask, request, abort
import requests
import random
import os
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent

app = Flask(__name__)
handler = WebhookHandler("YOUR Channel secret") #Channel secret

# LINE Notify Token
line_notify_token = 'YOUR line_notify_token'

def send_line_notify(message, image_url=None):
    headers = {
        'Authorization': f'Bearer {line_notify_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'message': message}
    if image_url:
        payload['imageThumbnail'] = image_url
        payload['imageFullsize'] = image_url
    response = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=payload)
    return response.status_code

@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return "OK"

# List of pre-defined image URLs
image_urls = [
    'https://megapx-assets.dcard.tw/images/ab174a89-69e1-44e7-a15b-ecd60add474e/full.jpeg',
    'https://megapx-assets.dcard.tw/images/3722ecd7-297e-4979-a733-dc4eaedbd326/full.jpeg',   
    'https://megapx-assets.dcard.tw/images/776c3489-c910-40f4-b5a3-cb1d7bb664ff/1280.jpeg',
    'https://megapx-assets.dcard.tw/images/2d2f27fd-7d26-4e2d-8cbb-549b28a1b801/1280.jpeg',  
    'https://megapx-assets.dcard.tw/images/d5274e0f-65ec-40b4-a380-7a8dd26997e2/full.jpeg', #美型驚訝
    'https://megapx-assets.dcard.tw/images/4af5cbc9-a6f9-4abb-a3d5-21da9081a0ee/1280.webp', #哆啦梳頭髮
    'https://megapx-assets.dcard.tw/images/c7e60d86-7d96-42e7-b26b-098c0c99f512/1280.webp'
]

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    # Respond differently based on the received message
    if '哆啦' in event.message.text:
        # Choose a random image from the pre-defined list
        chosen_image_url = random.choice(image_urls)
        # Send the chosen image through LINE Notify
        send_line_notify("哆啦: ", chosen_image_url)
    #else:
        # Echo the received message through LINE Notify
        # send_line_notify(event.message.text)

if __name__ == "__main__":
    app.run()
