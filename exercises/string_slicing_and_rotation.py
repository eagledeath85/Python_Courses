input_String = "qwertyu"
rotation = 4

Lrotation = input_String[0:rotation]
Rrotation = input_String[rotation:]

print(Lrotation, Rrotation)
new_string = str([Rrotation + Lrotation])
print(new_string)