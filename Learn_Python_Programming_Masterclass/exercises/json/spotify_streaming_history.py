import json


# spotify_streaming_history = '/home/administrateur/Documents/spotify_data.json'
spotify_streaming_history = '/home/administrateur/Downloads/my_spotify_data/MyData/StreamingHistory0.json'

# try:
#     # Opening spotify_streaming_history JSON file
#     f = open(spotify_streaming_history)
# except IOError as e:
#     # Raise exception if the file is not found
#     raise Exception("File not found exception", e)
# else:
#     # Reading from spotify_streaming_history file
#     data = json.loads(f.read())
#
#     # Iterating through the spotify_streaming_history file
#     for raw in data['details']:
#         print(raw)
# finally:
#     f.close()


try:
    # Opening spotify_streaming_history JSON file
    with open(spotify_streaming_history, 'r') as f:

        # Reading from spotify_streaming_history file
        data = json.loads(f.read())

    output = ','.join(*[data[0]])
    for obj in data:
        # Populating output file with objects from data
        output += f'\n{obj["endTime"]},{obj["artistName"]},{obj["trackName"]},{obj["msPlayed"]}'

    # Opening output csv file
    with open('output.csv', 'w') as f:
        # Writing in output file
        f.write(output)
except Exception as ex:
    print(f'Error: {str(ex)}')
finally:
    f.close()