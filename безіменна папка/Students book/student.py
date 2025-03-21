class Student:
    def __init__(self, name ):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        # Функція що додає оцінку з предмету
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def average_grade(self):
        # Функція що повертає середній бал
        total_grades = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total_grades / count, 2) if count > 0 else 0

    def show_grades(self):
        # Функція що виводить всі оцінки
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")