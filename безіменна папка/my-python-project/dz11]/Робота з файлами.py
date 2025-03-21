# r - читанння файлу
# w - режим запису файлу
# a - додавання файлу в кінець
# 
# 



# file = open('jorurnal.txt' , 'w')
# file.write('Hello world')
# file.close()


# file = open('jorurnal.txt' , 'r')
# content = file.read()
# print(content)
# file.close()

# file = open('jorurnal.txt' , 'w')
# file.write('Radislav')
# file.close()

# file = open('jorurnal.txt' , 'r')
# content = file.read()
# print(content)
# file.close()

# file = open('jorurnal.txt' , 'a')
# file.write('Hello world')
# file.close()

# file = open('jorurnal.txt' , 'r')
# content = file.read()
# print(content)
# file.close()


# import os

# if os.path.exists('jorurnal.txt'):
#     file = open('jorurnal.txt' , 'r')
#     print(file.read())
#     file.close()
# else:
#     print('File not found')


file = open('jorurnal.txt' , 'w')
lines = ['hello! and welcome to \n' , 'the LOS POLLOS HERMANOS\n']
file.writelines(lines)
file.close()

file = open('jorurnal.txt' , 'a')
file.write("my name is Gustavo\n")
file.close()

file = open('jorurnal.txt' , 'a')
file.write("But you can call me GUS\n")
file.close()

file = open('jorurnal.txt' , 'r')
x = file.read()
print(x)
file.close()