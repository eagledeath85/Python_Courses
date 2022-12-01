import math

user_input = int(input("Please enter an integer: "))


def __isPerfectSquare(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        #print(number, " is a perfect square")
        return True
    else:
        #print(number, " is not a perfect square")
        return False


def __isFibonnaciNumber(n):
    if __isPerfectSquare(5*n*n +4) == True or __isPerfectSquare(5*n*n -4) == True:
        print(n, "is a Fibonnaci number")
        return True
    else:
        print(n, "is not a Fibonnaci number")
        return False


#print(__isPerfectSquare(user_input))
print(__isFibonnaciNumber(user_input))
