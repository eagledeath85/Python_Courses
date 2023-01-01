import copy

animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

# A deep copy will copy any objects that are contained in whatever we're copying
things = copy.deepcopy(animals)
things["teddy"] = "bear"
print(animals)
print(things)