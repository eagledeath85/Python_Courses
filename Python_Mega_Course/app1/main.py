todos = []
user_choice = None

while True:
    user_choice = input("Please enter your choice: Add, Show or Exit ")
    match user_choice.casefold().strip():   # strip() removes all unwanted spaces
        case "add":
            todo = input("Please enter a todo to add to the todos list: ")
            todos.append(todo)
        case "show":
            for todo in todos:
                print(todo.capitalize())
        case other:
            break
