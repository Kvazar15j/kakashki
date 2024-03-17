class Student:
    name = ""
    group = ""
    age = 0
    grades = []
    gpa = 0

    def __init__(self, name, group='', age=0, grades=()):
        self.name = name
        self.group = group
        self.age = age
        self.grades = grades
        if grades:
            self.gpa = round(sum(self.grades) / len(grades), 2)

    def show_info(self):
        print(f'{self.name} ({self.age} лет), группа {self.group}')
        print(f'средний бал: {self.gpa} ({self.grades})')
student1 = Student(name="Kent", group="B58H7", age=16, grades=[7, 2, 7, 10, 11, 8, 9, 2])
student2 = Student("Serega")
student2.group = "B58H7"
student2.age = 15
student2.grades = [12, 10, 11, 9, 7, 10, 8]

student1.show_info()
student2.show_info()