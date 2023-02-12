import csv

input_filename = 'country_info.txt'

# SNIFFING THE FILE TO WORK OUT ITS DIALECT

# CSV module's Sniffer class examines a sample of the file, and works out things like the separators, the character
# used to delimit strings, and so on. It uses that sample to create a Dialect.
# A Dialect is just all of the various options, grouped together into a single object.

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    # To get our sample, we only need to read a few lines from the file to process
    sample = ""
    for line in range(3):
        sample += countries_data.readline()

    # Sniffing the file, to create a dialect
    country_dialect = csv.Sniffer().sniff(sample)

    # Go back to the start of the file
    # The seek() method is used to position the file pointer to another place in the file
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)