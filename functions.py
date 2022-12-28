def addmode():
    """  Enters add mode and allow user to input a series of todos
    :return nothing:
    """
    todos = get_todos()
    while True:
        todo = input("Enter a todo (enter empty to exit): ") + "\n"
        if len(todo.strip()) <= 0:
            break
        else:
            todos.append(todo)

    file = open('todos.txt', 'w')
    file.writelines(todos)
    file.close()

def get_todos(filepath="todos.txt"):
    file = open(filepath, 'r')
    todos = file.readlines()
    file.close()
    return todos
def write_todos(todos, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos)

def showtodo():
    """
    Reads a file and print outs the todos on screen
    :return:
    """
    todos = get_todos()
    print("Todos: ")
    todos = [item.strip('\n') for item in todos]

    for i, item in enumerate(todos):
        # item = todos[i].title().strip('\n')  # capitalize and replace the breakline with empty
        item = todos[i].title()
        row = f"{i + 1}-{item}"
        print(row)
    return todos

if __name__ == "__main__":
    print(get_todos())