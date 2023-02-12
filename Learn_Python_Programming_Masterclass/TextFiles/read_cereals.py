import csv

csv_file = 'cereal_grains.csv'

with open(csv_file, encoding='utf-8', newline='') as csv_file:
    # Providing a value for the quoting argument, telling the reader function how the data has been quoted
    # When reading, QUOTE_NONNUMERIC tells the reader that the strings will be quoted,
    # allowing numerical values to be converted to floats
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)