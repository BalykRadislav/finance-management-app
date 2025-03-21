
name = input("Введіть ваше ім'я: ")

# Записуємо ім'я в файл
with open("name.txt", "w") as file:
    file.write(name)

# Читаємо ім'я з файлу
with open("name.txt", "r") as file:
    saved_name = file.read()

print(f"Привіт, {saved_name}!")
