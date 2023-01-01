small_ints = set(range(21))
print(small_ints)

# Clearing the set by deleting all its values
small_ints.clear()
print(small_ints)


# There are two different things we might want to do, and having two different methods reflects that:
    # 1: Ensure that, when we're done, something no longer exists. In this case, we don't care if it was already
# there or not – we just want it gone.
    # 2: Remove something if it exists, but provide some sort of notification if it doesn't.
# These are different use cases, and Python provides an obvious way to do each one;
# discard for the first case, and remove for the second.

# Discarding a specific item from a set
# If the item to discard is not present in the set, the discard() method won't return any error
small_ints = set(range(21))
small_ints.discard(5)
print(small_ints)

# Remove a specific item from an item
# If the item to remove is not present in the set, the remove() method will return an error
small_ints = set(range(21))
small_ints.remove(5)
small_ints.remove(25)
print(small_ints)