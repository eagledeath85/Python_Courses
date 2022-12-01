data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []


suffix_flower = " - Flower"
suffix_shrub = " - Shrub"
for item in data:
    if item.__contains__(suffix_flower):
        # line_new = line[len(prefix):]
        item = item[:-len(suffix_flower)]
        flowers.append(item)
    elif item.__contains__(suffix_shrub):
        item = item[:-len(suffix_shrub)]
        shrubs.append(item)
print(flowers)
print(shrubs)