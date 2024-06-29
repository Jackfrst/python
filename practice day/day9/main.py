import todo_manupulation as tm

user_choice_prompt = "Enter your choice between add,edit,complete,show and exit :"
user_prompt = "Enter a Todo :"
user_edit_option = "Enter the Todo number That you want to edit :"
user_complete_option = "Enter the Todo number That you want to mark as complete :"

while True:
    user_choice = input(user_choice_prompt).lower().strip()
    if user_choice.startswith("add"):
        tm.add_todo(user_choice)
    elif user_choice.startswith("edit"):
        try:
            tm.edit_todo(user_choice, user_prompt)
        except ValueError:
            print("Your command is invalid, try using format as: [edit _index_]")
            continue
    elif user_choice.startswith("show"):
        tm.show_todo()
    elif user_choice.startswith("complete"):
        tm.complete_todo(user_choice)
    elif user_choice.startswith("exit"):
        break
    else:
        print("You have entered a unknown command")
print("bye bye")
