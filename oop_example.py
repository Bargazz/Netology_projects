class Student:
    def __init__(self, name, surname,):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_student_grades = {}

    def grades_student(self, lecturers, course, grade):
        if isinstance(lecturers, Lecturer) and course in lecturers.courses_attached and course in self.courses_in_progress:
            if course in lecturers.grades:
                lecturers.grades[course].append(grade)
                lecturers.average_lecturer_grades[course] = [sum(lecturers.grades[course]) / len(lecturers.grades[course])]
            else:
                lecturers.grades[course] = [grade]
        else:
            print('Ошибка')

    def all_average_grades(self):
        if not self.grades:
            return 0
        some_dict = []
        for item in self.grades.values():
            some_dict.extend(item)
        return sum(some_dict) / len(some_dict)

    def __eq__(self, other):
        if isinstance(other, Student):
            return 'Ошибка'
        return self.all_average_grades() == other.all_average_grades()

    def __lt__(self, other):
        if isinstance(other, Student):
            return 'Ошибка'
        return self.all_average_grades() < other.all_average_grades()

    def __le__(self, other):
        if isinstance(other, Student):
            return 'Ошибка'
        return self.all_average_grades() <= other.all_average_grades()

    def __str__(self):
        return f"\rИмя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за курс {', '.join(f'{key}: {round(values[0], 2)}' for key, values in self.average_student_grades.items())}" \
               f"\nСредняя оценка за дз {round(self.all_average_grades(), 1)}" \
               f"\nКурсы в процессе изучения: {self.courses_in_progress}" \
               f"\nЗавершенные курсы: {self.finished_courses}\n"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_lecturer_grades = {}

    def all_average_grades(self):
        if not self.grades:
            return 0
        some_dict = []
        for item in self.grades.values():
            some_dict.extend(item)
        return sum(some_dict) / len(some_dict)

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return 'Ошибка'
        return self.all_average_grades() == other.all_average_grades()

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return 'Ошибка'
        return self.all_average_grades() < other.all_average_grades()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return 'Ошибка'
        return self.all_average_grades() <= other.all_average_grades()

    def __str__(self):
        return f"\rИмя: {self.name}" \
               f"\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекцию: {', '.join(f'{key}: {round(values[0], 2)}' for key, values in self.average_lecturer_grades.items())}\n" \
               f"Средняя оценка за лекции: {round(self.all_average_grades(), 1)}\n" \



class Reviewer(Mentor):
    def grades_student(self, students, course, grade):
        if isinstance(students, Student) and course in students.courses_in_progress and course in self.courses_attached:
            if course in students.grades:
                students.grades[course].append(grade)
                students.average_student_grades[course] = [sum(students.grades[course]) / len(students.grades[course])]
            else:
                students.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return f"Имя: {self.name}" \
               f"Фамилия: {self.surname}"


student_1 = Student('Андрей', 'Петров')
student_1.courses_in_progress.append('Python')
student_1.finished_courses.append('C++')
student_1.finished_courses.append('JavaScript')
student_1.finished_courses.append("Основы программирования")

#Имя, фамилия, пол студента и что изучал/изучает
student_2 = Student('Александра', 'Иванова')
student_2.courses_in_progress.append('C++')
student_2.finished_courses.append('JavaScript')
student_2.finished_courses.append("Основы программирования")

#Имя, фамилия, пол студента и что изучал/изучает
student_3 = Student('Илья', 'Кочетков')
student_3.courses_in_progress.append('JavaScript')
student_3.finished_courses.append('C++')
student_3.finished_courses.append("Основы программирования")

#Имя, фамилия лектора и какие курсы приподаёт
PJ_lecturer1 = Lecturer('Фатима', 'Ахмедова')
PJ_lecturer1.courses_attached.append('Python')
PJ_lecturer1.courses_attached.append('JavaScript')
PJ_lecturer1.courses_attached.append("Основы программирования")

#Имя, фамилия лектора и какие курсы приподаёт
PJ_lecturer2 = Lecturer('Владимир', 'Федоров')
PJ_lecturer2.courses_attached.append('Python')
PJ_lecturer2.courses_attached.append('JavaScript')

#Имя, фамилия лектора и какие курсы приподаёт
C_lecturer1 = Lecturer('Данил', 'Микрон')
C_lecturer1.courses_attached.append('C++')
C_lecturer1.courses_attached.append('C')
C_lecturer1.courses_attached.append('C#')
C_lecturer1.courses_attached.append("Основы программирования")

#Имя, фамилия лектора и какие курсы приподаёт
C_lecturer2 = Lecturer('Яна', 'Симонова')
C_lecturer2.courses_attached.append('C++')
C_lecturer2.courses_attached.append('C')
C_lecturer2.courses_attached.append('C#')

#Имя, фамилия рецензента и по каким курсам проверяет
C_reviewer1 = Reviewer('Дмитрий', 'Прилужный')
C_reviewer1.courses_attached.append('C++')
C_reviewer1.courses_attached.append('C')
C_reviewer1.courses_attached.append('C#')

#Имя, фамилия рецензента и по каким курсам проверяет
C_reviewer2 = Reviewer('Ильдар', 'Цветков')
C_reviewer2.courses_attached.append('C++')
C_reviewer2.courses_attached.append('C')
C_reviewer2.courses_attached.append('C#')

#Имя, фамилия рецензента и по каким курсам проверяет
PJ_reviewer1 = Reviewer('Елена', 'Гриняева')
PJ_reviewer1.courses_attached.append('Python')
PJ_reviewer1.courses_attached.append('JavaScript')

#Имя, фамилия рецензента и по каким курсам проверяет
PJ_reviewer2 = Reviewer('Виктор', 'Вист')
PJ_reviewer2.courses_attached.append('Python')
PJ_reviewer2.courses_attached.append('JavaScript')

#Оценки 1 студента по курсам
PJ_reviewer1.grades_student(student_1, 'Python', 9)
PJ_reviewer2.grades_student(student_1, 'Python', 10)

#Оценки 2 студента по курсам
C_reviewer1.grades_student(student_2, 'C++', 9)
C_reviewer2.grades_student(student_2, 'C++', 6)

#Оценки 3 студента по курсам
PJ_reviewer1.grades_student(student_3, 'JavaScript', 9)
PJ_reviewer1.grades_student(student_3, 'JavaScript', 7)

#Оценки лекции от 1 студента по курсам
student_1.grades_student(PJ_lecturer1, 'Python', 10)
student_1.grades_student(PJ_lecturer2, 'Python', 9)

#Оценки лекции от 2 студента по курсам
student_2.grades_student(C_lecturer1, 'C++', 6)
student_2.grades_student(C_lecturer2, 'C++', 5)

#Оценки лекции от 3 студента по курсам
student_3.grades_student(PJ_lecturer1, 'JavaScript', 5)
student_3.grades_student(PJ_lecturer2, 'JavaScript', 10)


print(f"Список студентов:\n\n{student_1}\n{student_2}\n{student_3}\n")
print(f"Списор лекторов:\n\n{PJ_lecturer1}\n{PJ_lecturer2}\n{C_lecturer1}\n{C_lecturer2}")
print(f"Список рецензентов:\n\n{PJ_reviewer1}\n{PJ_reviewer2}\n{C_reviewer1}\n{C_reviewer2}")