from primes_and_squares import squares_generator, primes_generator


# intersection() produces a new set containing those elements that are in both the sets
evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
squares = set(squares_generator(100))
print(primes)
print(squares)

# Odds perfect squares less than 50
print(odds.intersection(squares))

# Evens perfect squares less thant 50
print(evens.intersection(squares))

# Using the method instead of the operator allow us to pass an iterable to the method
even_squares = evens.intersection(squares_generator(100))
print(even_squares)

# Using the operator allows us to get the intersection of more than 2 sets
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}
intersection = farm_animals & wild_animals & potential_rides    # animals that can be ridden
mounts = farm_animals.intersection(wild_animals, potential_rides)
print(intersection)
print(mounts)