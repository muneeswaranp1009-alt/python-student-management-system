class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.subjects = [] 
        self.marks = {} 


    def add_marks(self, subject, mark):
        if subject not in self.subjects:
            self.subjects.append(subject)
        self.marks[subject] = mark
        print(f"{self.name} - {subject} mark : ({mark}) was added.")

    def display_info(self):
        print(f"\nStudent Name: {self.name} | Roll No: {self.roll_no}")
        print(f"Subjects Enrolled: {self.subjects}")
        print(f"Marks List: {self.marks}")
    
        if len(self.marks) > 0:
            total = sum(self.marks.values())
            average = total / len(self.marks)
            print(f"Total: {total} | Average: {average:.2f}")
        print("-" * 30)


class ManagementSystem:
    def __init__(self):
        self.student_db = {}

    def add_new_student(self, name, roll_no):
        if roll_no in self.student_db:
            print(f"\nRoll No {roll_no} already exists!")
        else:
            new_student = Student(name, roll_no)
            self.student_db[roll_no] = new_student
            print(f"\nNew student : '{name}' added successfully!\n")

    def get_student(self, roll_no):
        if roll_no in self.student_db:
            return self.student_db[roll_no]
        else:
            print(f"Student with Roll No '{roll_no}' not found.")
            return None

print("--- Welcome to School Management System ---")

admin = ManagementSystem()

admin.add_new_student("Ashwin", 101)
admin.add_new_student("Muneeswaran", 102)

student1 = admin.get_student(101)
student2 = admin.get_student(102)

if student1:
    student1.add_marks("Maths", 95)
    student1.add_marks("Science", 88)

if student2:
    student2.add_marks("Computer", 99)
    student2.add_marks("English", 92)

if student1: student1.display_info()
if student2: student2.display_info()