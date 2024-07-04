import pandas as pd

# Specify the path to the Excel file
file_path = 'C:/Users/Carlos Mukoyi/Documents/code/portalapi/data/KSA_Dashboard_2024v1.5.xlsx'

# Read the Excel file into a pandas DataFrame
try:
    df = pd.read_excel(file_path)

    # Print the column names to check for discrepancies
   # print("Column names:", df.columns)

    # Strip any leading or trailing spaces from the column names
    df.columns = df.columns.str.strip()

    # Print the column names again to verify
   # print("Column names after stripping:", df.columns)

    # Generate summary
    summary = {
        'Total Policies': df['Policy No'].nunique(),
        #'Total Device Types': df['Device Type'].nunique(),
        'Total Device Types': df['Device Type'].value_counts().to_dict(),
        'Unit Status Counts': df['Unit Status'].value_counts().to_dict(),
        'User Status Counts': df['User Status'].value_counts().to_dict(),
        'Unit Assignment Status Counts': df['Unit Assignment Status'].value_counts().to_dict()
    }

    # Print summary
    for key, value in summary.items():
        print(f"{key}: {value}")
    

except Exception as e:
    print(f"An error occurred: {e}")
