import requests
import json

url = "https://walaa.connectedcar360.net/v1/api/Policies/ChangeNumber"

payload = json.dumps({
  "CurrentNumber": "UATBLE10031",
  "NewNumber": "UATOBD10031",
  "ChangeOnlyInPortal": False
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': ''
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
