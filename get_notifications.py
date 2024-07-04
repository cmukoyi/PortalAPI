import requests
import json

# url = "https://walaa.connectedcar360.net/V1/odata/Notifications?%24format=json&%24top=50&%24orderby=DateCreated+desc&%24filter=NotificationType+eq+Blackjack.Shared.Classifiers.NotificationType%272%27&%24count=true"
# url = "https://walaa.connectedcar360.net/V1/odata/Notifications?%24format=json&%24top=1000&%24orderby=DateCreated+desc&%24filter=DateCreated+ge+2024-02-19T00%3A00%3A00%2B02%3A00&%24count=true"
url = "https://ggci.connectedcar360.net/V1/odata/Notifications?%24format=json&%24top=1000&%24orderby=DateCreated+desc&%24filter=DateCreated+ge+2024-03-06T00%3A00%3A00%2B02%3A00&%24count=true"


payload = ""
headers = {
  'Authorization': 'Bearer EBTEUeKbQp27-O-_dOrtnavmStakgBtyd4S2meCrRWf4k2wgOkWEwreirjMQpSGE6jh8aDnlQ1kQxCi7fXsnBzf2GGVAvK1bKXO5EXCKYoEytW7kXu3-79-I_u5p5xt_gt97ev6dHfzqv6Z5y-YlXYGxxvxasrptyhTFaPYl39hC20FyFO6h60VJyxJQhxLMa6Rs6Bn-3uaHQMmLvd97V4IqTSzvNuOx1LkOU6-VtTy9J-XaD2izqG44qdRPBvDiikdkGgqcrDJgbhvOw4PDzK6PTyMSvNiacf2BnZcj0JeClv_4Srvq35cCaFg2b89gHhUIVA3r7_QO8tRBBID8cj-YnvOe9eWnF5UZPWJ-BZo3T48AuTOXQwTp-kbeI8fQt6ULsRVqDq7bu99AtWMDTiUraK1ImR461HH6ObhNBuv8oReCRHAzZopMyox4CantjBq-leibdwAQgMFAbaweYRQvwnOjXmzE-8jX6xfkWWD5XqLuV6AoKQ0Yb_UvddVmAf2xe88Ln3oakIpIX5qwYQ',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse response text as JSON
    response_json = response.json()
    
    # Save JSON response to a file
    with open('response.json', 'w') as json_file:
        json.dump(response_json, json_file)
    
    print("JSON response saved to 'response.json'")
else:
    print("Failed to fetch data:", response.status_code)
