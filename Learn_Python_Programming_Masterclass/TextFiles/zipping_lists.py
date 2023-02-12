import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

# The zip() function takes iterables and returns an iterable containing tuples
# If we provide two lists, for example, each tuple will contain two items – one from each list, in turn.
# Passing three lists will create tuples containing three items each.
# The zip() function zips together the two iterables and creates tuples containing each item from each iterable

# Create a list for column headers of the csv file we're going to create
keys = ['album', 'artist', 'year']

filename = 'albums.csv'

with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in albums:
        # Create a tuple (keys, albums_row) with the zip function
        zip_object = zip(keys, row)
        # print(zip_object)
        # for thing in zip_object:
        #     print("\t", thing)
        # Converting the zip_object tuple into a dictionary to be used with the DictWriter()
        album_dict = dict(zip_object)
        writer.writerow(album_dict)