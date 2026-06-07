students={
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Eve": 90
}

print("===== STUDENT GRADE MANAGER =====")
print("""Enter choice:\n
    1. Add Student
    2. Highest Grade
    3. Delete Student
    4. Average Grade
    5. Exit""")
def add_student():
    name = input("Enter student name: ")
    grade = int(input("Enter student grade: "))
    students[name] = grade
    print(f"Student {name} added with grade {grade}.")
def highest_grade():
    if students:
        highest = max(students.values())
        top_students = [name for name, grade in students.items() if grade == highest]
        print(f"Highest grade: {highest} by {', '.join(top_students)}")
def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"Student {name} deleted.")
    else:
        print(f"Student {name} not found.")
def average_grade():
    if students:
        avg = sum(students.values()) / len(students)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No students to calculate average grade.")
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
        continue
    elif choice == '2':
        highest_grade()
        
    elif choice == '3':
        delete_student()
        
    elif choice == '4':
        average_grade()
        
    elif choice == '5':
        print("Exiting Student Grade Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
    

    