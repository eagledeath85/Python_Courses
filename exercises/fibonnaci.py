def Fibonnaci(n):
    if n < 0:
        print("Wrong input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonnaci(n-1) + Fibonnaci(n-2)


print(Fibonnaci(30))
