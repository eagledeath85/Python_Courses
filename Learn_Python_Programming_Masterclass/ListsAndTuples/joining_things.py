# join() method creates a string from a list and separates each item with the string that it's called on
# !!! ALL THE ITEMS IN THE ITERABLE MUST BE STRINGS !!!

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavander",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

separator = " | ".join(flowers)
print(separator)