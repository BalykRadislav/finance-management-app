# try:
#     passengers = ["alice" , "bob" , "kate"]
#     print(passengers[3])
# except IndexError:
#     print("індекс поза межами списку")

# # -------------------------------------

# def devide():
#     try:
#         result = int(input("enter a number: ")) / int(input("enter a number: "))
#         print(result)
#     except ZeroDivisionError:
#         print("не можливо поділити на нуль , калькулятор вибухнув💣💥")

# while True:
#     devide()
#     if input("continue? yes/no: ") == "no":
#         break
# print("goodbye")

# # -------------------------------------

# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             print(file.read())
#     except FileNotFoundError:
#         print(f"Помилка: Файл '{filename}' не знайдено.")

# read_file("example.txt")

# -------------------------------------

import json

def load_config(filename):
    default_config = {"setting1": "value1", "setting2": "value2"}
    try:
        with open(filename, "r") as file:
            config = json.load(file)
            print("Налаштування завантажено:", config)
    except FileNotFoundError:
        print("Файл конфігурації не знайдено. Створюємо новий...")
        with open(filename, "w") as file:
            json.dump(default_config, file)
        config = default_config
    finally:
        print("Операція завершена.")
    return config

config = load_config("config.json")





            
























# nums = []
# def numbers():
#     try:
#         while True:
#             num = int(input("enter a number or 'stop' to stop: "))
#             if num.lower() == "stop":
#                 break
#             nums.append(int(num))
#     except ValueError:
#         print("you must enter a number")
#     finally:
#         print(f"введені числа: {nums}")

# numbers()



