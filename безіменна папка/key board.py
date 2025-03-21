from pynput import keyboard

class RobotOficiant:
    def __init__(self, stravy):
        self.stravy = stravy
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.stravy):
            strava = self.stravy[self.index]
            self.index += 1
            return f"🤖 Ось ваша {strava}!"
        else:
            return "🍽 Всі страви подано!"

# Створюємо ітератор
menu = iter(RobotOficiant(["бургер", "паста", "піца"]))

def on_press(key):
    try:
        if key.char == '1':
            print(next(menu))
        elif key.char == 'q':
            print("👋 До побачення!")
            return False  # Завершуємо прослуховування
    except StopIteration:
        print("🍽 Всі страви подано!")

# Запускаємо прослуховування клавіш
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()