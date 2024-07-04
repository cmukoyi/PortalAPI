import csv
import requests

# Function to change password for a given username using bearer token
def change_password(username, old_password, new_password, bearer_token):
    url = "https://poc.connectedcar360.net/V1/api/account/ChangePassword"
    payload = {
        "OldPassword": old_password,
        "newPassword": new_password,
        "confirmPassword": new_password
    }
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code

# Read responses from CSV file
input_file = 'C:/Users/Carlos Mukoyi/Documents/code/portalapi/responses5.csv'
output_file = 'C:/Users/Carlos Mukoyi/Documents/code/portalapi/password_changes5.csv'

output_rows = []

with open(input_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row['username']
        old_password = row['old_password']
        new_password = row['new_password'].replace(" ", "")  # Remove spaces from new password
        bearer_token = row['bearer_token']
        status_code = change_password(username, old_password, new_password, bearer_token)
        output_rows.append({'username': username, 'new_password': new_password, 'status_code': status_code})

# Write results to CSV file
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['username', 'new_password', 'status_code']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in output_rows:
        writer.writerow(row)

print("Password changes saved to", output_file)
