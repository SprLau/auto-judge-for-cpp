file1 = open("stdout", "r")
file2 = open("testout", "r")
file3 = open("data.txt", "r")

list1 = file1.readlines()
list2 = file2.readlines()
list3 = file3.readlines()

def print_all(list):
	for str in list:
		print(str, end="")
	print("\n")

err = False

for (str1, str2) in zip(list1, list2):
	if str1 != str2:
		print("---- DIFF FOUND! ----")
		print("***" + str1 + "***")
		print("***" + str2 + "***\n")
		print("-> data:")
		print_all(list3)
		print("-> std:")
		print_all(list1)
		print("-> test:")
		print_all(list2)
		print("---------------------")
		err = True
		break

if not err:
	print("----- ACCEPTED! -----")
