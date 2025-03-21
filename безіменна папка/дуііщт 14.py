# КОРТЕЖІ
# my_tuple = (1, 2, 3)

#  -----------------------------------------------------

# treasure = ("gold coins", "ancient parchment", "treasure map")
# my_tuple = ("apple", 42, 3.14)
# print(treasure)
# print(my_tuple)

#  -----------------------------------------------------

# my_tuple = ("apple", "banana", "cherry")

#  Отримати перший елемент
# print(my_tuple[0])  # Виведе: apple

#  Отримати останній елемент
# print(my_tuple[-1])  

#  -----------------------------------------------------

# my_tuple = ("apple", "banana", "cherry")

# print(my_tuple[0])  

# print(my_tuple[-1])  


#  -----------------------------------------------------

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# combined_tuple = tuple1 + tuple2
# print(combined_tuple)

#  -----------------------------------------------------

# def get_coordinates():
#     return (40.7128, -74.0060)

# coordinates = get_coordinates()
# print(coordinates)

#  -----------------------------------------------------

# trip = ("Italy", 7, ["Rome", "Florence", "Venice"])
# trip[2].append("Milan")
# print(trip)

#  -----------------------------------------------------

# def print_tuple_info(t):
#     print(f"Перший елемент: {t[0]}")
#     print(f"Другий елемент: {t[1]}")

# my_tuple = ("apple", 10)
# print_tuple_info(my_tuple)

#  -----------------------------------------------------

# def calculate():
#     a = 5
#     b = 10
#     return a, b  

# result = calculate()
# print(result)


#  -----------------------------------------------------

# my_tuple = ("apple", "banana", "cherry")
# a, b, c = my_tuple
# for item in my_tuple:
#     print(item)

#  -----------------------------------------------------

# my_dick = {("a", "b"): "value1", ("x", "y"): "value2"}
# print(my_dick[("a", "b")])

#  -----------------------------------------------------
store_prices = {
    ("T-shirt", "M"): 15.99,  
    ("T-shirt"): 17.99, 
    ("Jeans", "32"): 49.99,   
    ("Jeans", "34"): 51.99,   
    ("Jacket", "L"): 89.99   
}
def get_price(product, size):
    
    if (product, size) in store_prices:
        return store_prices[(product, size)]
    else:
        return "Товар або розмір не знайдено."
product_name = "T-shirt"
product_size = "L"
price = get_price(product_name, product_size)
print(f"Ціна {product_name} розміру {product_size}: {price} грн.")

#  -----------------------------------------------------
#  -----------------------------------------------------
#  -----------------------------------------------------
#  -----------------------------------------------------
#  -----------------------------------------------------