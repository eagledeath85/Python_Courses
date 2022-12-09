from contents import pantry, recipes

# With dictionary comprehension
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
    # Checking with what we're working
    # print(index, key)
    # Populating display_dict dictionary with index-key from enumerate(recipes)
    display_dict[str(index + 1)] = key
print(display_dict)


while True:
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking the ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            # Checking the food_item amount left in pantry, return 0 by default
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{food_item} - OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"You need to buy {quantity_to_buy} of {food_item}")