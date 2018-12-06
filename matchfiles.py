# Match faces in two images, given by files
import base64
import json

import requests

matchurl = "https://api.facesoft.io/v1/face/match"

headers = {
    'apikey': "xxxxxxxxxx-xxxxxxxxxxx"  # Insert your API key here
}

with open("Pele.png", "rb") as f:
    data = f.read()
    b64string1 = data.encode("base64")

with open("pele2.png", "rb") as f:
    data = f.read()
    b64string2 = data.encode("base64")

payload = {
    'image1': b64string1,
    'image2': b64string2
}

response = requests.request("POST", matchurl, data=json.dumps(payload), headers=headers)

print(response.text)
