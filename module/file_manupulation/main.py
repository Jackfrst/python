def user_input():
    prompt = "Enter any input: "
    _input_string_ = input(prompt)
    return _input_string_.strip().capitalize()


def file_add(file_element):
    file = open("text.txt", 'r')
    todo = file.readlines()
    file.close()

    todo.append(file_element)
    print(todo)

    file = open("text.txt", 'w')
    file.writelines(todo)
    file.close()


if __name__ == '__main__':
    while True:
        input_string = user_input() + "\n"
        print(input_string)
        file_add(input_string)
