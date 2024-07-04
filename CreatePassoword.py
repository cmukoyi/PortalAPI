import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/Carlos Mukoyi/Documents/code/portalapi/createpass1.csv')

# Assuming the header of the password column is 'Password'
password_header = 'new_password'

# Append '!' to all values in the password column starting from the second row (index 1)
for idx, value in enumerate(df[password_header][1:], start=1):
    df.at[idx, password_header] = value + '!'  # Append '!' to the existing value

# Write the modified DataFrame back to the CSV file
df.to_csv('C:/Users/Carlos Mukoyi/Documents/code/portalapi/createpass2.csv', index=False)
