from manupulation_module import file_manupulation as fm


def add_todo(new_todo):
    todo_list = fm.get_todo('files/todos.txt')
    # todo_list.append((new_todo[4:] + "\n").capitalize())
    todo_list.append((new_todo + "\n").capitalize())
    fm.set_todo('files/todos.txt', todo_list)


def edit_todo(todo_edit, user_prompt):
    print("Existing Todo:")
    show_todo()

    todo_list = fm.get_todo('files/todos.txt')

    todo_edit_index = int(todo_edit[5:])

    if todo_edit_index < 0 or todo_edit_index > len(todo_list):
        print("You have entered an invalid index")
    else:
        todo_list[todo_edit_index - 1] = input(user_prompt).capitalize() + "\n"
        fm.set_todo('files/todos.txt', todo_list)
        print("New Todo:")
        show_todo()


def show_todo():
    todo_list = fm.get_todo('files/todos.txt')

    for index, item in enumerate(todo_list):
        print(f"{index + 1}. {item.strip("\n")}")


def complete_todo(complete_choice):
    print("Existing Todo:")
    show_todo()

    todo_list = fm.get_todo('files/todos.txt')

    todo_complete_index = int(complete_choice[9:])

    if todo_complete_index < 0 or todo_complete_index > len(todo_list):
        print("You have entered an invalid index")
    else:
        todo_to_remove = todo_list[todo_complete_index - 1].strip('\n')
        todo_list.pop(todo_complete_index - 1)
        fm.set_todo('files/todos.txt', todo_list)

        print(f"--> {todo_to_remove} is removed from the list")
        print("New Todo:")
        show_todo()
