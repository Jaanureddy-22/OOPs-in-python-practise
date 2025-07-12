class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student:
    def __init__(self, roll_number, course):
        self.roll_number = roll_number
        self.course = course

class result:
    def __init__(self, marks):
        self.marks = marks

class collegestudent(person, student, result):
    def __init__(self, name, age, roll_number, course, marks):
        person.__init__(self, name, age)
        student.__init__(self, roll_number, course)
        result.__init__(self, marks)

    def display(self):
        print("---------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)
        print("Course:", self.course)
        print("Result:", self.marks)

# ✅ Now we write main logic OUTSIDE the class
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")
    marks = float(input("Enter 2nd sem marks: "))

    student_obj = collegestudent(name, age, roll_number, course, marks)
    students.append(student_obj)

print("\nAll Student Details:")
for student in students:
    student.display()
