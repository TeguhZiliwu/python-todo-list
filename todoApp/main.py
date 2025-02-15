todoPrompt = "Enter a title : "
userPrompt = "Type add, show, or exit : "
todos = []

while True:
    user_action = input(userPrompt)

    match user_action.lower():
        case "add":
            todo = input(todoPrompt)
            todos.append(todo.title())
        case "show":
            print("List of todo :")
            for item in todos:
                print(item)
        case "exit":
            break

print("Program exit!")