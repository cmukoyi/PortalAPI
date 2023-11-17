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
  'Authorization': 'bearer VDZXQFAkZGItZyhaiEAf0mThIX0-SCF2mfi-mPte4EOusm7CUPLC51Fq3_Ebbl_DBu9nfKQBzP2UGE0uILuDJVurcYWkeLaAiO3BEEhXcT-tzzZGV10kNfzHinpHC3526AqnLOwfrvM89bPdVr96n0qf4rb4nE6kKYiKgsn73skRw_Ou9y0q61gCk2c4X1VvZPpg9fAjtTJUHjcGxLhzhAoqaDqUMZEbalVWgXWYYijg3nFBP6wtzbIVd_VHKc7xD4a94gov-LXrRT6DtiuF4EtKrU-ed_jZz6MNQt8GSuwDdWJ72Q4O1UHfWDKynDK0AvU2zjHqOv-DAcW53OJsxBbjtNtjzOf0v-fX6OrvAvatkLPUtlOSLUkObTgJe4pGbbGefAbeIF7ox4mx7Zzl9-n_YbPN0xohKx_lh7i0CixlbxH58z552AMCkbmP1fM99Z1XqQjlk7vsGkdrhWQqV4YeXowRZqBrEe8eYohzz2Vs31oTn7ASzroT1Dfc0jkfiuMh8NfxB2cd4ekVQXbjdg'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
