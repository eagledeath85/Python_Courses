import csv

# CREATE ROWS OF DICTIONARIES WHEN READING A CSV FILE
# The DictReader produces rows a dictionaries, so we don't have to create one in the code
cereals_filename = 'cereal_grains.csv'

with open(cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)