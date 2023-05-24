filenames = ["file 1", "file 2"]
for filename in filenames:
    file = open(filename, "w")
    file.write("Hello")
    file.close()