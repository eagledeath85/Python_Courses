import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}

with open(input_filename, encoding='utf-8', newline='') as csv_country_file:
    # Get the column headings from the first line of the file
    headings = csv_country_file.readline().strip("\n").split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_reader = csv.DictReader(csv_country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        #countries[country.casefold()] = country_dict
        countries[row['country'].casefold()] = row
        #countries[code.casefold()] = country_dict
        countries[row['cc'].casefold()] = row

while True:
    chosen_country = input("Please enter the country of your choice (name or 2 digits code): ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break
    else:
        print("The country name typed is not in the list")