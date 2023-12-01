import functions
import PySimpleGUI as sg
import os
import time

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")
clock = sg.Text("", key="Clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do Item Here...",
                         key='todo_item')
add_button = sg.Button("Add")
list_items = sg.Listbox(values=functions.get_todos(),
                        key="list_todos",
                        enable_events=True,
                        size=(45,10),)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-Do List",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_items, edit_button, complete_button],
                           [exit_button]
                          ],
                   font=("Helvetic", 20)
                   )

while True:
    event, value = window.read(timeout=100)
    window["Clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))

    # maintain scroll position
    scroll_position = window['list_todos'].Widget.yview()

    match event:
        case "Add":
            todos = functions.get_todos()
            if value['todo_item'] == '':
                continue
            todos.append(value['todo_item']+"\n")
            functions.write_todos(todos)
            window['list_todos'].update(values=todos)
            window['todo_item'].update(value='')
        case "Edit":
            try:
                todos = functions.get_todos()
                todo_to_edit = value['list_todos'][0]
                new_todo = value['todo_item'] + '\n'
                if value['todo_item'] == '':
                    continue
                idx = todos.index(todo_to_edit)
                todos[idx] = new_todo
                functions.write_todos(todos)
                window['list_todos'].update(values=todos)
                window['todo_item'].update(value='')

            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "list_todos":
            window['todo_item'].update(value=value['list_todos'][0].strip('\n'))
        case "Exit":
            break
        case "Complete":
            try:
                todo_to_complete = value['list_todos'][0]
                todos = functions.get_todos()
                idx = todos.index(todo_to_complete)
                todos.pop(idx)
                functions.write_todos(todos)
                window['list_todos'].update(values=todos)
                window['todo_item'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case sg.WIN_CLOSED:
            break
    window['list_todos'].Widget.yview_moveto(scroll_position[0])
window.close()