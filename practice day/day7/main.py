user_choice_prompt = "Enter your choice between add,edit,complete,show and exit :"
user_prompt = "Enter a Todo :"
user_edit_option = "Enter the Todo number That you want to edit :"
user_complete_option = "Enter the Todo number That you want to mark as complete :"


def add_todo():
    new_todo = input(user_prompt).capitalize() + "\n"

    with open('files/todos.txt', 'r') as file:
        todo_list = file.readlines()

    todo_list.append(new_todo)

    with open('files/todos.txt', 'w') as file:
        file.writelines(todo_list)


def edit_todo():
    print("Existing Todo:")
    show_todo()

    with open('files/todos.txt', 'r') as file:
        todo_list = file.readlines()

    todo_edit_index = int(input(user_edit_option).strip())

    if todo_edit_index < 0 or todo_edit_index > len(todo_list):
        print("You have entered an invalid index")
    else:
        todo_list[todo_edit_index - 1] = input(user_prompt).capitalize() + "\n"
        with open('files/todos.txt', 'w') as file:
            file.writelines(todo_list)
        print("New Todo:")
        show_todo()


def show_todo():
    with open('files/todos.txt', 'r') as file:
        todo_list = file.readlines()

    for index, item in enumerate(todo_list):
        print(f"{index + 1}. {item.strip("\n")}")


def complete_todo():
    print("Existing Todo:")
    show_todo()

    with open("files/todos.txt", "r") as file:
        todo_list = file.readlines()

    todo_complete_index = int(input(user_complete_option).strip())

    if todo_complete_index < 0 or todo_complete_index > len(todo_list):
        print("You have entered an invalid index")
    else:
        todo_list.pop(todo_complete_index - 1)
        with open("files/todos.txt", "w") as file:
            file.writelines(todo_list)

        print("New Todo:")
        show_todo()


while True:
    user_choice = input(user_choice_prompt).lower().strip()
    match user_choice:
        case "add":
            add_todo()
        case "edit":
            edit_todo()
        case "show":
            show_todo()
        case "complete":
            complete_todo()
        case "exit":
            break
        case error:
            print("You have entered a unknown command")

print("bye bye")
