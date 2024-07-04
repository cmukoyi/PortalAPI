import json

# Read the provided JSON file
with open('C:/Users/Carlos Mukoyi/Documents/code/response.json', 'r') as json_file:
    data = json.load(json_file)

# Extracting required fields from each entry in the "value" array
formatted_data = []
for entry in data['value']:
    unique_reference = None
    customer_name = None
    policy_no = None
    
    # Loop through NotificationFields to find required fields
    for field in entry['NotificationFields']:
        if field['Name'] == 'RegistrationUrl':
            unique_reference = field['Value'].split('=')[-1]
        elif field['Name'] == 'CustomerFullName':
            customer_name = field['Value']
        elif field['Name'] == 'PolicyNo':
            policy_no = field['Value']
    
    # Create dictionary for each entry with required fields
    formatted_entry = {
        "UniqueReference": unique_reference,
        "CustomerName": customer_name,
        "PolicyNo": policy_no,
        "Email": "Walaa.Aigenix@walaa.com"  # Assuming this email is constant for all entries
    }
    
    # Append formatted entry to the list
    formatted_data.append(formatted_entry)

# Write the formatted data to a new JSON file
output_file = 'output.json'
with open(output_file, 'w') as json_output:
    json.dump(formatted_data, json_output, indent=2)

print("Formatted data saved to:", output_file)
