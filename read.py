read = open("data.txt", "r")

list = read.readlines()

for str in list:
    print(str, end="")
