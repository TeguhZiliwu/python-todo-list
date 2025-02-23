todoPrompt = "Enter a title : "
userPrompt = "Type add, show, or exit : "
todos = []

while True:
    user_action = input(userPrompt)
    user_action = user_action.strip()

    match user_action.lower():
        case "add":
            todo = input(todoPrompt)
            todos.append(todo.title())
        case "show" | "display":
            print("List of todo :")
            for item in todos:
                print(item)
        case "exit":
            break
        case randomCommand:
            print("Hey, you entered an unknown command!")

print("Program exit!")