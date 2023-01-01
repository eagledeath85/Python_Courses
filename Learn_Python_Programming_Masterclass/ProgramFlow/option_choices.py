# This is the standard code format to create a menu
# where a user needs to choose an option from

input_choice = " "
while input_choice != "0":
    if input_choice in {"1", "2", "3", "4", "5"}:
        print("You've type {0}".format(input_choice))
    else:
        print("Please choose one the options below: "
              "\n1. Learn Python"
              "\n2. Learn Java"
              "\n3. Learn other language"
              "\n4. Go to the restaurant"
              "\n5. Go to the cinema"
              "\n6. Stay at home"
              "\n7. Go to bed"
              "\n0. Exit\n")
    input_choice = input()
