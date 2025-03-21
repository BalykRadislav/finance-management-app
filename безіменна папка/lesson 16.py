# Рекурсія 
# функція яка виконується сама в собі

#------------------------------------------------------

# def factorial(n):
#     if n == 1:  # Базовий випадок
#         return 1
#     else:
#         return n * factorial(n - 1)  # Рекурсивний крок

# print(factorial(5))

#------------------------------------------------------



# def fibonachi(n):
#     if n == 0 :
#         return 0
#     if n == 1:
#         return 1
#     return fibonachi(n-1)+fibonachi(n-2)
    

# print(fibonachi(3))

#------------------------------------------------------

# def countdown_to_open(n):
#     if n == 0:  # Якщо дійшли до 0, відкриваємо коробку
#         print("Бум! Коробку відкрито!")
#         return
#     print(f"{n}...")  # Виводимо поточне число
#     countdown_to_open(n - 1)  # Зменшуємо число і рахуємо далі

# countdown_to_open(5)  # Виведе 5, 4, 3, 2, 1, Бум!



#----------------------------------------------------

# def count_steps(steps):
#     if steps == 0:
#         print("я вдома")
#         return
#     if steps == 3:
#         print("ябіля сусіда ")
        
#     print(f"залишилося {steps} кроків ")
#     count_steps (steps-1)

# count_steps(50)



#----------------------------------------------------

# def open_boxes(box):
#     if not box:  # Якщо коробок більше немає
#         print("Не знайшов подарунка!")
#         return
#     if box[0] == "подарунок":  # Якщо перша коробка — це подарунок
#         print("Знайшов подарунок!")
#         return
#     print("Відкриваю коробку...")
#     open_boxes(box[1:])  # Відкриваємо наступну коробку

# open_boxes(["коробка1", "коробка2", "коробка3", "подарунок"])
 
#----------------------------------------------------


# def replace_word_in_boxes(boxes , old_word, new_word):
#     if not boxes:
#         return[]
#     return[boxes[0].replace(old_word, new_word)] + replace_word_in_boxes(boxes[1:], old_word, new_word)
# boxes = ["коробка1", "коробка2", "коробка3"]
# new_boxes = replace_word_in_boxes(boxes, "коробка", "пакет") 
# print(new_boxes)


#----------------------------------------------------

# def modify_nested_boxes(boxes):
#     if not boxes:  # Якщо коробки закінчилися
#         return []
#     if isinstance(boxes[0], list):  # Якщо елемент є списком, обробляємо його
#         return [modify_nested_boxes(boxes[0])] + modify_nested_boxes(boxes[1:])
#     return [boxes[0] + " модифікована"] + modify_nested_boxes(boxes[1:])  # Модифікуємо коробку і рекурсивно

# # Список коробок з вкладеними коробками
# nested_boxes = ["коробка1", ["коробка2", "коробка3"], "коробка4"]
# new_boxes = modify_nested_boxes(nested_boxes)  # Модифікуємо всі коробки
# print(new_boxes)

#----------------------------------------------------


