def add_todo(new_todo):
    with open('files/todos.txt', 'r') as file:
        todo_list = file.readlines()

    todo_list.append((new_todo + "\n").capitalize())

    with open('files/todos.txt', 'w') as file:
        file.writelines(todo_list)

    print(todo_list)

def show_todo():
    

if __name__ == '__main__':
    user_choice_prompt = "Enter your choice between add,edit,complete,show,exit:"
    user_todo_prompt = "Enter the todo :"
    user_edit_option = "Enter the Todo number that you want to edit :"
    user_complete_option = "Enter the TODO number you want to mark as complete :"

    while True:
        user_choice = input(user_choice_prompt).lower().strip()
        if "add" in user_choice:
            add_todo(user_choice[4:])
        elif "show" in user_choice:
            show_todo()
        elif "exit" in user_choice:
            break
        else:
            print("You have entered an unknown command")
    print("System shutting down....")
