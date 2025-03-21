# def make_tea():  
#     print("Наливаю воду")
#     print("Кип'ячу воду")
#     print("Кладу чайний пакетик у чашку")
#     print("Заливаю кип'ятком")
#     print("Чай готовий!")

# make_tea()

# def calculate_average(math, english, science):  
#     return (math + english + science) / 3
# average = calculate_average(90, 85, 100)
# print(f"Середній бал: {average}")



# def calculate_remaining_money(total_money,spending):
#     return total_money - spending

# remaining = calculate_remaining_money(100, 40)  
# print(f"Залишилось: {remaining} гривень")


# remaining = calculate_remaining_money(80, 50)  
# print(f"Залишилось: {remaining} гривень")



# Список кольорів: ["червоний", "синій", "зелений"].
# Список предметів: ["сумка", "футболка", "шкарпетки"].
# Ти хочеш створити всі можливі комбінації, наприклад:

# "червона сумка"
# "червона футболка"

# def generate_combination(colors , items):
#     combination = []
#     for color in colors:
#         for item in items:
#             combination.append(f"всі комбігації: {color} {item}")
#         return combination
    
# color = [input("введіть всі кольори які хочете додати: ")]
# items = [input("введіть всі предмети які хочете додати: ")]
# all_combination = generate_combination(color,items)
# for combination in all_combination:
#     print(combination)

# def print_message(first_name,last_name):
#     full_name = f"{first_name} {last_name}"
#     print(full_name)
#     return full_name
# user_2 = input("write your name: ")
# user_1 = input("write your surname: ")

# result = print_message(user_1,user_2)
# print(f"your full name was saved as : {result}")



# user4 = input("write user2 name: ")
# user3 = input("write user2 surname: ")

# print_message(user3,user4)



# def draw_triangle():
#    for i in range(7):  
#      i = i + 1        
#      print('*' * i) 
    
# draw_triangle()



# def new_func():
#     name = 'radislav'   glboal
#     def user1():
#         name = 'mark'       enclosing
#         def user2():
#             name = 'bogdan'
#             print(name)     local
#         user2()
#         print(name)     f enclosing
#     user1()
#     print(name)

# new_func()     шукає в legb

# def order_pizza(size, topping="пепероні", crust="тонке"):
#     print(f"Замовлена піца: Розмір: {size}, Начинка: {topping}, Тісто: {crust}")
# order_pizza(size="велика", topping="гриби", crust="глибоке")   #Всі аргументи вказані явно
# order_pizza(size="середня")   #Використовуємо значення за замовчуванням для topping і crust



# def create_account(username, password, email="not@set.com"):
#     print(f"Створено акаунт: {username}, Email: {email}")
# create_account("user123", "password456", email="user@example.com")
# create_account("user456", "password789")

#дз
# subscribers_list_news = list()
# subscribers_list_what_new = list()
# subscribers_list_ads = list()

# def subscribe(email, is_news = True, is_new = True, is_ads = True):
#     global subscribers_list_news, subscribers_list_what_new, subscribers_list_ads
#     if(is_news):
#         subscribers_list_news.append(email)
#     if(is_new):
#         subscribers_list_what_new.append(email)
#     if(is_ads):
#         subscribers_list_ads.append(email)


# def print_subscribers(subscribers_list, list_name) :
#     delimiter = '---------------------------'
#     print('На розсилку {} підписалися {} користувачі'.format(list_name, len(list_name)))
#     for user in subscribers_list:
#         print(user)
#         print(delimiter)
#         print()
        
# subscribe('ivanov@gmail.com')
# subscribe('petrov@gmail.com', True, False, False)
# subscribe('ivanova@gmail.com', is_ads = False)

# print_subscribers(subscribers_list_news, '"Новини"')
# print_subscribers(subscribers_list_what_new, '"Що нового ?"')
# print_subscribers(subscribers_list_ads, '"Рекламні пропозиції"')


import requests

API_KEY = "d469c02f080f4fa99337d62c14522fc7"  # Ваш API ключ від OpenWeatherMap
BASE_URL = "https://api.weatherbit.io/v2.0/current"

def get_weather(city):
    """Отримує погодні умови для міста через OpenWeatherMap API."""
    try:
        # Параметри запиту
        params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "en"}
        
        # Запит до API
        response = requests.get(BASE_URL, params=params)
        
        # Перевіряємо статус запиту
        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"]  # Опис погоди
            temperature = data["main"]["temp"]  # Температура
            return f"{description.capitalize()}, {temperature}°C"
        else:
            return "Неможливо отримати погоду"
    except Exception as e:
        print(f"Помилка при отриманні погодних умов: {e}")
        return "Помилка погоди"

def show_flights(flights):
    """Виводить усі рейси."""
    if not flights:
        print("Список рейсів порожній.")                                                                                                                                                                                                                
        return
    print("\nСписок рейсів:")
    for flight in flights:
        print(f"{flight['номер']} | {flight['місто']} | {flight['час']} | {flight['статус']} {flight['погода']}")
    print()

def add_flight(flights):
    номер = input("Введіть номер рейсу: ")
    місто = input("Введіть місто призначення: ")
    час = input("Введіть час вильоту (HH:MM): ")
    статус = input("Введіть статус рейсу (Вчасно/Затримано/Скасовано): ")
    погода = get_weather(місто)
    flights.append({"номер": номер, "місто": місто, "час": час, "статус": статус,"погода":погода})
    print("Рейс додано успішно.\n")

def delete_flight(flights):
    """Видаляє рейс за номером."""
    номер = input("Введіть номер рейсу, який потрібно видалити: ")
    for flight in flights:
        if flight["номер"] == номер:
            flights.remove(flight)
            print("Рейс видалено.\n")
            return
    print("Рейс із таким номером не знайдено.\n")

def search_flights_by_city(flights):
    """Шукає рейси за містом."""
    місто = input("Введіть місто для пошуку: ")
    results = [flight for flight in flights if flight["місто"].lower() == місто.lower()]
    if results:
        print("\nЗнайдені рейси:")
        show_flights(results)
    else:
        print("Рейсів до цього міста не знайдено.\n")

def update_flight_status(flights):
    """Оновлює статус рейсу."""
    номер = input("Введіть номер рейсу для оновлення статусу: ")
    for flight in flights:
        if flight["номер"] == номер:
            новий_статус = input("Введіть новий статус (Вчасно/Затримано/Скасовано): ")
            flight["статус"] = новий_статус
            print("Статус оновлено.\n")
            return
    print("Рейс із таким номером не знайдено.\n")

def update_weather(flights):
    """Оновлює погодні умови для всіх рейсів."""
    for flight in flights:
        flight["погода"] = get_weather(flight["місто"])
    print("Погода оновлена для всіх рейсів.\n")


def main():
    flights = []
    print("=== Меню ===")
    options = ["Показати всі рейси", "Додати рейс", "Видалити рейс", "Пошук рейсів за містом", "Оновити статус рейсу","оновити погодні умови", "Вихід"]
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    while True:
        choice = int(input("Оберіть дію (1-6): "))
        if choice == 1:
            show_flights(flights)
        elif choice == 2:
            add_flight(flights)
        elif choice == 3:
            delete_flight(flights)
        elif choice == 4:
            search_flights_by_city(flights)
        elif choice == 5:
            update_flight_status(flights)
        elif choice == 6:
            update_weather(flights)
        elif choice == 7:
            print("Вы вышли из програмы.")
            break
        else:
            print("Неправильный выбор.")

main()