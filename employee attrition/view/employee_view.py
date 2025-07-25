class EmployeeView:
    def display_menu(self):
        print("\n📌 Employee Attrition Predictor")
        print("1. Add Employee")
        print("2. Show All Employees")
        print("3. Train Model & Predict Attrition")
        print("4. Exit")
        return input("Enter your choice: ")

    def get_employee_input(self):
        print("\n📝 Enter Employee Details:")
        name = input("👤 Name: ")
        experience = int(input("📆 Work Experience (in years): "))
        salary = int(input("💰 Monthly Salary (₹): "))
        workload = int(input("⏱️ Workload (hours per day): "))
        attrition = int(input("🔁 Attrition (1 = Yes, 0 = No): "))
        return name, experience, salary, workload, attrition

    def get_prediction_input(self):
        print("\n🔍 Enter details for prediction:")
        experience = int(input("📆 Experience (in years): "))
        salary = int(input("💰 Monthly Salary (₹): "))
        workload = int(input("⏱️ Workload (hours/day): "))
        return experience, salary, workload

    def show_employees(self, employees):
        if not employees:
            print("⚠️ No employee data found.")
            return

        print("\n📋 Employee Records:")
        print("-" * 60)
        for emp in employees:
            status = "Yes" if emp['attrition'] == 1 else "No"
            print(f"👤 Name: {emp['name']}")
            print(f"📆 Experience: {emp['experience']} years")
            print(f"💰 Salary: ₹{emp['salary']} / month")
            print(f"⏱️ Workload: {emp['workload']} hours/day")
            print(f"🔁 Attrition: {status}")
            print("-" * 60)

    def show_prediction_result(self, prediction):
        if prediction == 1:
            print("⚠️ Prediction: Employee is likely to leave (Attrition = YES).")
        else:
            print("✅ Prediction: Employee is likely to stay (Attrition = NO).")
