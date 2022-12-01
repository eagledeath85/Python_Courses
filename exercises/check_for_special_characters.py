import re

input_string = "Geeks$For$Geeks"

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

if regex.search(input_string) == 0:
    print("String", input_string,  "is OK")
else:
    print("String", input_string, "is not OK")
