class Item:
    def __init__(self, name, price, ammount):
        self.name = name
        self.price = price
        self.ammount = ammount
    
    def buy(self, ammount):
        if ammount > self.ammount:
            raise ValueError(f"Not enough of item: {self.name}")
        self.ammount -= ammount
        return self.price * ammount
    

class Shop:
    def __init__(self):
        self.items = {
                "apple": Item("apple", 5, 10),
                "milk": Item("milk", 10, 7),
                "pen": Item("pen", 20, 9)
        }

    def buy_item(self, name, ammount, money):
        if name not in self.items:
            raise KeyError(f"Товар {name} не знайдено")
        item = self.items[name]
        general_price = item.buy(ammount)

        if money < general_price:
            raise ValueError("Немає грошей")
        решта = money - general_price
        return f"Ви купили {ammount} {name}. Ваша решта: {решта}"
    
shop = Shop()

try:
    item = input("Який товар бажаєте придбати: ")
    ammount = int(input("How much: "))
    money = int(input("Скільки у вас грошей: "))
    result = shop.buy_item(item, ammount, money)
    print(result)
except ValueError as e:
    print("Error", e)
except KeyError as e:
    print("Error", e)

finally:
    print("Thanks!")