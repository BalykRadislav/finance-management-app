from student import Student


def input_student():
    # Функція що створює студента
    name = input("Введіть ім'я студента: ")
    return Student(name)

def add_student_frade(student):
    # Функція що додає оцінку студенту
    subject = input("Введіть предмет: ")
    try:
        grade = float(input("Введіть оцінку: "))
        student.add_grade(subject, grade)
        print(f"Оцінка {grade} з предмету {subject} додана")
    except ValueError:
        print("Оцінка повинна бути числом")
    
def show_student_info(student):
    # Функція що виводить інформацію про студента
    print(f"\nСтудент: {student.name}")
    student.show_grades()
    print(f"Середній бал: {student.average_grade()}")
   
