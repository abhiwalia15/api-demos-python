# Compare two images given by urls
import base64
import json

import requests


def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)


headers = {
    'apikey': "xxxxxxxxxx-xxxxxxxxxxx"  # Insert your API key here
}

matchurl = "https://api.facesoft.io/v1/face/match"

payload = {
    'image1': get_as_base64(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Arnold_Schwarzenegger_September_2017.jpg/220px-Arnold_Schwarzenegger_September_2017.jpg"),
    'image2': get_as_base64(
        "https://media2.mensxp.com/media/content/2017/Oct/life-lessons-from-arnold-schwarzenegger1400-1508319857_1100x513.jpg")}

response = requests.request("POST", matchurl, data=json.dumps(payload), headers=headers)

print(response.text)
