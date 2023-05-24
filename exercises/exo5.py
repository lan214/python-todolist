# Exo 1
filenames = ['document', 'report', 'presentation']
for i, filename in enumerate(filenames):
    print(f"{i}-{filename.capitalize()}.txt")

# Exo 2
ips = ['100.122.133.105', '100.122.133.111']
index = int(input("Enter the index of the IP you want: "))
print(f"You chose {ips[index]}")