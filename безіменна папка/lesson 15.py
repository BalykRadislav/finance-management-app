# КЛАСИ
# __init__ - допомагає створити "іграшку"
# self - працює з кожною іграшкою
# class Toy:
#     # це шаблон для іграшки
#     def __init__(self, color, size, toy_type):
#         self.color = color
#         self.size = size
#         self.toy_type = toy_type
#     def describe(self):
#         print(f"це іграшка - {self.toy_type}. вона {self.color}. має розмір {self.size}")

# toy1 = Toy("червона", "велика", "вантажівка")
# toy2 = Toy("синя", "малий", "авто")

# toy1.describe()
# toy2.describe()
#------------------------------------------------------

# # Створюємо іграшки як словники
# toy1 = {
#     "color": "червона",
#     "size": "велика",
#     "toy_type": "лялька"
# }

# toy2 = {
#     "color": "синя",
#     "size": "середня",
#     "toy_type": "машинка"
# }

# # Функція для опису іграшки
# def describe_toy(toy):
#     print(f"Ця іграшка - {toy['toy_type']}. Вона {toy['color']} і має розмір {toy['size']}.")

# # Описуємо іграшки
# describe_toy(toy1)
# describe_toy(toy2)
#------------------------------------------------------

# class Robot:
#     def __init__(self, name, power, secret_code):
#         self.name = name
#         self.power = power
#         self.__secret_code = secret_code

#     def reveal_secret(self):
#         return f"Секретний код робота {self.name}: {self.__secret_code}"

# robot1 = Robot("Робік", 100, "12345")

# print(robot1.reveal_secret())  # Ми знаємо код
# # print(robot1.__secret_code)  # Помилка! Секрет схований.


#------------------------------------------------------

# class book:
#     # це шаблон для іграшки
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def describe(self):
#         print(f"це книга {self.title} . її автор -{self.author} , і має кількість сторінок - {self.pages}")
#     def is_long(self):
#         if self.pages > 300:
#             print(f"Книга '{self.title}' довга.")
#         else:
#             print(f"Книга '{self.title}' коротка.")


# # Створюємо книги
# book1 = book("Гаррі Поттер", "Дж. К. Ролінг", 350)
# book2 = book("Колобок", "Невідомий", 15)

# # Використовуємо методи
# book1.describe()
# book1.is_long()

# book2.describe()
# book2.is_long()


#------------------------------------------------------
# class student:
#     # це шаблон для іграшки
#     def __init__(self, name , age , form):
#         self.name =name
#         self.age = age
#         self.form = form
#     def introduce(self):
#         print(f"привіт! мене звати {self.name}. мені {self.age} років . і я навчаюсь в {self.form} класі")
        
#     def highschool(self):
#         if self.age >= 14:
#             print(f"студент більше 14 років - вже в старшій школі")
#         else:
#             print(f"студенту немає 14. в молодшій школі")


# # Створюємо книги
# student1 = student("Jack" , 14 , 9)
# student2 = student("John" , 13 , 8)

# # Використовуємо методи
# student1.introduce()
# student1.highschool()

# student2.introduce()
# student2.highschool()

#------------------------------------------------------
# class Animal:
#     # це шаблон для іграшки
#     def __init__(self, name , type , voice):
#         self.name = name
#         self.type = type
#         self.voice = voice
#     def make_sound(self):
#         print(f"{self.name} {self.type} , каже -{self.voice}")
    
#     def describe(self):
#         print(f"це {self.type} , на імя {self.name} ")


# # Створюємо книги
# animal1 = Animal("левчик", "лев", "рррррррр")
# animal2 = Animal("пухнастик", "кролик", "фффрррррр")

# animal1.make_sound()
# animal1.describe()

# animal2.make_sound()
# animal2.describe()
#------------------------------------------------------
# class Facebook:
#     def __init__(self, name , age , subs):
#         self.name = name
#         self.age = age
#         self.subs = subs
# def subs(self):
#     if subs >= 10000:
#         print("користувач популярний")
#     else :
#         print("користувач непопулярний")

# def describe(self):
#     print(f"привіт! мій нік на facebook -{self.name} , мені {self.age} і в мене {self.subs} підписників")

# user1 = Facebook("fantaser4ik", 23 , 10245)
# user2 = Facebook("lazach", 16 , 1023)

# user1.describe()
# user1.subs()


#------------------------------------------------------

class Product:
    """Клас для опису товару"""
    def __init__(self, name, price, stock):
        self.name = name          # Назва товару
        self.price = price        # Ціна товару
        self.stock = stock        # Кількість на складі

    def describe(self):
        return [self.name, self.price, self.stock]
    def list_products(self):
        if not self.products:
            print(f"У категорії '{self.name}' ще немає товарів.")
        else:
            # Форматування заголовків таблиці
            print(f"\nТовари у категорії '{self.name}':")
            print(f"{'Назва товару':<20} {'Ціна (грн)':<15} {'Кількість на складі'}")
            print("-" * 50)
            for product in self.products:
                name, price, stock = product.describe()
                print(f"{name:<20} {price:<15}  {stock}")
            print("-" * 50)
                
class Category:
    """Клас для опису категорії товарів"""
    def __init__(self, name):
        self.name = name  # Назва категорії
        self.products = []  # Список товарів у категорії

    def add_product(self, product):
        self.products.append(product)
        print(f"Товар '{product.name}' додано до категорії '{self.name}'.")

class Store:
    """Клас для управління магазином"""
    def __init__(self, name):
        self.name = name  # Назва магазину
        self.categories = []  # Список категорій

    def add_category(self, category):
        self.categories.append(category)
        print(f"Категорію '{category.name}' додано до магазину '{self.name}'.")
    def list_categories(self):
        if not self.categories:
            print("У магазині ще немає категорій.")
        else:
            # Форматування заголовків таблиці
            print(f"\nКатегорії магазину '{self.name}':")
            print(f"{'№':<5} {'Назва категорії'}")
            print("-" * 30)
            for i, category in enumerate(self.categories, start=1):
                print(f"{i:<5} {category.name}")
            print("-" * 30)

# Основна логіка взаємодії
def main():
    print("Вітаємо у програмі управління магазином!")
    store_name = input("Введіть назву магазину: ")
    my_store = Store(store_name)

    while True:
        print("\nМеню:")
        print("1. Додати категорію")
        print("2. Додати товар до категорії")
        print("3. Переглянути категорії")
        print("4. Переглянути товари у категорії")
        print("5. Завершити роботу")
        
        choice = input("Виберіть опцію: ")
        if choice == "1":
            category_name = input("Введіть назву категорії: ")
            category = Category(category_name)
            my_store.add_category(category)

        elif choice == "2":
            if not my_store.categories:
                print("У магазині ще немає категорій. Спочатку додайте категорію.")
                continue
            my_store.list_categories()
            category_index = int(input("Виберіть номер категорії для додавання товару: ")) - 1
            if 0 <= category_index < len(my_store.categories):
                category = my_store.categories[category_index]
                product_name = input("Введіть назву товару: ")
                product_price = float(input("Введіть ціну товару: "))
                product_stock = int(input("Введіть кількість товару: "))
                product = Product(product_name, product_price, product_stock)
                category.add_product(product)
            else:
                print("Невірний номер категорії.")
        elif choice == '3':
            my_store.list_categories()
        elif choice == "4":
            if not my_store.categories:
                print("У магазині ще немає категорій.")
                continue
            my_store.list_categories()
            category_index = int(input("Виберіть номер категорії для перегляду товарів: ")) - 1
            if 0 <= category_index < len(my_store.categories):
                category = my_store.categories[category_index]
                category.list_products()
            else:
                print("Невірний номер")
        elif choice == "5":
            print("Дякуємо за використання програми!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#------------------------------------------------------
