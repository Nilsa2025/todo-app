temperatures = [10, 12, 14]

file = open("file.txt", 'w')

temperatures = [str(i)+"\n" for i in temperatures]

file.writelines(temperatures)
