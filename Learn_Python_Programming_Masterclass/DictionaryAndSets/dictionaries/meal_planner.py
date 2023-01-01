from contents import pantry, recipes


def add_missing_items_to_shopping_list(shopping_list_to_build: dict, food_item_to_buy: str,
                                       item_quantity_to_buy: int) -> None:
    """
    Adding missing_item and amount to a dictionnary
    :param shopping_list_to_build: dictionary containing item and minimum quantity to buy
    :param food_item_to_buy: item to buy
    :param item_quantity_to_buy: quantity of the item to buy
    :return: shopping list as a dictionnary
    """
    # if food_item_to_buy in shopping_list_to_build:
    #     shopping_list_to_build[food_item_to_buy] += item_quantity_to_buy
    # else:
    #     shopping_list_to_build[food_item_to_buy] = item_quantity_to_buy

    #This line of code is equivalent to the if/else above
    shopping_list_to_build[food_item_to_buy] = shopping_list_to_build[food_item_to_buy, 0] + quantity_to_buy


# With dictionary comprehension
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
    # Checking with what we're working
    # print(index, key)
    # Populating display_dict dictionary with index-key from enumerate(recipes)
    display_dict[str(index + 1)] = key

print(display_dict)
shopping_list = {}

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
                add_missing_items_to_shopping_list(shopping_list, food_item, quantity_to_buy)
        print("+++++++++++++++++++++++++++++++++++")
    #     if len(shopping_list) != 0:
    #         print("Here is your shopping list ready to download: ")
    #         for food_item, quantity_to_buy in shopping_list.items():
    #             print(f"{food_item} - {quantity_to_buy}")
    # print()
for things in sorted(shopping_list.items()):
    print(things)