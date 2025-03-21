# Створіть структуру даних для зберігання інформації про кошельки користувачів. Кожен кошелек містить назву валюти і баланс.
# Дозвольте користувачам створювати новий кошелек з заданою валютою і початковим балансом.
# Дозвольте користувачу ввести та зберегти курси конвертації між валютами.
# Реалізуйте функцію, що дозволяє конвертувати певну суму з одного кошелька в інший за заданим курсом.
# Напишіть функцію, яка виводить поточний стан всіх кошельків користувача.
# Логуйте всі операції з кошельками для можливості відстеження історії транзакцій користувача.
# Додайте можливість "перезавантажувати" кошельки, тобто встановлювати баланс кошельків на задану суму або видаляти всі кошельки для нової сесії.

class CurrencyWallet:
    def init(self):
        self.wallets = {}
        self.exchange_rates = {}  # Курси обміну
        self.transaction_log = []

    def create_wallet(self, currency, balance):
        if currency in self.wallets:
            print(f"Кошелек з валютою {currency} вже існує.")
        else:
            self.wallets[currency] = balance
            print(f"Кошелек з валютою {currency} створено з балансом {balance}.")

    def set_exchange_rate(self, from_currency, to_currency, rate):
        if from_currency not in self.wallets or to_currency not in self.wallets:
            print("Введена валюта відсутня серед кошельків.")
        else:
            self.exchange_rates[(from_currency, to_currency)] = rate
            print(f"Курс обміну {from_currency} -> {to_currency} встановлено на рівні {rate}.")

    def convert_currency(self, from_currency, to_currency, amount):
        if from_currency not in self.wallets or to_currency not in self.wallets:
            print("Одна з валют відсутня серед кошельків.")
            return

        if (from_currency, to_currency) not in self.exchange_rates:
            print("Курс обміну для цих валют не встановлено.")
            return
        
        rate = self.exchange_rates[(from_currency, to_currency)]
        converted_amount = amount * rate

        self.wallets[from_currency] -= amount
        self.wallets[to_currency] += converted_amount

        transaction = {
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "converted_amount": converted_amount,
            "rate": rate,
        }
        self.transaction_log.append(transaction)
        print(f"Конвертовано {amount} {from_currency} -> {converted_amount:.2f} {to_currency}.")

    def show_wallets(self):
        print("\nСтан кошельків:")
        for currency, balance in self.wallets.items():
            print(f"{currency}: {balance:.2f}")

    def show_transaction_log(self):
        print("\nІсторія транзакцій:")
        for transaction in self.transaction_log:
            print(transaction)

    def reset_wallets(self):
        self.wallets.clear()
        self.transaction_log.clear()
        print("Всі кошельки видалено.")
if name == "main":
    wallet_manager = CurrencyWallet()

    while True:
        print("\nМеню:")
        print("1. Створити кошелек")
        print("2. Встановити курс обміну")
        print("3. Конвертувати валюту")
        print("4. Показати стан кошельків")
        print("5. Показати історію транзакцій")
        print("6. Скинути кошельки")
        print("7. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            currency = input("Введіть назву валюти: ")
            balance = float(input("Введіть початковий баланс: "))
            wallet_manager.create_wallet(currency, balance)

        elif choice == "2":
            from_currency = input("З якої валюти: ")
            to_currency = input("В яку валюту: ")
            rate = float(input("Введіть курс обміну: "))
            wallet_manager.set_exchange_rate(from_currency, to_currency, rate)

        elif choice == "3":
            from_currency = input("З якої валюти: ")
            to_currency = input("В яку валюту: ")
            amount = float(input("Введіть суму для конвертації: "))
            wallet_manager.convert_currency(from_currency, to_currency, amount)

        elif choice == "4":
            wallet_manager.show_wallets()

        elif choice == "5":
            wallet_manager.show_transaction_log()

        elif choice == "6":
            wallet_manager.reset_wallets()

        elif choice == "7":
            print("Вихід із програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")