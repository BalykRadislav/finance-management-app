
file_path = "counter.txt"


try:
    with open(file_path, "r") as file:
        counter = int(file.read())  
except FileNotFoundError:
    counter = 0  


counter += 1

with open(file_path, "w") as file:
    file.write(str(counter))


print(f"Кількість запусків програми: {counter}")
