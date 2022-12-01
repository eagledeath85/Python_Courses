# else can also be present at the end of a for loop, as a sort of default value
# else defines a block that always executes if the loop finishes without break
# In this case, the else is at the same indentation level as the for

numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        print("Those numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
