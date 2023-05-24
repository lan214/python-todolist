file = open("members.txt", "r")
members = file.readlines()
file.close()

member = input("Add a new member:")
members.append(member + "\n")

file = open("members.txt", "w")
file.writelines(members)