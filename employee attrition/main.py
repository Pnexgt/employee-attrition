from controller.employee_controller import EmployeeController

def main():
    controller = EmployeeController()
    
    while True:
        choice = controller.view.display_menu()
        
        if choice == '1':
            controller.add_employee()
        elif choice == '2':
            controller.show_all_employees()
        elif choice == '3':
            controller.train_and_predict()
        elif choice == '4':
            print("👋 Exiting Employee Attrition Predictor.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
