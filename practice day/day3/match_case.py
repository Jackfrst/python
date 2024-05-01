user_choice_prompt = "Enter add, show or exit: "
user_input_prompt = "Enter todo: "

todo_list = []

while True:
    user_action = input(user_choice_prompt)

    match user_action:
        case "add":
            todo = input(user_input_prompt)
            todo_list.append(todo)
        case "show":
            print(todo_list)
        case "exit":
            break

print("Bye")
