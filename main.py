import json
import customtkinter as ctk

students = {}
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
    name = name_entry.get().lower()
    grade = int(grade_entry.get())
    students[name] = grade
    save_students()
    show_students()
def highest_grade():
    if students:
        highest = max(students.values())
        result_label.configure(text=f"Highest: {highest}")
def delete_student():
    name = name_entry.get().lower()
    if name in students:
        del students[name]
        save_students()
        show_students()
    else:
        print("Student not found.")
def average_grade():
    if students:
        avg = sum(students.values()) / len(students)
        result_label.configure(text=f"Average: {avg:.2f}")
def view_all_students():
    if not students:
        print("No students found.")
        return
    print("\nStudent Records")
    for name, grade in students.items():
        print(f"{name} : {grade}")
def show_students():
    student_box.delete("1.0", "end")
    for name, grade in students.items():
        student_box.insert("end", f"{name} : {grade}\n")
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Student Grade Manager")
app.geometry("1000x600")

left_frame = ctk.CTkFrame(app, width=300)
left_frame.pack(side="left", fill="y", padx=20, pady=20)

title = ctk.CTkLabel(left_frame, text="Student Form", font=("Arial", 20, "bold"))
title.pack(pady=20)

name_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Name")
name_entry.pack(pady=10)

grade_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter Grade")
grade_entry.pack(pady=10)
add_btn = ctk.CTkButton(left_frame, text="Add Student", command=add_student)
add_btn.pack(pady=10)

delete_btn = ctk.CTkButton(left_frame, text="Delete Student", command=delete_student)
delete_btn.pack(pady=10)

avg_btn = ctk.CTkButton(left_frame, text="Show Average", command=average_grade)
avg_btn.pack(pady=10)

highest_btn = ctk.CTkButton(left_frame, text="Highest Grade", command=highest_grade)
highest_btn.pack(pady=10)
right_frame = ctk.CTkFrame(app)
right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

right_title = ctk.CTkLabel(right_frame, text="Students List", font=("Arial", 20, "bold"))
right_title.pack(pady=20)

student_box = ctk.CTkTextbox(right_frame, width=400, height=400)
student_box.pack(pady=10)
result_label = ctk.CTkLabel(right_frame, text="", font=("Arial", 16))
result_label.pack(pady=10)

show_students()

app.mainloop()



 
