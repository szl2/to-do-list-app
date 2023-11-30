import functions

import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is", now)

while True:
    # Update todos from the todos.txt in a list
    todos = functions.get_todos()

    # Ask for user action
    user_prompt = "Type add, show, edit, complete, or exit: "
    user_action = input(user_prompt)
    user_action = user_action.strip().lower()

    # Process user command
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"
        todos.append(todo.capitalize())

    elif user_action.startswith('show'):
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
        except ValueError:
            print("The command is not valid")
            continue

        try:
            todos[number]
        except IndexError:
            print("Index is out of range")
            continue

        new_todo = input("Enter new todo: ") + "\n"
        todos[number] = new_todo

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1
        except ValueError:
            print("The command is not valid")
            continue

        try:
            todos[number]
        except IndexError:
            print("Index is out of range")
            continue

        todo_to_remove = todos[number].strip("\n")
        todos.pop(number)
        print(f'{todo_to_remove} is completed.')

    elif user_action == 'exit':
        print('Bye!')
        break

    else:
        print("Invalid Command")

    # update the todos.txt file
    functions.write_todos(todos)
