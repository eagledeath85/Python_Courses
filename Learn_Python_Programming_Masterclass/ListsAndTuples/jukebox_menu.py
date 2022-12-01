from nested_data import albums

# List of songs is always on index 3 in the tuple of the albums list
# We can declare it as a constant variable
# In Python, a constant is written in capital letters
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

# Display the menu as long as an invalid choice is made
# Use of a while loop to do this
# Check buy_computers_improved.py

while True:
    print("Please choose your album (invalid choices exits the program):")
    # parenthesis are needed because enumerate(albums) return a list of indexes and tuples
    # for index, value in enumerate(albums):
    #     # Unpacking the tuple contained in value
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)

    for index, (title, artist, year, songs) in enumerate(albums):
        print("{0}: {1}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
        print(songs_list)
    else:
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{0}: {1}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("You have chosen {0}".format(title))

    print("*" * 40)