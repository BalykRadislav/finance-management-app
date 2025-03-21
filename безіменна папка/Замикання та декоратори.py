# Замикання
#------------------------------------------------------

# def make_storage(item):
#     def storage():
#         return f"у чарівній коморі лежить : {item}"
#     return storage

# apple_storage = make_storage("aplle")
# strawberry_storage = make_storage("strawberry")
# book_storage = make_storage("book")

# print(apple_storage())
# print(strawberry_storage())
# print(book_storage())
        

#------------------------------------------------------
# def personal_notebook(name):
#     notes = []

#     def add_note(note):
#         notes.append(note)
#         return f"{name} записав {note}"
    
#     def show_notes():
#         return f"{name}'s  нотатки : {notes}"
    
#     return add_note, show_notes

# alice_notebook, alice_notes = personal_notebook("Аліса")
# bob_notebook, bob_notes = personal_notebook("Боб")


# print(alice_notebook("Я люблю читати"))  # Аліса записав: Я люблю читати
# print(alice_notebook("Моя улюблена книга — Гаррі Поттер"))

# print(bob_notebook("Я граю в футбол"))  

# # Переглядаємо нотатки
# print(alice_notes())  
# print(bob_notes())

#------------------------------------------------------

# def count_from(start):
#     def next():
#         nonlocal start
#         start +=1

#         return start
#     return next

# counter = count_from(0)

# print(counter())
# print(counter())
# print(counter())


#------------------------------------------------------

# def greeting(name):
#     def say_hello():
#         print(f"hello {name}!")

#     return say_hello


# name_R = greeting('Radislav')

# name_R()


#------------------------------------------------------

# def count_from(start):
#     def next():
#         nonlocal start
#         start +=1

#         return start
#     return next

# counter = count_from(0)

# print(counter())
# print(counter())
# print(counter())


# def створити_сейф(пароль):
#     секретний_код = пароль
    
#     def перевірити_пароль(): 
#         введений_код = input("введіть пароль: ")
#         if введений_код == секретний_код:
#            return "пароль вірний сейф відкритий"
#         else: 
#             return "пароль невірний сейф закритий"
#     return перевірити_пароль 
    
# мій_сейф = створити_сейф("1001")
# print(мій_сейф())



#------------------------------------------------------

# def create_bonus_system():
#     bonus = 0 


#     def add_bonus(quantity):
#         nonlocal bonus 
#         bonus += quantity
#         return bonus
#     return add_bonus

# my_bonus = create_bonus_system()
# my_bonus2 = create_bonus_system()

# print("user 1")
# print(my_bonus(10)) 
# print(my_bonus(10)) 
# print(my_bonus(10)) 
# print("user 2")
# print(my_bonus2(12)) 
# print(my_bonus2(12)) 
# print(my_bonus2(12)) 


#------------------------------------------------------

# def filtre_age(minimalage):
#     def age_checker():
#         age = int(input("enter your age: "))
#         if age == minimalage:
#             return f"your {age} is enough to watch yhe film"
#         else:
#             return f"go and eat some candies"
#     return age_checker

# filter_cinema = filtre_age(18)
# filter_Porn = filtre_age(21)
# filtre_barbie = filtre_age(3)

# print("age cinema checker")
# print(filter_cinema())
# print("age cinema checker for porn")
# print(filter_Porn())
# print("age cinema checker for barbie")
# print(filtre_barbie())


# while True:
#     print("age checker program")
#     print("enter '1' for cinema(minimal age = 18)")
#     print("enter '2'  to watch potn (minimal age = 21)")
#     print("enter '3' to watch barbie (minimal age = 3)")
#     print("enter 4 to exit")
#     choice = input("enter your choice: ")
#     if choice == '1':
#         print(filter_cinema())
#     elif choice == '2':
#         print(filter_Porn())
#     elif choice == '4':
#         print(filtre_barbie())
#     elif choice == '4':
#         break
#     else:
#         print("wrong choice")



#------------------------------------------------------
# def box():
#     def toy():
#         print("this is a toy")
#     toy()
# box()

#------------------------------------------------------
# def my_decorator(func):
#     def obgortka():
#         print("ready")
#         func()
#         print("done")
#     return obgortka 

# @my_decorator

# def my_function():
#     print("doing task")

# # my_decorator(my_function)()
# my_function()
#------------------------------------------------------

# def simple_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper
# @simple_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
    

#------------------------------------------------------

# def log_decorator(func):
#     def wrapper():
#         print(f"Calling function {func.__name__}")
#         func()
#         print(f"Function {func.__name__} finished")
#     return wrapper

# @log_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# #------------------------------------------------------

# def auth_decorator(func):
#     def wrapper():
#         user = input("enter your name: ")
#         if user == "admin":
#             func() 
#         else:
#             print("Access denied")
#     return wrapper
# @auth_decorator

# def secret_function():
#     print("Hello admin")

# secret_function()
  

#------------------------------------------------------
# def auth_decorator(func):
#     def wrapper():
#         user = input("enter your name: ")
#         password = input("enter your password: ")

#         if user == "admin" and password == "1456":
#             func() 
#         else:
#             print("Access denied")
#     return wrapper
# @auth_decorator

# def secret_function():
#     print("Hello admin")

# secret_function()

#------------------------------------------------------
# def show_data(**kwargs):
#     print("Дані:", kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# show_data(name="Богдан", age=33, city="Тернопіль")

# def add_nums(*args):
#     result = 0
#     for num in args:
#         result += num
#     print(f"Результат додавання: {result}")

# add_nums(10, -78, 30, 4, -89)

# add_nums(1, 2, 3, -4, 5, -12, 7, -8, -5, 10)
#------------------------------------------------------

# def greeting(*args , **kwargs):
#     for name in args:
#         print(f"Hello {name}!")

#     for key, value in kwargs.items():
#         print(f"{key.capitalize()}:  {value}")

# greeting("John", "Anna", age=25, city="Kyiv")
    
#------------------------------------------------------

# def hello(*args):
#     for name in args:
#         print(f"Hello {name}!")

# hello("alice", "bob", "john")
#------------------------------------------------------




#------------------------------------------------------


#------------------------------------------------------