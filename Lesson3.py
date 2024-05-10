class StudySubject:
    name: str
    hours: int
    enable: bool

    def __init__(self):
        self.name = input("Введіть назву предмета: ")
        self.hours = int(input("Введіть кількість годин: "))
        self.enable = bool(input("Введіть True, якщо предмет має доступ, інакше False: "))

    def info_study(self):
        print(f'Study: {self.name} | {self.hours}')

python = StudySubject()
# python.info_study()

class Student:
    name: str
    surname: str
    studies: list

    def __init__(self):
        self.name = input("Введіть і'мя студента: ")
        self.surname = input("Введіть призвіще студента: ")
        self.studies = []

        while True:
            study_name = input("Введіть назву предмета студента чи натисніть Enter для завершення: ")
            if not study_name:
                break
            study_hours = int(input("Введіть кількість годин: "))
            study_enable = bool(input("Введіть True, якщо предмет має доступ, інакше False: "))
            self.studies.append(StudySubject(study_name, study_hours, study_enable))

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')

    def info_all(self):
        self.info_student()
        for study in self.studies:
            study.info_study()


class Group:
    def __init__(self):
        self.group_name = input("Введіть назву групи: ")
        self.num_students = int(input("Введіть кількість студентів в групі: "))
        self.age_category = input("Введіть вікову категорію групи: ")
        self.students = []

        for _ in range(self.num_students):
            student = Student()
            self.students.append(student)

    def info_group(self):
        print(f'Group: {self.group_name} | {self.age_category} | {len(self.students)} students')

    def info_all_students(self):
        self.info_group()
        for student in self.students:
            student.info_all()

group = Group()
group.info_all_students()
