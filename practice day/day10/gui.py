from manupulation_module import todo_manupulation as tm
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App',
                   font=('Helvetica', 20),
                   layout=[[label], [input_box, add_button]])
while True:
    event, values = window.read()
    print(values["todo"])
    match event:
        case "Add":
            tm.add_todo(values["todo"])


window.close()

