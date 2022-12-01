# Dictionnary Declaration
dictionnary_1 = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Accessing values in dictionnary
value = dictionnary_1["key1"]
print(value)

# Checking weither or not values are in the dictionnary

check1 = "key1" in dictionnary_1
check2 = "key2" not in dictionnary_1
print(check1)
print(check2)

# .keys() method allows to get all the keys from a dictionnary
print(dictionnary_1.keys())
for key in dictionnary_1.keys():
    print(key)

# .values() method allows to get all the values from a dictionnary
print(dictionnary_1.values())
for value in dictionnary_1.values():
    print(value)

# .items() method allows to get key-value pair from a dictionnary
print(dictionnary_1.items())
for item in dictionnary_1.items():
    print("this is item", item)
for key, value in dictionnary_1.items():
    print(key, value)

# .get() method allows to look for and to get a key from a dictionnary,
# and return something other than an error message
# Syntax is dictionnary_name.get(key, "error to return if the key is not found)
print(dictionnary_1.get("key4", "This is not a key from this dictionnary"))

# .fromkeys() method allows to create key-pair value from any type of data
# It should always be used on an empty dictionnary
# Syntax is like this
ex_1 = {}.fromkeys(["key_1"], "value_1")
print(ex_1)

# .pop() method allows to remove a key-value pair from a dictionnary
car_dictionnary = {"make": "Honda", "model": "civic", "year": 2005}
truncated = car_dictionnary.pop("model")
print(car_dictionnary)
print(truncated)

# .popitem() method allows to remove the last key-value pair from a dictionnary without having to give it an argument
ex_3 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "H&R block"}
ex_3.popitem()
print(ex_3)

# .clear() method removes everything from a dictionnary that it is called on
ex_4 = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print(ex_4.clear())

#.copy() method allows to make a copy of the dictioonnary itself
birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years)
people = birth_years.copy()
people[1982] = "madeline"
print(people)
print(birth_years)

# .update() method allows to add key-value pairs from one dictionnary to another
# or overwrite the values of existing keys in a dictionnary with values from another dictionnary
city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto", "population": 20}
print(city_info)
population = {"population": 2930000}
city_info.update(population)
print(city_info)

# .setdefault() method allows to check whether keys exist in a dictionnary and add them if not
# it replace the following piece of code:
computers = {"Google": "Chromebook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"
print("computers", computers)
# The if statement above is performed by the setdefault method. Therefore, setdefault() doesn't
computers.setdefault("Lenovo", "ThinkPad")

# .dict() method is another way to create a dictionnary
empty = dict()
print("empty", empty)
with_values = dict(key1="value1", key2="value2", key3="value3")
print(with_values)