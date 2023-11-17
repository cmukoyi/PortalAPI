import requests

url = "https://test.scopemlog.net/api/public/policy/17130603A001/17130603A001_RENAMED009"

payload = ""
headers = {
  'Authorization': ''
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
