import requests
import json
import csv
import os
from datetime import date, datetime

# Define the CSV file path
csv_file_path = 'setMode.csv'  # Update with the path to your CSV file
url = "https://poc.connectedcar360.net/v1/api/Policies/SetRecordingMode"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer xNQrlUsvcgCdxAv_EJbCGbwkWsPHAtYqfKMK1ipHuTmrZI3mwKzIBThMwGn5fqLDOmQe68IGU_kF3rd3Qq_unnIfO1dyht6A79QdJhNMml_YC1zisttaTtGAXZpBE17RVoFazLpAtOOD5GKuduEMarOUxEuWWQZa2GswOzc1LemnfxMeqZskROvvHkrOYNdqxNdpzOipGIQIzXTo_Mj765998SL27zdjp_80kOcPzTLiYkt7qWdk4vjgptOU7RPLIFbQ6htvsCl3c-RDtch9JrSoxQwluvslnzEA9l7SFcFebY7jnZ_8cqGtesxLgjRBxMLgkhc6F71mnwxjhTvKXhbpKu2hsOll3iiAo9YdlGTaYrucOlxw28NlFZg2Z1GJmyFVtPQi42FiXkOedT5TZQN6b9mDflJCHh6YsFuX2HQGSHmaZR1HoVHq_E_QjIGKLlSBZXvkQAvbyAMrAEBm6-OHlOm5eAARgd2N7-SwxpvVb5RbhQIrFsr-PBrSJQm6xLqTxrLVGnHlKwd8chsm0A'
}

# Get the current date for creating the log file
current_date = date.today()
log_filename = f"responses_{current_date}.log"

# Check if the log file already exists for today, and append to it if it does
if os.path.exists(log_filename):
    mode = 'a'  # Append mode
else:
    mode = 'w'  # Create a new file if it doesn't exist

# Open the log file in the appropriate mode
with open(log_filename, mode) as log_file:
    # Read the CSV file to get the PolicyNumber
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            policy_number = row['PolicyNumber']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Sending request for PolicyNumber: {policy_number}")

            # Construct the payload for the request
            payload = json.dumps({
                "PolicyNumber": policy_number,
                "RequestedTripRecordingMode": "BeaconRecording"
            })

            try:
                response = requests.post(url, headers=headers, data=payload)
                response.raise_for_status()  # Raise an exception for HTTP errors
                response_text = response.text
                print(f"Response for PolicyNumber {policy_number} (HTTP {response.status_code}): {response_text}")
            except requests.exceptions.RequestException as e:
                response_text = str(e)
                print(f"An error occurred for PolicyNumber {policy_number}: {response_text}")

            # Write the response with timestamp to the log file
            log_entry = f"{timestamp} - PolicyNumber: {policy_number}, HTTP {response.status_code}, Response: {response_text}\n"
            log_file.write(log_entry)
