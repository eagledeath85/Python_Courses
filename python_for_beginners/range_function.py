# range with 1 argument

def one_argument():
    one_input = range(5)
    for num in one_input:
        print(num)


def two_arguments():
    two_input = range (5, 10)
    for num in two_input:
        print(num)


def three_arguments():
    three_input = range(20, 0, -2)
    for num in three_input:
        print(num)


one_argument()
print("###########")
two_arguments()
print("###########")
three_arguments()

