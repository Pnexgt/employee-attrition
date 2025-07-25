class Employee:
    def __init__(self, name, experience, salary, workload, attrition):
        self.name = name
        self.experience = experience       
        self.salary = salary                
        self.workload = workload            
        self.attrition = attrition          
    def to_dict(self):
        return {
            "name": self.name,
            "experience": self.experience,
            "salary": self.salary,
            "workload": self.workload,
            "attrition": self.attrition
        }

    def __str__(self):
        return (f"👤 Name: {self.name}\n"
                f"📆 Experience: {self.experience} years\n"
                f"💰 Salary: ₹{self.salary}/month\n"
                f"⏱️ Workload: {self.workload} hours/day\n"
                f"🔁 Attrition: {'Yes' if self.attrition == 1 else 'No'}")
