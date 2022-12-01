# In slicing backward, the start value must be greater than the stop value

letters = "abcdefghijklmnopqrstuvwxyz"
backward = letters[25:0:-1]
print(backward)                 # zyxwvutsrqponmlkjihgfedcb
print(letters[25::-1])          # zyxwvutsrqponmlkjihgfedcba
print(letters[::-1])            # zyxwvutsrqponmlkjihgfedcba
print(letters[16:13:-1])        # qpo
print(letters[-10:-13:-1])      # qpo
print(letters[4::-1])           # edcba
print(letters[-22::-1])         # edcba

# Pattern to reverse the last n characters of a sequence is [:-(n+1):-1]
    # Slice the string to produce the last 8 characters in reverse order
print(letters[:-9:-1])          # zyxwvuts

    # Slice the string to produce the last 4 characters in reverse order
print(letters[:-5:-1])


# Pattern to get the last n characters of a sequence is [-n:]
print(letters[-4:])

# Pattern to get the first n characters of a sequence is [:n]
print(letters[:1])
