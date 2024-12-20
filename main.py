import requests
from datetime import datetime
from time import sleep

def send_ntfy(topic, message):
    url = f"https://ntfy.sh/{topic}"
    response = requests.post(url, data=message.encode('utf-8'))
    if response.status_code ==200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification: {response.status_code} {response.text}")

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #print(current_time)
    if current_time == "19:20":
        send_ntfy("Feed_the_dog", "Feed Louie now OR ELSE")
    sleep(60)

#send_ntfy("Feed_the_dog", "Feed Louie now...OR ELSE")