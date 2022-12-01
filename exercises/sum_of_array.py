array = [54, 7, 95, 76, 3]


def __sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

answer = __sum(array)
print("The sum of the array is", answer)
