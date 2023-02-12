input_filename = 'country_info.txt'

countries = {}

with open(input_filename, 'r') as country_file:
    # Exclude the first line of the country_file from the dictionary
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        # We want to put all the fields in a dictionary. To do that, we'll put those fields into variables. To do so,
        # we unpack the fields from the list
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        # Creating the dictionary
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        #print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

#print(countries)

while True:
    chosen_country = input("Please enter the country of your choice: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data_capital = countries[country_key]['capital']   # country_data_capital -> dict
        print(f'The capital of {chosen_country.capitalize()} is {country_data_capital}')
    elif chosen_country == 'quit':
        break
    else:
        print("The country typed is not in the list")