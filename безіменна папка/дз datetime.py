# from datetime import datetime

# now = datetime.now()
# date_str = input("Введіть дату (YYYY-MM-DD): ")

# # Перетворення рядка у datetime-об'єкт
# saved_date = datetime.strptime(date_str, "%Y-%m-%d")

# # Обчислення різниці між датами
# days_left = (saved_date - now).days

# print(f"До введеної дати залишилося {days_left} днів.")

# ---------------------------------------------------------

# from datetime import datetime
# import pytz

# from_zone = input("Введіть вихідну часову зону: ")
# to_zone = input("Введіть цільову часову зону: ")

# time_str = input("Введіть час (HH:MM): ")
# hours, minutes = map(int, time_str.split(":"))

# now = datetime.now()
# local_time = datetime(now.year, now.month, now.day, hours, minutes, tzinfo=pytz.timezone(from_zone))
# converted_time = local_time.astimezone(pytz.timezone(to_zone))

# print("Час у", to_zone, ":", converted_time.strftime("%H:%M"))

# ---------------------------------------------------------

# numbers = [1 , 3 , 5 ,6 , 3, 5 , 6, 7 , 90 , 7, 590 , 60 , 60]
# if all(num > 0 for num in numbers):
#     numbers = sorted(numbers)
#     print(numbers)
# else:
#     print("eror")

# ---------------------------------------------------------

# import math 
# def get_sqrt():
#     num = int(input("введіть число для знаходженя квадратного кореня: "))
#     print(math.sqrt(num))


# def get_floor():
#     num1 = float(input("введіть число для округлення вниз: "))
#     print(math.floor(num1))


# def get_ceil():
#     num2 = float(input("введіть число для округлення вгору: "))
#     print(math.ceil(num2))

# def get_log():
#     num3 = int(input("введіть число для логорифму: "))
#     print(math.log(num3))

# def main():
#     while True:
#         print("\n===МЕНЮ КАЛЬКУЛЯТОРА===")
#         print("1 - знайти квадрат з числа")
#         print("2 - логорифм")
#         print("3 - округлення вниз")
#         print("4 - округлення вверх")
#         choice = input("виберіть функцію калькуятора: ")
#         if choice == '1':
#             get_sqrt()
#         elif choice == '2':
#             get_log()
#         elif choice == '3':
#             get_floor()
#         elif choice == '4':
#             get_ceil()
#         else:
#             print("помилка")
    
# main()