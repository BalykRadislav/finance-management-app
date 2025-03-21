# синтаксис all(iterable)


# смарагди = []
# if all(смарагди):
#     print("Дракон відкрив скарб")
# else:
#     print("Ой , закрито")

#--------------------------------------

# numbers = [1 , 2 , 3, 4 , 45]

# all_positive = all(number > 0 for number in numbers)
# print(all_positive)

# ---------------------------------------
# words = []
# all_none_empty = all(words)
# print(all_none_empty)

#_-------------__-----_--__-__-_-__-__--
# синтаксис any(iterable)

# sky = [False , False , True , False , False]
# if any(sky):
#     print("yf")
# else:
#     print("e")

# ----------------__-_--_-_--_-_-


# sky = [0 , 0 , 0  ,0]
# if any(sky):
#     print("yf")
# else:
#     print("e")

# -------------_--_--_--_-__

# прогноз = ["☀️" , "☀️" , "☀️" , "🌧️"]
# if any(day == "🌧️" for day in прогноз):
#     print("бери парасольку ☂️")
# else:
#     print("дощу не буде ☀️")

#--____--------_--_-_------_-

# numbers = [-1 , 0 , 2 , 15 , 20 , 0 ,-11 , -1]
# positive_num = any(num > 0 for num in numbers)
# print(positive_num)

# ------_--_-__-_____-_--_--_-_-_--_-_--_

# words = ["apple" , "banana" , "Cherry" , "Qiwi"]
# x = any(word[0].isupper() for word in words)
# print(x)
# ------_--_-__-_____-_--_--_-_-_--_-_--_

# inputs = [0 , "" , None , False , "ValidInput"]
# x = any(inputs)
# print(x)
# ------_--_-__-_____-_--_--_-_-_--_-_--_
# list1 = [1 , 3 ,5]
# list2 = [2 , 4 , 6]
# list3 = [0 , 2, 3]
# x = any(3 in lst for lst in [list1 , list2 ,list3])
# print(x)

# ------_--_-__-_____-_--_--_-_-_--_-_--_
#  синтаксис sorted(terable , key=None , reverse=False)


# num = []

# while True:
#     y = input("Введіть число: ")
#     if y == "":
#         break
#     num.append(int(y))
# x = sorted(num)
# print(x)

# ------_--_-__-_____-_--_--_-_-_--_-_--_

# tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
# sorted_tuples = sorted(tuples, key=lambda x: x[1])
# print(sorted_tuples)

# ------_--_-__-_____-_--_--_-_-_--_-_--_

# words = ["apple" , "banana" , "Cherry" , "Qiwi"]
# x = sorted(words , reverse=True)
# print(x)

# ------_--_-__-_____-_--_--_-_-_--_-_--_

numbers = [1 , 2 , 4 ,5 , 6 , 7 , 0 , 3]
a = sorted(numbers)
x = all(num >= 0 for num in numbers)
if x == True:
    print(a)

