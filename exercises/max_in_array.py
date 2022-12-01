array = [233, 34, 654, -894]
n = len(array)


def __find_max(arr, array_length):
    maximum = arr[0]
    for i in range(1, array_length):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum


print(__find_max(array, n))
