# for loop enables to iterate through an iterable
# iterable can be a sequence or a range

# It is possible to iterate by item or by index
# When iterating by item, the syntax is "for item in list_of_items: do something
# When iterating by index or range, the length must be one item more than the actual desired range

# Iterating via item
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    print(item)

print("-" * 30)

# Iterating via index
for i in range(0, 11):
    print(i)

print("-" * 30)

for i in range(101):
    if i % 7 == 0:
        print(i)
