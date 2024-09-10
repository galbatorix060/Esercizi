from Corsi_ITS2 import Group
from Corsi_ITS2 import Student

class Course:
    def __init__(self, name) -> None:
        groups: list[Group] = []
        self.name = name
        self.groups = groups
    
    def register(self, student : Student):
        for i in self.groups:
                if len(i.get_students()) < i.get_limit() and student not in i.get_students():
                    i.add_student(student)
                    return

    def get_gruops(self):
        return self.groups
    
    def add_group(self, group : Group):
        self.groups.append(group)