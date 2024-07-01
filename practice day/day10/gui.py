from manupulation_module import todo_manupulation as tm
from manupulation_module import file_manupulation as fm
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fm.get_todo("files/todos.txt"),
                      key='todos',
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")
window = sg.Window('My To-do App',
                   font=('Helvetica', 20),
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    # todo = values["todo"].lower().strip()
    """IT Strip 1st 4 latter"""
    match event:
        case "Add":
            todos = fm.get_todo('files/todos.txt')
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fm.set_todo('files/todos.txt', todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']
            todos = fm.get_todo('files/todos.txt')
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fm.set_todo('files/todos.txt', todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
