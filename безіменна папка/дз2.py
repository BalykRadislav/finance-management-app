# def число_В_КВАДРАТІ():
#     number = int(input("введіть число: "))
#     square = (lambda x: x **2)(number)
#     print(f"число в квадраті : {square}")
    
# число_В_КВАДРАТІ()
#------------------------------------------------------

# numbers = [1 , 2 , 3 , 4 , 5]

# result = list(map(lambda x : x*2 , numbers))

# print(result)

# map(function, iterable)

#------------------------------------------------------

# celsious = [0 , 20 , 30 , 40]
# result = list(map(lambda x : x*9/5+32 , celsious))
# print(result)

#------------------------------------------------------

# words = ["hello" , "word" , "python" , "rocks"]
# result =  list(map(lambda x: x.upper(), words ))
# print(result)

#------------------------------------------------------

# numbers = [1 , 2 ,3 ,4, 5]
# result = list(map(lambda x: x**2 , numbers))
# print(result)

#------------------------------------------------------

# names = ["Kiril", "Artem" , "Radislav" , "Dan"]
# result = list(map(lambda x: len(x) , names ))
# print(result) 

#------------------------------------------------------

# names = ["RADISLAV" , "ANTON"]
# result = list(map(lambda x: x.lower(), names))



# print(result)
#------------------------------------------------------

# FILTER
# filter(function, iterable)



# NUMBER = [ 1 , 2, 3, 4, 5 ,6 ,7 ,8 ,9]
# result = list(filter(lambda x: x% 2 == 0 , NUMBER))

# print(result)

#------------------------------------------------------

# words = ["apple", "banana", "avocado", "cherry", "apricot"]
# result = list(filter(lambda x: x.startswith("a") , words))

# print(result)

#------------------------------------------------------

# numbers = [1, 3, 5, 7, 9]
# result = list(filter(lambda x: x > 5  , numbers))
# print(result)

#------------------------------------------------------


# words = ["cat", "dog", "elephant", "rat", "fox"]
# result = list(filter(lambda x: len(x) > 4 , words))
# print(result)

#------------------------------------------------------

# numbers = [-5, -3, 0, 2, 8, -1]
# result = list(filter(lambda x: x>0 , numbers))
# print(result)

#------------------------------------------------------

# names = ["John", "Paul", "Ringo", "George", "Anna"]
# result = list(filter(lambda x: len(x) ==4 , names))
# print(result)

#------------------------------------------------------
# Вибираємо лише парні числа.
# Збільшуємо кожне парне число на 10.
# Виводимо результат у циклі.




# while True:
#     try:
#         user_input = input("введіть числа через кому : ")
#         numbers = list(map(int,  user_input.split(" , ")))
#         break
#     except ValueError:
#         print("Помилка! Введіть тільки числа через кому.")
# even_numbers = list(filter(lambda x: x% 2 == 0 , numbers))
# double_numbers = list(map(lambda x: x+ 10 , even_numbers))
# print('result: ')
# for num in double_numbers:
#     print(num)

#------------------------------------------------------

# Залишає товари дорожчі за 100.
# Розраховує знижку 20% для всіх таких товарів.
# Виводить результати у вигляді таблиці.


# while True:
#     try:
#         user_input = input("введіть ціни товарів  через кому : ")
#         price= list(map(int,  user_input.split(" , ")))
#         break
#     except ValueError:
#         print("Помилка! Введіть тільки ціни  через кому.")
# expensive_items= list(filter(lambda x: x > 100 , price))
# discounted_prices= list(map(lambda x: x * 0.8 , expensive_items))

# print('\nТаблиця Знижок:')
# print(f"{'Ціна до знижки':<15}{'Ціна зі знижкою':<15}")
# print("-" * 30)
# for original, discounted in zip(expensive_items, discounted_prices):
#     print(f"{original:<15}{discounted:<15.2f}")


#------------------------------------------------------

# names = ["John", "Paul", "Ringo", "George", "John", "Paul", "Anna"]
# unique_names = list(filter(lambda x:  names.count(x) == 1 , names))
# name_with_surname = list(map(lambda x: f"{x} Smith" , unique_names ))
# print("formated names:")
# for name in name_with_surname:
#     print(name)

#------------------------------------------------------

# numbers = [10 , 12 , 5 ,6 , 7 , 8 , 15 ,18 , 10]
# formated = list(filter(lambda x: x > 10 , numbers))
# ten = list(map(lambda x: x**2 , formated))
# print(numbers)
# print("result:")
# for num in ten:
#     print(num)

#------------------------------------------------------

# Перевірка на наявність літер у словах та видалення літер "a" або "e"

words = ["apple", "banana", "cherry", "grape", "pear"]
filtered_words = list(filter(lambda x: 'a' in x or 'e' in x, words))
deleted_letters = list(map(lambda x: x.replace("a" , "").replace("e" , ""), filtered_words))
print(words)
print("result:")
for nam in deleted_letters:
    print(nam)

    #------------------------------------------------------

    