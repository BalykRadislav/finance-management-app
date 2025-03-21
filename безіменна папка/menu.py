#новорічне меню
products = []
while True:
    print("\n===НОВОРІЧНЕ МЕНЮ===")
    print("1. Додати страву")
    print("2. Видалити страву")
    print("3. Переглянути всі страви")
    print("4. Вихід")
    choice = input("виберіть дію  (1-4): ")
    if choice == "1":
        name = input("введіть назву страви яку хочете додати: ")
        quantity = int(input("введіть к-сть страви: "))
        products.append({"name": name, "quantity": quantity})
        print(f"страву '{name}' успішно додано.")
    elif choice == "2":
        name = input("введіть назву страви яку хочете видалити: ")
        found = False
        for product in products:
            if product["name"].lower() == name.lower():
                 products.remove(product)
                 print(f"страва '{name}' видалена з списку")
        if not found:
            print(f"товар '{name}' не знайдено")
    elif choice =="3":
        if not products:
            print("список страв порожній")
        else:
            print("\nСписок :")
            for idx, product in enumerate(products, 1):
                print(f"{idx}. Назва: {product['name']}, Кількість: {product['quantity']}")
    

    elif choice == "4":
        print("вихід з програми...")
        break
    else :
        print("невідома команда , спробуйте ще раз")



     

