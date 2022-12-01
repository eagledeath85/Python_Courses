# Python cannot concatenate string and numbers
# To do so, we must coerce the numbers into string using the str() function

name = "Frank"
age = 24
occupation = "student"
print("My age is " + str(age) + " years")

# The .format() method allows to do the same thing

print("My age is {0} years and I'm a {1}".format(age, occupation))
print("There are {0} days in {1},"
      "{2}, "
      "{3}, "
      "{4}, "
      "{5}, "
      "{6}"
      " and {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

# the f-strings shortcut allows to concatenate strings and numbers in the output
print(name + f"is {age} years old")
print(type(age))
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
