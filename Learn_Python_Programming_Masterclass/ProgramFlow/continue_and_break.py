# The continue keyword allows to skip running the loop code after it for a specific value

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    print("Buy", item)

print("------------")
# Searching by index
for item in shopping_list:
    if item == "spam":
        continue
    print(item)

# The break keyword allows to jump out of the loop code when the value is met
print("------------")
for item in shopping_list:
    if item == "spam":
        break
    print(item)