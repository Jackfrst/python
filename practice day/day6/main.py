user_choice_prompt = "Enter your choice between add,edit,complete,show and exit :"
user_prompt = "Enter a Todo :"
user_edit_option = "Enter the Todo number That you want to edit :"
user_complete_option = "Enter the Todo number That you want to mark as complete :"

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
            for index, item in enumerate(todo_list):
                print(f"{index + 1}. {item}")
        case "complete":
            todo_complete_index = int(input(user_complete_option).strip())
            if todo_complete_index < 0:
                print("You have entered an invalid index")
            else:
                todo_list.pop(todo_complete_index - 1)
        case "exit":
            break
        case error:
            print("You have entered a unknown command")

print("bye bye")
