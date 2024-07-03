from manupulation_module import todo_manupulation as tm
from manupulation_module import file_manupulation as fm
import PySimpleGUI as sg

import time

sg.theme("Black")

label = sg.Text("Type in a to-do")
clock = sg.Text("", key="clock")
input_box = sg.InputText(tooltip="Enter todo", key="input")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fm.get_todo("files/todos.txt"),
                      key='list_of_todos',
                      enable_events=True,
                      size=(45, 10)
                      )
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
window = sg.Window('My To-do App',
                   font=('Helvetica', 20),
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                           ]
                   )

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # todo = values["todo"].lower().strip()
    """IT Strip 1st 4 latter"""
    match event:
        case "Add":
            todos = fm.get_todo('files/todos.txt')
            new_todo = values['input'] + '\n'
            todos.append(new_todo)
            fm.set_todo('files/todos.txt', todos)
            window['list_of_todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["list_of_todos"][0]
                new_todo = values['input']
                todos = fm.get_todo('files/todos.txt')
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                fm.set_todo('files/todos.txt', todos)
                window['list_of_todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit!!",
                         title="Warning",
                         font=('Helvetica', 10)
                         )

        case 'Complete':
            try:
                todo_to_complete = values["list_of_todos"][0]
                todos = fm.get_todo('files/todos.txt')
                todos.remove(todo_to_complete)
                fm.set_todo('files/todos.txt', todos)
                window['list_of_todos'].update(values=todos)
                window['input'].update(value="")
            except IndexError:
                sg.popup("Please select an item to complete!!",
                         title="Warning",
                         font=('Helvetica', 10)
                         )
        case 'Exit':
            exit()

        case 'list_of_todos':
            window['input'].update(value=values['list_of_todos'][0])

        case sg.WINDOW_CLOSED:
            exit()
