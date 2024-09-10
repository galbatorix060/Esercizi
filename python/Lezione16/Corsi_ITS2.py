class Person:
    def __init__(self, cf, name, surname, age) -> None:
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
    
class Student(Person):
    def __init__(self, cf, name, surname, age) -> None:
        super().__init__(cf, name, surname, age)
        self.group : Group = None

    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    def __init__(self, cf, name, surname, age) -> None:
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name, limit) -> None:
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
        self.limit_lecturers = 0

    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        cont = 0
        for i in self.students:
            cont += 1
            if cont % 10 == 0:
                self.limit_lecturers += 1
        return int(self.limit_lecturers)
    
    def add_student(self, student : Student):
        if student not in self.students:
            if len(self.students) < self.limit:
                self.students.append(student)

    def add_lecturer(self, lecturer):
        if len(self.lecturers) <= self.get_limit_lecturers():
            self.lecturers.append(lecturer)