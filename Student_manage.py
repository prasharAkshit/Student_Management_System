from Student import Student as S

class Student_Management():
    def __init__(self):
        self.students = []

    def add_student(self):
        
        student_id = int(input("Enter Student Id: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Student Marks: "))
        age = int(input("Enter Student Age: "))

        student = S(student_id, name, marks, age)
        self.students.append(student)

        print("Student Added Successfully...")

    def view_Student(self):
        if len(self.students) == 0:
            print("No student is found...")
            return
        
        for i in self.students:
            print("Name: ", i.name)
            print("ID: ", i.Student_id)
            print("\n")
    
    def search_Student(self):
        field = {
            "ID" : "Student_id",
            "NAME" : "name",
            "MARKS" : "marks",
            "AGE" : "age"
        }

        key = input("Search By: ")
        if key.upper() not in field:
            return print("Invalid Field")
        
        value = input(f"Enter a {key}: ")
        value = value if key.lower() == "name" else int(value)

        student = [s for s in self.students if getattr(s, field[key.upper()]) == value]

        if student:
            print("Student Found!!")
            for i in student:
                i.display()
        
        else:
            print("Student Not Found!!")

    def update_marks(self):
        id = int(input("Enter Student ID: "))

        for i in self.students:
            if i.id == id:
                new_marks = float(input("Enter marks: "))
                i.marks = new_marks
                print("Marks updated successfully...")
                return
        print("Student now found...")

    def delete_Student(self):
        id = int(input("Enter Student ID: "))

        for i in self.students:
            if i.id == id:
                self.students.remove(i)
                print("Student Deleted Successfully...")
                return
        print("Student not found...")

    def display_topper(self):
        if not self.students:
            print("No Student Available...")
            return

        max(self.students, key=lambda s: s.marks).display()