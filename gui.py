import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do Item Here...",
                         key='todo_item',
                         do_not_clear=False)
add_button = sg.Button("Add")
list_items = sg.Listbox(values=functions.get_todos(),
                        key="list_todos",
                        enable_events=True,
                        size=(45,10),)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-Do List",
                   layout=[[label],
                           [input_box, add_button],
                           [list_items, edit_button, complete_button],
                           [exit_button]
                          ],
                   font=("Helvetic", 20)
                   )

while True:
    event, value = window.read()
    print(event)
    print(value)
    print(value['list_todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            if value['todo_item'] == '':
                continue
            todos.append(value['todo_item']+"\n")
            functions.write_todos(todos)
            window['list_todos'].update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            todo_to_edit = value['list_todos'][0]
            new_todo = value['todo_item'] + '\n'
            if value['todo_item'] == '':
                continue
            idx = todos.index(todo_to_edit)
            todos[idx] = new_todo
            functions.write_todos(todos)
            window['list_todos'].update(values=todos)
        case "list_todos":
            window['todo_item'].update(value=value['list_todos'][0].strip('\n'))
        case "Exit":
            break
        case "Complete":
            todo_to_complete = value['list_todos'][0]
            todos = functions.get_todos()
            idx = todos.index(todo_to_complete)
            todos.pop(idx)
            functions.write_todos(todos)
            window['list_todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break




window.close()

