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

# set of odd numbers that aren't primes
print(odds.difference(primes))
print((odds - primes))

# difference() is not commutative, meaning a - b will produce a different result as b - a