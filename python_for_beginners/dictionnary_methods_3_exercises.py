internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
backup_internet_celebrities = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(backup_internet_celebrities)