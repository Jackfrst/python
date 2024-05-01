user_choice_prompt = "Enter add, show or exit: "
user_input_prompt = "Enter todo: "

todo_list = []

while True:
    user_action = input(user_choice_prompt).strip()

    match user_action.strip():
        case "add":
            todo = input(user_input_prompt)
            todo_list.append(todo)
        case "show" | "display":
            for item in todo_list:
                print(item.capitalize())
        case "exit":
            break
        case "error":
            print("Hey you entered and unknown command.")

print("Bye")
