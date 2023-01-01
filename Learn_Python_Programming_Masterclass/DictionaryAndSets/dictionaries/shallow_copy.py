animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

# Creating a new dictionary with the copy() method
# things and animal dictionaries have 2 different references now
things = animals.copy()
animals["teddy"] = "toy"

print(things)
print(animals)