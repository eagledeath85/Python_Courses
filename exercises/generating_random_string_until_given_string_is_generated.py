import string
import random
import time

possible_characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

#String to be generated
string_to_be_generated = "glasses"

try_this = ''.join(random.choice(possible_characters) for i in range(len(string_to_be_generated)))

try_next = ''
# number of tentatives = 0
tentatives = 0

# boolean to stop the loop
completed = False

while completed == False:
    print(try_this)
    try_next = ''
    completed = True

    for i in range(len(string_to_be_generated)):
        if try_this[i] != string_to_be_generated[i]:
            completed = False
            try_next += random.choice(possible_characters)
        else:
            try_next += string_to_be_generated[i]
    tentatives += 1
    try_this = try_next
    time.sleep(0.1)

print(str(tentatives))