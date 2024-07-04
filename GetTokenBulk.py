import csv
import requests

# Function to get bearer token for a given username and password
def get_bearer_token(username, password):
    url = "https://poc.connectedcar360.net/V1/token"
    payload = f'grant_type=password&username={username}&password={password}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        response_text = response.text
    else:
        access_token = None
        response_text = response.text
    return response.status_code, access_token, response_text

# Read usernames and passwords from CSV file
input_file = 'C:/Users/Carlos Mukoyi/Documents/code/portalapi/usernames_passwords2.csv'
output_file = 'C:/Users/Carlos Mukoyi/Documents/code/portalapi/responses_token2.csv'

with open(input_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Process each row and get bearer token
output_rows = []
for row in rows:
    username = row['username']
    password = row['password']
    status_code, bearer_token, response_text = get_bearer_token(username, password)
    output_rows.append({'username': username, 'password': password, 'bearer_token': bearer_token, 'status_code': status_code, 'response_text': response_text})

# Write responses to CSV file
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['username', 'password', 'bearer_token', 'status_code', 'response_text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in output_rows:
        writer.writerow(row)

print("Responses saved to", output_file)
