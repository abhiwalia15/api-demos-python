# Detect face landmarks in an image, given by a url
import base64
import json

import requests

landmarksurl = "https://api.facesoft.io/v1/face/landmarks"


def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)


headers = {
    'apikey': "xxxxxxxxxx-xxxxxxxxxxx" # Insert your API key here
}

payload = {
    'image1': get_as_base64("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Arnold_Schwarzenegger_September_2017.jpg/220px-Arnold_Schwarzenegger_September_2017.jpg"),
}

response = requests.request("POST", landmarksurl, data=json.dumps(payload), headers=headers)

print(response.text)
