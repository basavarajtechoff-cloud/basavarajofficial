#inheritance example
class company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        print(f"Company Name: {self.name}")
        print(f"Location: {self.location}")

class employee(company):
    def __init__(self, name, location, emp_name, emp_dept):
        super().__init__(name, location)  # Calls the constructor of the parent class (company).
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    def display_info1(self):
        super().display_info()  # Calls the display_info method of the parent class (company).
        print(f"Employee Name: {self.emp_name}")
        print(f"Department: {self.emp_dept}")

emp1 = employee("Wells", "Bangalore", "Basavaraj", "IT")  # Creates an instance of the employee class with company and employee details.
emp1.display_info()  # Calls the display_info method on the emp1 instance to display both company and employee information.
print("Now i use single level inheritance call from parent class to child class")
emp1.display_info1()  # Calls the display_info1 method on the emp1 instance to display both company and employee information, including the employee's name and department.