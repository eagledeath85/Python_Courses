animals = {'turtle',
           'horse',
           'robin',
           'python',
           'swallow',
           'hedgehog',
           'wren',
           'aardvark',
           'cat',
           }

birds = {'robin', 'swallow', 'wren'}

# Checking if birds is subset of animals
print(f"birds is a subset of animals: {birds.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issuperset(birds)}")

print(f"birds is a superset of animals: {birds > animals}")
print(f"animals is a subset of birds: {animals < birds}")