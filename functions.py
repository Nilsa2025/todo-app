def get_todos():
    """
        please use this function whenever
        you wanna have todos list
        :return: todos list
    """
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


def set_todos(todos):
    """
        gets the todos list and
        savew it in a txt file
    :param todos: list of todos`
    """

    with open('todos.txt', 'w') as file:
        file.writelines(todos)