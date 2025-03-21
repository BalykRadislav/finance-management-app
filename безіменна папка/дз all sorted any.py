# numbers = [1 , 2 , 4 ,5 , 6 , 7 , 0 , 10]
# a = sorted(numbers)
# x = all(num >= 0 for num in numbers)
# if x == True:
#     print(a)
# else:
#     print("не всі числа більше 0")

# def голосні(s):
#     vowels = "aeiouAEIOU"
#     return any(char in vowels for char in s)

# user_INPUT = input("введіть рядок для перевірки на голосні букви : ")
# if голосні(user_INPUT):
#     print(user_INPUT)
#     print("цей рядок містить голосні")
# else:
#     print(user_INPUT)
#     print("цей рядок не містить голосні")

# people = [
#     {"name": "Олександр", "age": 25},
#     {"name": "Андрій", "age": 30},
#     {"name": "Олександр", "age": 20},
#     {"name": "Марія", "age": 22},
#     {"name": "Андрій", "age": 25},
# ]

# sorted_people = sorted(people , key = lambda x: (x["name"] , x["age"]))

# print("Сортування за ім'ям, потім за віком (зростання):")
# for person in sorted_people:
#     print(person)

# sorted_people = sorted(people , key = lambda x: (x["name"] , x["age"]) , reverse=True)
# print("\nСортування за ім'ям, потім за віком (спадання):")
# for person in sorted_people:
#     print(person)
