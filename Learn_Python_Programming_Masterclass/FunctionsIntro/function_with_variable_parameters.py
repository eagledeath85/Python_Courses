
# The *arg notation indicates the function can accept variable quantity of this parameter
def sum(*numbers) -> int:
    result = 0
    for n in numbers:
        result += n
    return result


# The **kwarg notation indicates the function can accept key-value pairs
def new_sum(title, **numbers) -> int:
    result = 0
    for i in numbers.values():
        result += i
    return result


print(sum(5, 8, 6, 2, 3))
print(sum(4, 3, 6))

print((new_sum("SUM", maths=15, english=13, history=17)))
print(new_sum("GRADES", philosophy=10, physics=14))