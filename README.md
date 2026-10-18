# Python Student Management System

A beginner-friendly Python project that demonstrates how Object-Oriented Programming (OOP) can be used to manage student information and academic records.

The application allows users to create student records, store subject marks, retrieve students using their roll numbers, and display their academic details, including total marks and average marks.

## Features

- Create student records with names and roll numbers
- Prevent duplicate roll numbers
- Add subject marks for each student
- Store student subjects and marks
- Retrieve student records using roll numbers
- Display student information and enrolled subjects
- Calculate total marks and average marks
- Handle cases where a student record is not found

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Dictionaries and lists

## OOP Concepts Practiced

- Classes and objects
- Constructors (`__init__`)
- Instance attributes
- Instance methods
- Object interaction
- Data management using dictionaries and lists

## How It Works

The project contains two main classes.

### 1. Student

The `Student` class stores individual student information.

It includes methods to:

- Add marks for subjects
- Display student information
- Calculate total marks
- Calculate average marks

### 2. ManagementSystem

The `ManagementSystem` class manages student records using a dictionary.

It allows the program to:

- Add new students
- Check whether a roll number already exists
- Retrieve a student using their roll number
- Display a message when a student cannot be found

The program demonstrates these operations using two sample student records.

## Project Structure

python-student-management-system/
│
└── Sms(class fun).py

## How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository.
3. Open the project folder in your terminal.
4. Run the following command:

python "Sms(class fun).py"

5. The program will create sample student records, add subject marks, and display student information.

## Example Output

--- Welcome to School Management System ---

New student : 'Ashwin' added successfully!

New student : 'Muneeswaran' added successfully!

Student Name: Ashwin | Roll No: 101
Subjects Enrolled: ['Maths', 'Science']
Marks List: {'Maths': 95, 'Science': 88}
Total: 183 | Average: 91.50

The program also displays the corresponding details for the second student.

## Learning Outcomes

Through this project, I practiced:

- Designing classes and objects
- Using constructors and instance methods
- Managing records with dictionaries
- Storing subjects in lists
- Associating marks with subjects
- Implementing duplicate roll number checks
- Retrieving objects using dictionary keys
- Calculating totals and averages
- Organizing code using Object-Oriented Programming

## Project Background

I created this project as part of my Python learning journey to strengthen my understanding of OOP and explore how student records can be represented and managed using Python classes and objects.

## Future Improvements

- Add a menu-driven interface
- Allow users to enter student details dynamically
- Support updating and deleting student records
- Add input validation for marks
- Display all registered students
- Store student records in a file or database
- Add subject-wise performance reports

## Note

This is a beginner-level learning project. Student records are currently stored in memory and are not saved permanently.

## Author

Built as part of my Python learning journey.
