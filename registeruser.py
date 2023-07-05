import requests
import json

url = "https://poc.connectedcar360.net/V1/api/account/RegisterWithPolicy"

payload = json.dumps({
  "PolicyOrCustomerNumber": "poc001000",
  "UserName": "Carl837S",
  "Password": "Carl837S1!",
  "AgreementAccepted": "true"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
