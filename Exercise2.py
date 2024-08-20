def speed(distance,time):
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return distance / time


print(speed(200,4))
