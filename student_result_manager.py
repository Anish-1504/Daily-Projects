student = {}

while True:
    print("\n---- Student Result Management System ----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Adding a Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        student[name] = marks 
        print(f"Student {name} added successfully!")

    # Viewing a Student
    elif choice == "2":
        if not student:
            print("No students found.")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # Checking Result
    elif choice == "3":
        name = input("Enter student name to check result: ")
        if name in student:
            marks = student[name]

            if marks > 40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student not found.")

    # Exiting the program
    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")