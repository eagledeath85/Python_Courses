def sum_eo(n, t):
    sum = 0
    if t == 'e':
        for number in range(0, n):
            if number % 2 == 0:
                sum += number
        return sum
    elif t == 'o':
        for number in range(0, n):
            if (number + 1) % 2 == 0:
                sum += number
        return sum
    else:
        return -1


result = sum_eo(11, 'spam')
print(result)