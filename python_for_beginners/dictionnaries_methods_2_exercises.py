consonants_dictionnary = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
print(consonants_dictionnary)
for key, value in consonants_dictionnary.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac",
                   "Burger King": "Whopper",
                   "Chick-fil-A": "Original Chicken Sandwich"
                   }
big_mac = fast_food_items.pop("McDonald's")
print(big_mac)
fast_food_items.popitem()
print(fast_food_items)

