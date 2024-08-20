# # for i in range(1,5):
# #     for j in range(1,5):
# #         print("*",end="")
# #     print()
# # for i in range (0,5):
# #     for j in range (0,i):
# #         print("*",end="" )
# user_prompt="Enter todo"
# todos=[]
# while True:
#     user_action=input("Enter edit:")
#     match user_action:
#         case "Edit":
#             todo=input("Enter a todo:")
#             todos.edit(todo)
#             list=[1,2]
#             list=[0+1]
#    print
m=int(input("Enter row: "))
n=int(input("Enter column: "))
for i in range (0,m):
    for j in range(0,n):
        if i==0 or i==m-1 or j==0 or j==n-1:
            print("*", end="")
        else:
            print(" ",end="")
    print()
