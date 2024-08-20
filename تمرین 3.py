with open("file,txt","w") as file:
    file.write("Hello you")

with open("file,txt","r") as file:
    content = file.read()
    print(content)
    print(len(content))
