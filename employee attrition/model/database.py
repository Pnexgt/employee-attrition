import csv
import os

class Database:
    def __init__(self, filename='employees.csv'):
        self.filename = filename
        self.fields = ['name', 'experience', 'salary', 'workload', 'attrition']


        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()

    def add_employee(self, employee):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writerow({
                'name': employee['name'],
                'experience': employee['experience'],
                'salary': employee['salary'],
                'workload': employee['workload'],
                'attrition': employee['attrition']
            })

    def load_all_employees(self):
        data = []
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append([
                    row['name'],
                    int(row['experience']),
                    int(row['salary']),
                    int(row['workload']),
                    int(row['attrition'])
                ])
        return data
