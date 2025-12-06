import sqlite3

# Connecting to Database
con = sqlite3.connect("employees.db")
cur = con.cursor()

# Creating table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
""")

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")

    cur.execute("INSERT INTO employee (name, age, department) VALUES (?, ?, ?)", 
                (name, age, department))
    con.commit()
    print("Employee added successfully!")

def view_employees():
    cur.execute("SELECT * FROM employee")
    records = cur.fetchall()

    if records:
        for emp in records:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}")
    else:
        print("No employees found!")

def search_employee():
    emp_id = int(input("Enter Employee ID: "))
    cur.execute("SELECT * FROM employee WHERE id = ?", (emp_id,))
    emp = cur.fetchone()

    if emp:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}")
    else:
        print("Employee not found!")

def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    cur.execute("DELETE FROM employee WHERE id = ?", (emp_id,))
    con.commit()
    print("Employee deleted successfully!")

def menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            delete_employee()
        elif choice == 5:
            break
        else:
            print("Invalid choice, Please try again!")

if __name__ == "__main__":
    menu()
    con.close()
