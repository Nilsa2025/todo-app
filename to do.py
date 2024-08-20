# # user_promp="Enter a to do: "
# # text=input(user_promp)
# # print(text)
# user_prompt="enter a to do:"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
# todos=[todo1,todo2,todo3]
# print(todos)
# name=input("first name: ")
# family=input("last name: ")
# print(name,family)
# print(name.capitalize(),family.capitalize())
# print(name.upper(),family.upper())
# user_prompt="Enter a todo"
# todos=[]
# while True:
#     todo=input(user_prompt)
#     todos.append(todo)
#     # print(todos)
# import functions
from functions import set_todos,get_todos


user_prompt= "Enter a todo:"
todos=[]
while True:
    user_action=input("Enter add,show,edit,exit or complete:")
    # if "add" in user_action or "new" in user_action:
    if user_action.startswith("add"):
        # todo=input("Enter a todo:")+"\n"
        todo=user_action[4:]+"\n"
        #
        # with open("todos.txt","r")as file:
        #    todos=file.readlines()
        todos = get_todos()

        todos.append(todo)

        # with open("todos.txt", "w") as file:
           # file.writelines(todos)
        set_todos(todos)

    # elif "show" in user_action:
    elif user_action.startswith("show"):

        # with open("todos.txt", "r") as file:
        #     todos = file.readlines()
        todos = get_todos()

        for index,todo in enumerate(todos):
            todo=todo.strip("\n")
            print(index+1,"_",todo)
    # elif "edit" in user_action:
    elif user_action.startswith("edit"):
        try:
            todos=get_todos()

            number =user_action[5:]

            number = int(number) - 1
            new_todo = input("Enter a todo: ")+"\n"
            todos[number] = new_todo

            # with open("todos.txt", "w") as file:
                # file.writelines(todo)
            set_todos(todos)

        except IndexError:
            print("Your Index is out of range")

    # elif "complete" in user_action:
    elif user_action.startswith("complete"):
        todos = get_todos()
        # number = int(input("Enter a number to complete: "))
        number = user_action[9:]
        number= int(number)-1

        todo_to_remove=todos[int(number)].strip("\n")
        todos.pop(number)
        print(f"Todo {todo_to_remove} has been completed!")

        # with open("todos.txt", "w") as file:
        #     file.writelines(todos
        set_todos(todos)

    # elif "exit" in user_action:
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")
print("Done")




