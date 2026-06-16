class Student:

    def __init__(self, id, name, marks, age):
        self.Student_id = id
        self.name = name
        self.marks = marks
        self.age = age

    def display(self):
        print("\nStudent ID : ", self.Student_id)
        print("\nStudent Name : ", self.name)
        print("\nStudent Marks : ", self.marks)
        print("\nStudent Age : ", self.age)