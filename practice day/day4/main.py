user_choice_prompt = "Enter your choice between add,edit,show and exit :"
user_prompt = "Enter a Todo :"
user_edit_option = "Enter the Todo number That you want to edit :"

todo_list = []

while True:
    user_choice = input(user_choice_prompt).lower().strip()
    match user_choice:
        case "add":
            new_todo = input(user_prompt).capitalize()
            todo_list.append(new_todo)
        case "edit":
            todo_edit_index = int(input(user_edit_option).strip())
            todo_list[todo_edit_index - 1] = input(user_prompt)
        case "show":
            for item in todo_list:
                print(item)
        case "exit":
            break
        case error:
            print("You have entered a unknown command")

print("bye bye")
