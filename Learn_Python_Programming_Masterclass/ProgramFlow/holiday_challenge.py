name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("{0}, you are {1} year old, therefore you ARE eligible to the holiday".format(name, age))
else:
    print("{0}, you are {1} year old, therefore you are NOT eligible to the holiday".format(name, age))