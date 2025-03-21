# Генератори - це спеціальні об'єкти, які використовуються для створення ітераторів.



# def скриня_монет ():
#     coin = 1
#     while True:
#         yield coin #видаємо менту
#         coin += 1 #збільшуємо кількість монет на 1

# box = скриня_монет()
# print(next(box))
# print(next(box))
# print(next(box))
# print(next(box))

# ---------------------------------------

# def нескінченні_числа():
#     n = 0 
#     while True:
#         yield n
#         n += 1

# numbers = нескінченні_числа()
# for _ in range(5):
#     print(next(numbers))

# ---------------------------------------

# def even_numbers(nums , max=None):
#     quantity = 0
#     for num in nums:
#         if num % 2 == 0:
#             yield num
#             quantity += 1
#             if max and quantity >= max:
#                 break
        

# even_with_limits  = even_numbers(range(100) , max=5)
# even = even_numbers(range(20))

# # print(next(even_with_limits))

# print(list(even))
# print(list(even_with_limits))


# random_numbers = [3 , 8 , 9 , 0 , 8 , 8 ,6 ,4 ,2 , -1 , -4]
# even_nums_randoms = even_numbers(random_numbers)
# print(list(even_nums_randoms))

# ---------------------------------------

# def magical_story():
#     yield "Одного разу"
#     yield "в країні..."
#     yield "За горами..."
#     yield "за Горами..."

# story = magical_story()
# print(next(story))
# print(next(story))
# print(next(story))
# print(next(story))

#----------------------------------------

# def some_yield ():
#     yield "begining of the adventure"


#     for i in range (3):
#         yield f"step {i+1} "
#     yield "The adventure is over"

# gam = some_yield()

# print(next(gam))
# print(next(gam))
# print(next(gam))
# print(next(gam))
# print(next(gam))


#----------------------------------------

# def діалог():
#     name = yield "Як тебе звати?"
#     yield f"Приємно познайомитися, {name}!"
#     age = yield "Скільки тобі років?"
#     yield f"О, {age} років – чудовий вік!"
    
# розмова = діалог()

# print(next(розмова))
# print((розмова.send("Radislav")))
# print(next(розмова))
# print((розмова.send("15")))

#----------------------------------------

# even = (num for num in range(10) if num % 2 == 0)
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))
# print(list(even))

# -----------------------------------------

# cubes = (num ** 3  for num in range(1 , 6))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))

# ------------------------------------------

# basket = ["the apple is red" , "the apple is green" , "banana" , "the apple is red" , "pear" , "red"]
# red_apples = (fruit for fruit in basket if "red" in fruit)

# print(next(red_apples))
# print(next(red_apples))

#-------------------------------------------

# def magical_story():
#     try:   
#         yield "Одного разу"
#         yield "в країні..." 
#         yield "За горами..."
#         yield "за Горами..."
#     except ValueError:
#         yield "something went wrong"
#     yield "story continue"
# story = magical_story()
# print(next(story))
# print(next(story))
# story.throw(ValueError)
# print(next(story))

#---------------------------------------------

# import itertools

# def генератор_паролів(довжина):
#     символи = "abcdefghijklmnopqrstuvwxyz0123456789"
#     for комбінація in itertools.product(символи, repeat=довжина):
#         yield "".join(комбінація)

# # Використання генератора для паролів довжиною 4
# паролі = генератор_паролів(5)

# # Виведемо перші 10 паролів для перевірки
# for _ in range(10): 
#     print(next(паролі))

#-----------------------------------------------

# numbers = [ 1 , 4, 5, 7, 8, 10 , -3 , 5 ,7 , 0 , 20 , 32 ,33]

# square_of_even_numbers = (x ** 2 for x in numbers if x % 2 ==0)
# print(numbers)
# for square in square_of_even_numbers:
#     print(square)

#------------------------------------------------

# numbers = [ 1 , 4, 5, 7, 8, 10 , -3 , 5 ,7 , 0 , 20 , 32 ,33]
# sum_of_even_numbers = sum(x + x for x in numbers if x % 2 ==0)
# print(sum_of_even_numbers)
# ----=-------------=---------------------=----------------
# import random

# def random_numbers(n, min, max):
#     for _ in range(n):
#         yield random.randint(min, max)

# for number in random_numbers(5, 10, 20):
#     print(number)
# -------------------------------------
# def even_numbers():
#     n = 0
#     while True:
#         yield n
#         n += 2
    
# gen = even_numbers()
# for i in range(5):
#     print(next(gen))

# -------------------------------------

# def simple_numbers():
#     n = 0
#     while True:
#         yield n
#         n += 1  # Правильне збільшення n

# gen = simple_numbers()

# for num in gen:  # Нескінченний цикл
#     print(num)

#---------------------------------------

# import itertools

# def password_generator(length):
#     chars = "abcdefghijklmnopqrstuvwxyz0123456789"
#     for combo in itertools.product(chars, repeat=length):
#         yield "".join(combo)

# # Використання генератора для створення паролів довжиною 4 символи
# gen = password_generator(4)

# # Виведемо перші 10 паролів
# for _ in range(10):
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))

