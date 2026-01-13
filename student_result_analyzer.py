import json

students = []

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
        load_students = []
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file)

def show_menu():
    print("\n🎓 Student Result Analyzer")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

def add_student():
    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))

    grade = calculate_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)
    save_students()
    print("✅ Student added successfully!")


def view_students():
    if not students:
        print("📭 No students found.")
    else:
        print("\n📊 Student Report")
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Mark: {student['mark']}")
            print(f"Grade: {student['grade']}")
            print("-" * 20)

    
def calculate_grade(mark):
    if mark>=75:
        return "Distinction"
    elif mark>=50:
        return "Pass"
    else:
        return "Fail"
def delete_student():
    name_to_delete = input("Enter student name to delete: ").lower()

    for student in students:
        if student["name"].lower() == name_to_delete:
            students.remove(student)
            save_students()
            print("🗑️ Student deleted successfully!")
            return

    print("❌ Student not found.")



while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Goodbye 👋")
        break
    else:
        print("❌ Invalid choice.")

