# try:
#     milk = int(input('quantity of milk: '))
#     if milk == 0:
#         raise ValueError("we run out of milk")
#     print("cat is drinking milk happily")
# except ValueError as e:
#     print("eror ," , e)

# -------------------------------------

# try:
#     passengers = ["alice" , "bob" , "kate"]
#     print(passengers[3])
# except IndexError:
#     print("індекс поза межами списку")

# -------------------------------------

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("не можливо поділити на нуль , калькулятор вибухнув💣💥")

# -------------------------------------

# try:
#     backpack = {
#         "apple" : 2,
#         "notebook" : 1 ,
#     }
#     print(backpack["key"])

# except KeyError:
#     print("такого ключа немає")

# -------------------------------------

# try:
#     num = 5
#     text = "hello🦅"
#     result = num + text
# except TypeError:
#     print("неможлива команда❤️")

# -------------------------------------

# try:
#     age = int(input("enter your age: "))
#     if age < 0:
#         raise ValueError("you mustnt swing⛔️")
#     print("swinging")
# except ValueError as e:
#     print("eror," , e)

# -------------------------------------

# try:
#     milk = int(input('quantity of milk: '))
#     if milk == 0:
#         raise ValueError("we run out of milk")
#     print("cat is drinking milk happily")
# except ValueError as e:
#     print("eror ," , e)
# finally:
#     print("cat is purring and it is gonna sleep")

# -------------------------------------

# try:
#     with open("goiteens.txt", 'r') as file:
#         date = file.read()
        
# except FileNotFoundError:
#     print("Помилка: Файл 'goiteens.txt' не знайдено.")
# except EOFError:
#     print("проблеми з доступом до файлу")
# else:
#     print("все гаразд . виконуєм обробку данних .....")
#     print(date)
# finally:
#     print("операція завершена")

# -------------------------------------

# try:
#     number = int(input("enter a number: "))
# except ValueError:
#     print("ви ввели не число")
# else:
#     print(f"введене число :{number}")
#     result = number ** 2
#     print(f"квадрат числа :{result}")
# finally:
#     print("операція завершена")

# -------------------------------------

# try:
#     with open("goiteens.txt", 'r') as file:
#         data = file.read()
# except FileNotFoundError:
#     print("Помилка: Файл 'goiteens.txt' не знайдено.")
# except EOFError:
#     print("проблеми з доступом до файлу")
# else:
#     print("все гаразд . виконуєм обробку данних .....")
#     print(data)
#     words = data.split()
#     print(f"кількість слів в файлі: {len(words)}")
# finally:
#     print("операція завершена")

# -------------------------------------

# try:
#     connection = connect_to_database()
#     result = connection.execute_query("SELECT * FROM users")
# except DatabaseError as e:
#     print(f"Помилка бази даних: {e}")
# else:
#     print("Запит виконано успішно.")
#     for user in result:
#         print(f"Користувач: {user['name']}, Email: {user['email']}")
# finally:
#     connection.close()
#     print("З'єднання з базою даних закрито.")

# -------------------------------------

# class MyCustomError(Exception):
#     def __init__(self, message="Виникла помилка"):
#         self.message = message
#         super().__init__(self.message)

# try:
#     raise MyCustomError("Щось пішло не так!")
# except MyCustomError as e:
#     print(f"Обробка власного винятку: {e}")

# -------------------------------------

# class AgeError(Exception):
#     def init(self, age, message="Некоректний вік"):
#         self.age = age
#         self.message = f"{message}: {age}"
#         super().init(self.message)

# def check_age(age):
#     if age < 18:
#         raise AgeError(age, "Занадто молодий")
#     elif age > 100:
#         raise AgeError(age, "Занадто старий")
#     else:
#         print("Вік коректний")

# try:
#     check_age(int(input("Введіть вік: ")))
# except AgeError as e:
#     print(f"Оброблено: {e}")

# -------------------------------------

# class InsufficientFundsError(ValueError):
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         self.message = f"Недостатньо коштів: доступно {balance}, потрібно {amount}"
#         super().__init__(self.message)

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError(balance, amount)
#     else:
#         print("Операція успішна. Залишок:", balance - amount)

# try:
#     withdraw(140 , 100)
# except InsufficientFundsError as e:
#     print(f"Помилка: {e}")

# -------------------------------------

# class TransactionError(Exception):
#     pass

# class InsufficientFundsError(TransactionError):
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         super().__init__(f"Недостатньо коштів: доступно {balance}, потрібно {amount}")

# class UnauthorizedTransactionError(TransactionError):
#     def __init__(self, user):
#         self.user = user
#         super().__init__(f"Користувач {user} не має прав для виконання транзакції")

# def process_transaction(user, balance, amount):
#     if user != "admin":
#         raise UnauthorizedTransactionError(user)
#     if amount > balance:
#         raise InsufficientFundsError(balance, amount)
#     print("Транзакція успішна!")

# try:
#     process_transaction("admin", 100, 50)
# except TransactionError as e:
#     print(f"Помилка транзакції: {e}")

# -------------------------------------

class FileError(Exception):
    pass

class FileNotFoundError(FileError):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Файл '{filename}' не знайдено")

class FileReadError(FileError):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Не вдається прочитати файл '{filename}'")
def read_file(filename):
    if not filename.endswith('.txt'):
        raise FileReadError(filename)
    if filename == "goiteens.txt":
        raise FileNotFoundError(filename)
    print(f"Файл '{filename}' успішно прочитано")

try:
    read_file("goiteens.txt")
except FileError as e:
    print(f"Помилка роботи з файлом: {e}")