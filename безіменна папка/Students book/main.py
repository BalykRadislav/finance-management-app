from grades import input_student, add_student_frade, show_student_info

def main():
    # Функція що виконує головний код
    student = input_student()
    while True:
        print("\n===MENU===")
        print("1. Додати оцінку")
        print("2. Показати інформацію")
        print("3. Вийти")
        choice = input("Виберіть пункт: ")
        if choice == "1":
            add_student_frade(student)
        elif choice == "2":
            show_student_info(student)
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невірний вибір , спробуйте ще раз")

if __name__ == "__main__":
    main()
        



