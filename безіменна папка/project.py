import random

# Розміри поля
BOARD_SIZE = 5

# Створення пустої дошки
def create_board(size):
    return [[" "] * size for _ in range(size)]

# Виведення дошки
def print_board(board):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for idx, row in enumerate(board):
        print(str(idx) + " " + " ".join(row))

# Перевірка, чи координати валідні
def is_valid_placement(board, x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == " "

# Розстановка кораблів гравцем
def place_ships(board, num_ships):
    for _ in range(num_ships):
        while True:
            try:
                print_board(board)
                coords = input("Введіть координати для корабля (формат: x y): ").split()
                x, y = int(coords[0]), int(coords[1])
                if is_valid_placement(board, x, y):
                    board[x][y] = "S"  # S позначає корабель
                    break
                else:
                    print("Неправильне місце! Спробуйте ще раз.")
            except (ValueError, IndexError):
                print("Будь ласка, введіть координати у форматі: x y (наприклад, 1 2)")

# Розстановка кораблів комп'ютером
def place_computer_ships(board, num_ships):
    for _ in range(num_ships):
        while True:
            x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
            if is_valid_placement(board, x, y):
                board[x][y] = "S"
                break

# Хід гравця
def player_turn(computer_board, visible_board):
    while True:
        try:
            print_board(visible_board)
            coords = input("Ваш постріл (формат: x y): ").split()
            x, y = int(coords[0]), int(coords[1])
            if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                if computer_board[x][y] == "S":
                    print("Влучили!")
                    visible_board[x][y] = "X"
                    computer_board[x][y] = " "
                elif visible_board[x][y] == " ":
                    print("Промах!")
                    visible_board[x][y] = "-"
                else:
                    print("Ви вже стріляли сюди.")
                break
            else:
                print("Координати поза межами дошки. Спробуйте ще раз.")
        except (ValueError, IndexError):
            print("Будь ласка, введіть координати у форматі: x y.")

# Хід комп'ютера
def computer_turn(player_board):
    while True:
        x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
        if player_board[x][y] == "S":
            print(f"Комп'ютер влучив у ({x}, {y})!")
            player_board[x][y] = "X"
            break
        elif player_board[x][y] == " ":
            print(f"Комп'ютер промахнувся ({x}, {y}).")
            player_board[x][y] = "-"
            break

# Перевірка на перемогу
def check_victory(board):
    for row in board:
        if "S" in row:
            return False
    return True

# Основна гра
def play_game():
    print("Ласкаво просимо до гри 'Морський бій'!")
    player_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)
    visible_computer_board = create_board(BOARD_SIZE)
    
    num_ships = 3  # Кількість кораблів для кожного
    
    print("Розставте свої кораблі.")
    place_ships(player_board, num_ships)
    print("Комп'ютер розставляє свої кораблі...")
    place_computer_ships(computer_board, num_ships)
    
    while True:
        print("\nВаше поле:")
        print_board(player_board)
        print("\nПоле комп'ютера:")
        print_board(visible_computer_board)
        
        # Хід гравця
        print("\nВаш хід!")
        player_turn(computer_board, visible_computer_board)
        if check_victory(computer_board):
            print("Ви виграли! Усі кораблі комп'ютера знищені.")
            break
        
        # Хід комп'ютера
        print("\nХід комп'ютера!")
        computer_turn(player_board)
        if check_victory(player_board):
            print("Ви програли! Усі ваші кораблі знищені.")
            break

# Запуск гри
play_game()
