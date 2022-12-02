def square_numbers(*args: int) -> int:
    print("Number\t\tSquare Number")
    for value in args:
        print("{0}\t\t\t{1}".format(value, value**2))


square_numbers(1, 2, 3, 4, 5)