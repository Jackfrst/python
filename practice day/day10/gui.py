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
    print(values["todo"])
    todo = values["todo"].lower().strip()
    """IT Strip 1st 4 latter"""
    match event:
        case "Add":
            tm.add_todo(todo)
        case sg.WINDOW_CLOSED:
            break

window.close()

