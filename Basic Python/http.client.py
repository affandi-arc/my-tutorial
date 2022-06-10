import requests

url = "https://api-xyz.com/trueid/aov/?id=80102348948637"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)