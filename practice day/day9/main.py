user_choice_prompt = "Enter your choice between add,edit,complete,show and exit :"
user_prompt = "Enter a Todo :"
user_edit_option = "Enter the Todo number That you want to edit :"
user_complete_option = "Enter the Todo number That you want to mark as complete :"


def add_todo(new_todo):
    with open('files/todos.txt', 'r') as file:
        todo_list = file.readlines()

    todo_list.append((new_todo[4:] + "\n").capitalize())

    with open('files/todos.txt', 'w') as file:
        file.writelines(todo_list)


def edit_todo(todo_edit):
    print("Existing Todo:")
    show_todo()

    with open('files/todos.txt', 'r') as file:
        todo_list = file.readlines()

    todo_edit_index = int(todo_edit[5:])

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


def complete_todo(complete_choice):
    print("Existing Todo:")
    show_todo()

    with open("files/todos.txt", "r") as file:
        todo_list = file.readlines()

    todo_complete_index = int(complete_choice[9:])

    if todo_complete_index < 0 or todo_complete_index > len(todo_list):
        print("You have entered an invalid index")
    else:
        todo_to_remove = todo_list[todo_complete_index - 1].strip('\n')
        todo_list.pop(todo_complete_index - 1)
        with open("files/todos.txt", "w") as file:
            file.writelines(todo_list)

        print(f"--> {todo_to_remove} is removed from the list")
        print("New Todo:")
        show_todo()


while True:
    user_choice = input(user_choice_prompt).lower().strip()
    if user_choice.startswith("add"):
        add_todo(user_choice)
    elif user_choice.startswith("edit"):
        try:
            edit_todo(user_choice)
        except ValueError:
            print("Your command is invalid, try using format as: [edit _index_]")
            continue
    elif user_choice.startswith("show"):
        show_todo()
    elif user_choice.startswith("complete"):
        complete_todo(user_choice)
    elif user_choice.startswith("exit"):
        break
    else:
        print("You have entered a unknown command")
print("bye bye")
