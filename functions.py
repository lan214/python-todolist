import os

FILENAME = "todos.txt"

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w'):
        pass


def get_todos(filename=FILENAME):
    """ Read a text file and return the list of to-do items. """
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILENAME):
    """ Write the to-do items list in a text file. """
    with open(filename, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
