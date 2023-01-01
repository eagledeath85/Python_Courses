data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]


def simple_hash(s: str) -> int:
    """
    A simple hashing function
    :param s: the string to hash
    :return: the hash value of the string
    """
    # Calculate the ordinal value of the first character of the string s
    basic_hash = ord(s[0])

    # Return the remainder after dividing by 10
    return basic_hash % 10


def get(k: str) -> str:
    """
    Return the value for a key, or none if the key doesn't exist
    :param k:
    :return:
    """
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


# Creating a list holding the keys and a list holding the values
keys = [""] * 10
values = keys.copy()

# Testing the function
for key, value in data:
    h = simple_hash(key)
    #h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value
print(keys)
print(values)
print()
value = get("lemon")
print(value)