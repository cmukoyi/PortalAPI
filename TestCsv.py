import csv

input_file = 'C:/Users/Carlos Mukoyi/Documents/code/portalapi/createpass1.csv'

with open(input_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
