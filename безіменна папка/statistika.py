import os
import random

# Функція для виведення ігрового поля
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("|".join(row))
    print("-" * (len(board) * 2 - 1))



def get_random_move(board):
    empty_cells = [(r, c) for r in range(len(board)) for c in range(len(board)) if board[r][c] == " "]
    return random.choice(empty_cells) if empty_cells else None

stats = {"X": 0, "O": 0, "draws": 0}

while True:
    try:
        size = int(input("Введіть розмір поля (мінімум 3): "))
        if size < 3:
            print("Розмір поля повинен бути не менше 3. Спробуйте ще раз.")
            continue
    except ValueError:
        print("Будь ласка, вводьте лише числа. Спробуйте ще раз.")
        continue

    board = [[" " for _ in range(size)] for _ in range(size)]
    current_player = "X"
    winner = None

    mode = input("Виберіть режим гри: 1 - два гравці, 2 - проти комп'ютера: ").strip()
    play_against_ai = mode == "2"

    # Гра
    while True:
        print_board(board)
        if current_player == "X" or not play_against_ai:
            print(f"Гравець {current_player}, ваш хід.")
            try:
                row = int(input(f"Введіть номер рядка (0-{size-1}): "))
                col = int(input(f"Введіть номер колонки (0-{size-1}): "))

                if row < 0 or row >= size or col < 0 or col >= size:
                    print("Невірні координати. Спробуйте ще раз.")
                    continue
                if board[row][col] != " ":
                    print("Ця клітинка вже зайнята. Спробуйте іншу.")
                    continue
            except ValueError:
                print("Будь ласка, вводьте лише числа. Спробуйте ще раз.")
                continue
        else:
            print("Хід комп'ютера...")
            row, col = get_random_move(board)

        board[row][col] = current_player

        # Перевірка виграшу
        winner = None

        # Перевірка рядків
        for r in board:
            if all(cell == current_player for cell in r):
                winner = current_player

        # Перевірка колонок
        for c in range(size):
            if all(board[r][c] == current_player for r in range(size)):
                winner = current_player

        # Перевірка діагоналей
        if all(board[i][i] == current_player for i in range(size)):
            winner = current_player
        if all(board[i][size - i - 1] == current_player for i in range(size)):
            winner = current_player

        
    # Перевірка на нічию
        draw = all(cell != " " for row in board for cell in row)

        if winner:
            print_board(board)
            print(f"Гравець {winner} виграв!")
            stats[winner] += 1  # Оновлення статистики для переможця
            break
        elif draw:
            print_board(board)
            print("Нічия!")
            stats["draws"] += 1  # Оновлення статистики для нічиї
            break

        current_player = "O" if current_player == "X" else "X"

    # Виведення статистики
    print("\nСтатистика:")
    print(f"Перемоги X: {stats['X']}")
    print(f"Перемоги O: {stats['O']}")
    print(f"Нічиї: {stats['draws']}")

    play_again = input("\nХочете зіграти ще раз? (так/ні): ").strip().lower()
    if play_again != "так":
        print("Дякуємо за гру!")
        break