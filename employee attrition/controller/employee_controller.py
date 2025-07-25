import csv
from model.employee_model import Employee
from view.employee_view import EmployeeView
from ml_model import train_model, predict_attrition

class EmployeeController:
    def __init__(self):
        self.view = EmployeeView()
        self.filename = "employee_data.csv"

    def add_employee(self):
        name, experience, salary, workload, attrition = self.view.get_employee_input()
        employee = Employee(name, experience, salary, workload, attrition)
        self._save_to_csv(employee.to_dict())
        print("✅ Employee added successfully!\n")

    def _save_to_csv(self, employee_data):
        file_exists = False
        try:
            with open(self.filename, 'r'):
                file_exists = True
        except FileNotFoundError:
            pass

        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "experience", "salary", "workload", "attrition"])
            if not file_exists:
                writer.writeheader()
            writer.writerow(employee_data)

    def show_all_employees(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                employees = list(reader)
                if not employees:
                    print("🚫 No employee data available.\n")
                    return
                for emp in employees:
                    emp_obj = Employee(emp['name'], emp['experience'], emp['salary'], emp['workload'], emp['attrition'])
                    print(emp_obj, "\n")
        except FileNotFoundError:
            print("🚫 No employee data file found.\n")

    def train_and_predict(self):
        try:
            train_model(self.filename)
            print("✅ Model trained and saved successfully.\n")
            experience, salary, workload = self.view.get_prediction_input()
            result = predict_attrition(experience, salary, workload)
            print(f"📊 Prediction: {'Likely to LEAVE' if result == 1 else 'Likely to STAY'}\n")
        except Exception as e:
            print(f"❌ Error: {str(e)}\n")
