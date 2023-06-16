# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def set_age(self, age):
#         self.age = age

#     # def add(self, x):
#     #     return x + 1

#     # def bark(self):
#     #     print("bark")


# d = Dog("Muse", 24)
# d.set_age(34)
# print(d.get_age(8

# ))

# # print(d.name)
# # print(d.age)
# # d2 = Dog("Sage", 12)
# # print(d2.get_name())
# # print(d2.get_age())
# # print(d.add(3))
# # d.bark()


class student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = student("Geko", 19, 35)
s2 = student("Sage", 12, 34)
s3 = student("reyna", 23, 56)

Course = Course("Science", 2)
Course.add_student(s1)
Course.add_student(s2)

print(Course.get_avg())
