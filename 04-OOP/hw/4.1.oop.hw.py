import datetime


class Homework:
    """class for your homework"""

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        now = datetime.datetime.now()
        if now < self.deadline + self.created:
            return True
        else:
            return False


class Student:
    """Description of the students"""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return


class Teacher:
    """Description of the teacher"""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

teacher = Teacher('Daniil', 'Shadrin')
student = Student('Roman', 'Petrov')
teacher.last_name
student.first_name  # Petrov

expired_homework = teacher.create_homework('Learn functions', 0)
expired_homework.created = datetime.datetime(2019, 11, 27, 2, 2, 19, 470181)
expired_homework.created
expired_homework.deadline  # 0:00:00
expired_homework.text  # 'Learn functions'

# create function from method and use it
create_homework_too = teacher.create_homework
oop_homework = create_homework_too('create 2 simple classes', 5)
print(oop_homework.deadline)  # 5 days, 0:00:00

student.do_homework(oop_homework)
student.do_homework(expired_homework)  # You are late
