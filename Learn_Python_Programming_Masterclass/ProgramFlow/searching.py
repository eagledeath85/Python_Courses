shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# searching by index
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("Item found at position {0}".format(found_at))

# Another way to find the index of the item_to_find can be like this:
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
print(found_at)