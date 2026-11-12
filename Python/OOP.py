#OOP
#Classes
class employee:
    emp_name='Basavaraj'
    emp_dept='CDO'

    def info(self):
       print(f"Employee {self.emp_name} works in {self.emp_dept} department")  # Displays the employee's name and department.  
    def info1(self,emp_name,emp_dept):
        print(f"Employee {emp_name} works in {emp_dept} department")

emp1=employee()  # Creates an instance of the employee class.
emp1.info()  # Calls the info method on the emp1 instance to display the employee
    
emp2=employee()  # Creates another instance of the employee class and calls the info method to display the employee's information.  
emp2.info1("Ravi","HR")

#constructors
class employee1:
    def __init__(self,emp_name,emp_dept):
        self.emp_name=emp_name
        self.emp_dept=emp_dept

    def info(self):
       print(f"Employee {self.emp_name} works in {self.emp_dept} department")  # Displays the employee's name and department.

emp1=employee1("Chetu","IT")  # Creates an instance of the employee1 class with specified name and department.

emp1.info()  # Calls the info method on the emp1 instance to display the employee's information.

#static methods , class methods and instance methods
class employee2:
    emp_name='Basavaraj'
    emp_dept='CDO'

    def info(self):
       print(f"Employee {self.emp_name} works in {self.emp_dept} department")  # Displays the employee's name and department.

    @classmethod
    def info1(cls,emp_name,emp_dept):
        cls.emp_name=emp_name  # Updates the class variable emp_name with the provided value.
        cls.emp_dept=emp_dept  # Updates the class variable emp_dept with
        print(f"Employee {cls.emp_name} works in {cls.emp_dept} department")  # Displays the employee's name and department using class method.

    @staticmethod
    def info2():
        print("This is a static method")  # Displays a message indicating that this is a static method. 

emp1=employee2()  # Creates an instance of the employee2 class.
emp1.info()  # Calls the info method on the emp1 instance to display the employee's information.
employee2.info1("Raj","Admin")  # Calls the class method info1 on the employee2 class
employee2.info2()  # Calls the static method info2 on the employee2 class   

#getters and setters
class employee3:
    def __init__(self,emp_name,emp_dept):
        self.__emp_name=emp_name  # Initializes the private instance variable __emp_name with the provided value.
        self.__emp_dept=emp_dept  # Initializes the private instance variable __emp_dept with the provided value.

    def get_emp_name(self):
        return self.__emp_name  # Returns the value of the private instance variable __emp_name.

    def set_emp_name(self,emp_name):
        self.__emp_name=emp_name  # Updates the value of the private instance variable __emp_name with the provided value.

    def get_emp_dept(self):
        return self.__emp_dept  # Returns the value of the private instance variable __emp_dept.

    def set_emp_dept(self,emp_dept):
        self.__emp_dept=emp_dept  # Updates the value of the private instance variable __emp_dept with the provided value.

    def info(self):
       print(f"Employee {self.__emp_name} works in {self.__emp_dept} department")  # Displays the employee's name and department using private variables.

emp1=employee3("Rajjjjjj","TCOO")  # Creates an instance of the employee3 class with specified name and department.
emp1.info()  # Calls the info method on the emp1 instance to display the employee's information.        
emp1.set_emp_name("Raviiii")  # Updates the employee's name using the setter method.
emp1.set_emp_dept("HRrrr")  # Updates the employee's department using the setter
emp1.info()  # Calls the info method again to display the updated employee's information.