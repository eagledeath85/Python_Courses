import math

for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print("##############################")
# We can format the output by adding width to the values in {}.
# Syntax is {0:width} for right alignment
for j in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(j, j ** 2, j ** 3))

# Syntax is {0: <width} for left alignment
print("##############################")
for j in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(j, j ** 2, j ** 3))

# Syntax is {0: ^width} for center alignment
print("##############################")
for j in range(1, 13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(j, j ** 2, j ** 3))

# Syntax to give float approximation number is {0:width.nb_of_float_decimal}
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))