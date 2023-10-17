user_prompt = "Enter todo: "
todo_list = []
user_input = ""

while user_input.lower() != "exit":
    todo_list.append(user_input.capitalize())
    user_input = input(user_prompt)

print(todo_list)
