def get_todo(filepath):
    with open(filepath, 'r') as file:
        todo = file.readlines()
    return todo


def set_todo(filepath, todo_list):
    with open(filepath, 'w') as file:
        file.writelines(todo_list)
