import json
import customtkinter as ctk
ctk.set_appearance_mode("dark")
app = ctk.CTk()
left_frame = ctk.CTkFrame(app, width=300)
left_frame.pack(side="left", fill="y", padx=20, pady=20)
title = ctk.CTkLabel(left_frame, text="Student Form", font=("Arial", 20, "bold"))
title.pack(pady=20)
name_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Name")
name_entry.pack(pady=10)
grade_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Grade")
grade_entry.pack(pady=10)
add_btn = ctk.CTkButton(left_frame, text="Add Student")
add_btn.pack(pady=20)
app.title("Student Grade Manager")
app.geometry("1000x600")
app.mainloop()
def load_students():
    global students

    try:
        with open("students.json", "r") as f:
            students = json.load(f)

    except FileNotFoundError:
        students = {}
def save_students():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
load_students()
def add_student():
    name = input("Enter student name: ").lower()
    grade = int(input("Enter student grade: "))
    students[name] = grade
    save_students()
    print(f"{name} added successfully.")
def highest_grade():
    if not students:
        print("No student data available.")
        return
    highest = max(students.values())
    top_students = [
        name
        for name, grade in students.items()
        if grade == highest
    ]
    print(f"Highest Grade: {highest}")
    print("Top Student(s):")
    for student in top_students:
        print(student)
def delete_student():
    name = input("Enter student name to delete: ").lower()
    if name in students:
        del students[name]
        save_students()
        print(f"{name} deleted successfully.")
    else:
        print("Student not found.")
def average_grade():
    if not students:
        print("No student data available.")
        return
    average = sum(students.values()) / len(students)
    print(f"Average Grade: {average:.2f}")
def view_all_students():
    if not students:
        print("No students found.")
        return
    print("\nStudent Records")
    for name, grade in students.items():
        print(f"{name} : {grade}")
while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("""Enter choice:

    1. Add Student
    2. Highest Grade
    3. Delete Student
    4. Average Grade
    5. View All Students
    6. Exit""")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
        save_students()
    elif choice == '2':
        highest_grade()
        
    elif choice == '3':
        delete_student()
        save_students()
    elif choice == '4':
        average_grade()
        
    elif choice == '5':
        view_all_students()
        load_students()
    elif choice == '6':
        print("Exiting Student Grade Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


 
