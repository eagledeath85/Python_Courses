# Local variables cannot be used by code in the global scope
def loc_ex():
    breakfast = "wafles"
    return breakfast


loc_ex()
print(breakfast) # breakfast is undefined in the global scope


# Global variables can be accessed by code in a local scope
def print_glob_1():
    print(glob_var)


def print_glob_2():
    loc_var = "that is very long"
    print(glob_var + loc_var)


glob_var = "This is a string"
print_glob_1()
print_glob_2()


# The local scope of one function cannot use variables
# from another function's local scope
def first():
    loc = 2
    return loc


def second():
    return loc

first()
second()


# You can use the same name for different variables
# as long as they are in different scopes
def loc_ex1():
    fruit = "pear"
    print(fruit)


def loc_ex2()
    fruit = "banana"
    print(fruit)


fruit = "apple"
loc_ex1()
loc_ex2()
print(fruit)


# Assigning a global variable a new value from within a function
# can be done with Global Statements
def loc_ex3():
    global fruit
    fruit = "pear"
    print(fruit)


fruit = "apple"
loc_ex3()
print(fruit)
