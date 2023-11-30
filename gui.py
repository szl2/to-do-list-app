import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter To-Do Item Here...",
                         key='todo_item',
                         do_not_clear=False)
add_button = sg.Button("Add")

window = sg.Window("To-Do List",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetic", 20)
                   )

while True:
    todos = functions.get_todos()

    event, value = window.read()
    print(event, value)

    match event:
        case "Add":
            if value['todo_item'] == '':
                continue
            todos.append(value['todo_item']+"\n")
            print(todos)
        case sg.WIN_CLOSED:
            break

    functions.write_todos(todos)


window.close()

