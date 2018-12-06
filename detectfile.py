# Detect faces in an image, given in a file
import base64
import json

import requests

detecturl = "https://api.facesoft.io/v1/face/detect"

headers = {
    'apikey': "xxxxxxxxxx-xxxxxxxxxxx"  # Insert your API key here
}

with open("pele.png", "rb") as f:
    data = f.read()
    b64string = data.encode("base64")

payload = {
    'image1': b64string,
}

response = requests.request("POST", detecturl, data=json.dumps(payload), headers=headers)

print(response.text)
