file = open("journal.txt", "w")
lines = ["hello\n", "Hi Roman\n", "Hi friends\n"]
file.writelines(lines)
file.close()

file = open("journal.txt", "a")
file.write = ("open", "banana", "orange")
file.close()

file = open("journal.txt", "r")
x = file.read()
print(x)
file.close()

file = open("journal.txt", "r")
x = file.readline()
for line in file:
    print(line , end="")

file.close()

