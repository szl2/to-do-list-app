FILE_PATH = "todos.txt"

def get_todos(filepath=FILE_PATH):
    """read a text file and return a list of to-do items"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILE_PATH):
    """write a list of todos into the todos.txt text file """
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())