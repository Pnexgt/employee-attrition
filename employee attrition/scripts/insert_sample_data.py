from model.employee import Employee
from model.database import Database

def insert_sample_employees():
    db = Database()
    sample_employees = [
        Employee("Alice", 2, 35000, 45, 0),
        Employee("Bob", 5, 60000, 55, 1),
        Employee("Charlie", 1, 30000, 40, 0),
        Employee("David", 7, 70000, 60, 1),
        Employee("Eve", 3, 40000, 50, 0),
        Employee("Frank", 6, 50000, 58, 1),
        Employee("Grace", 4, 45000, 48, 0),
        Employee("Hannah", 8, 80000, 65, 1),
        Employee("Ivy", 1, 25000, 38, 0),
        Employee("Jack", 5, 65000, 62, 1),
    ]
    for emp in sample_employees:
        db.insert_employee(emp)
    print("Inserted sample employees into database.")

if __name__ == "__main__":
    insert_sample_employees()
