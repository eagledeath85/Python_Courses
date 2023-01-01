from contents import pantry

# The setdefault() method returns the value of a key, if the key exists in the dictionary
# It returns the defined default value if the key doesn't exist AND ADDS THE KEY TO THE DICTIONARY
# The get() method is identical to setdefault(), but doesn't add the missing key to the dictionary
chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

goose_quantity = pantry.setdefault("goose", 0)
print(f"goose: {goose_quantity}")
print()
print("pantry now contains:")
for key, value in sorted(pantry.items()):
    print(key, value)