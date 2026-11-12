"""A small command-line employee directory for practicing Python fundamentals."""

from functools import reduce
import threading


# Inheritance: Company holds details shared by the company and its employees.
class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name} | Location: {self.location}")


# Employee inherits the company details and adds employee-specific information.
class Employee(Company):
    _created_count = 0

    def __init__(self, employee_id, name, department, salary, company_name, location):
        super().__init__(company_name, location)  # Initialize the shared Company fields.
        self.__employee_id = employee_id  # Double underscores keep these fields internal to the class.
        self.set_name(name)
        self.set_department(department)
        self.set_salary(salary)  # Use the setter so salary validation is applied at creation.
        Employee._created_count += 1

    # Getters and setters provide controlled access to the private employee fields.
    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name.strip(): 
            raise ValueError("Employee name cannot be empty.")
        self.__name = name.strip()

    def get_department(self):
        return self.__department

    def set_department(self, department):
        if not department.strip():
            raise ValueError("Department cannot be empty.")
        self.__department = department.strip()

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if not self.is_valid_salary(salary):
            raise ValueError("Salary must be a non-negative number.")
        self.__salary = float(salary)

    @staticmethod
    def is_valid_salary(salary):
        """A static method validates a value without needing an Employee object."""
        return isinstance(salary, (int, float)) and salary >= 0

    @classmethod
    def created_count(cls):
        """A class method returns how many Employee objects were created this run."""
        return cls._created_count


# The directory uses both a list (display order) and a dictionary (ID lookup).
class EmployeeDirectory:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location
        self._employees = []
        self._hire_order = []
        self._employees_by_id = {}

    def add_employee(self, employee_id, name, department, salary):
        employee_id = employee_id.strip()
        if not employee_id:
            raise ValueError("Employee ID cannot be empty.")
        if employee_id in self._employees_by_id:
            raise ValueError(f"Employee ID '{employee_id}' already exists.")

        employee = Employee(
            employee_id,
            name,
            department,
            salary,
            self.company_name,
            self.location,
        )
        self._employees.append(employee)  # append adds each new hire to the list.
        self._hire_order.append(employee)  # Keep hire chronology separate from the display order.
        self._employees_by_id[employee_id] = employee  # The dictionary enables direct ID lookup.
        return employee

    def find_by_id(self, employee_id):
        employee = self._employees_by_id.get(employee_id)
        if employee is None:
            raise ValueError(f"No employee has ID '{employee_id}'.")
        return employee

    def search_by_name(self, search_text):
        # A list comprehension collects every name containing the search text.
        return [
            employee
            for employee in self._employees
            if search_text.casefold() in employee.get_name().casefold()
        ]

    def filter_by_department(self, department):
        # This comprehension creates a new list and leaves the directory unchanged.
        return [
            employee
            for employee in self._employees
            if employee.get_department().casefold() == department.casefold()
        ]

    def pin_to_top(self, employee_id):
        employee = self.find_by_id(employee_id)
        self._employees.remove(employee)  # Remove it from its current display position.
        self._employees.insert(0, employee)  # Insert it at index zero to pin it to the top.

    def remove_employee(self, employee_id):
        employee = self._employees_by_id.pop(employee_id, None)  # pop removes the ID mapping.
        if employee is None:
            raise ValueError(f"No employee has ID '{employee_id}'.")
        self._employees.pop(self._employees.index(employee))  # Remove the same object from the list.
        self._hire_order.remove(employee)
        return employee

    def all_employees(self):
        # Slicing returns a copy so callers cannot change the directory's list directly.
        return self._employees[:]

    def latest_hires(self, limit=3):
        # Negative slicing selects newest hires even if display order was changed by pinning.
        if limit <= 0:
            return []
        return self._hire_order[-limit:][::-1]


# *args accepts any number of employee records; **options accepts named display settings.
def print_employee_list(*employee_records, **options):
    allowed_options = {"title", "show_company"}
    unknown_options = set(options) - allowed_options
    if unknown_options:
        raise TypeError(f"Unknown display option(s): {', '.join(sorted(unknown_options))}")

    title = options.get("title", "Employee Directory")
    show_company = options.get("show_company", False)
    print(f"\n--- {title} ---")

    if not employee_records:
        print("No employees to display.")
        return

    for employee in employee_records:
        print(
            f"ID: {employee.get_employee_id()} | "
            f"Name: {employee.get_name()} | "
            f"Department: {employee.get_department()} | "
            f"Salary: INR {employee.get_salary():,.2f}"
        )
        if show_company:
            employee.display_company_info()


# This report demonstrates map, filter, lambda, dictionary/list comprehensions, and reduce.
def print_payroll_report(employees):
    if not employees:
        print("\nNo employees are available for the report.")
        return

    # map transforms each Employee object into the name needed for this report.
    names = list(map(lambda employee: employee.get_name(), employees))
    print("\n--- Payroll and Department Report ---")
    print("Employees:", ", ".join(names))

    # A dictionary comprehension groups employees by their department using filter.
    departments = {
        employee.get_department()
        for employee in employees
    }
    employees_by_department = {
        department: list(
            filter(
                lambda employee: employee.get_department() == department,
                employees,
            )
        )
        for department in departments
    }

    # The nested dictionary stores each department's count and payroll total.
    department_summary = {
        department: {
            "count": len(department_employees),
            "payroll": reduce(
                lambda total, employee: total + employee.get_salary(),
                department_employees,
                0.0,
            ),
        }
        for department, department_employees in employees_by_department.items()
    }

    for department, details in department_summary.items():
        print(
            f"{department}: {details['count']} employee(s), "
            f"payroll INR {details['payroll']:,.2f}"
        )

    total_payroll = reduce(
        lambda total, employee: total + employee.get_salary(),
        employees,
        0.0,
    )
    print(f"Total payroll: INR {total_payroll:,.2f}")

    # A lambda provides the sorting rule: highest salary first.
    highest_paid = sorted(employees, key=lambda employee: employee.get_salary(), reverse=True)
    print_employee_list(*highest_paid[:3], title="Top Three Salaries")


def run_report_in_thread(directory):
    # Pass a snapshot to the worker so the report reads a stable list.
    employee_snapshot = directory.all_employees()
    report_thread = threading.Thread(
        target=print_payroll_report,
        args=(employee_snapshot,),
        name="payroll-report",
    )
    report_thread.start()  # Start the report on a separate thread.
    report_thread.join()  # Wait for it to finish before accepting another menu command.


# Small input helpers keep menu actions readable and report invalid input clearly.
def parse_salary(raw_salary):
    try:
        salary = float(raw_salary)
    except ValueError as error:
        raise ValueError("Enter a valid number for salary.") from error

    if not Employee.is_valid_salary(salary):
        raise ValueError("Salary must be a non-negative number.")
    return salary


def read_salary():
    return parse_salary(input("Salary in INR: "))


def add_employee_from_input(directory):
    employee_id = input("Employee ID: ").strip()
    name = input("Employee name: ").strip()
    department = input("Department: ").strip()
    salary = read_salary()
    employee = directory.add_employee(employee_id, name, department, salary)
    print(f"Added {employee.get_name()} to the directory.")


# The menu connects the project features to simple text commands.
def run_directory():
    directory = EmployeeDirectory("Practice Company", "Bengaluru")

    # Starter records make it possible to explore the project before adding data.
    sample_records = [
        ("E101", "Asha", "Engineering", 72000),
        ("E102", "Ravi", "Sales", 58000),
        ("E103", "Maya", "Engineering", 81000),
    ]
    for employee_details in sample_records:
        directory.add_employee(*employee_details)  # * unpacks each tuple into the method arguments.

    while True:
        print(
            "\nEmployee Directory"
            "\n1. List employees"
            "\n2. Add employee"
            "\n3. Search by name"
            "\n4. Filter by department"
            "\n5. Update an employee"
            "\n6. Remove an employee"
            "\n7. Pin employee to top"
            "\n8. Show latest hires"
            "\n9. Run payroll report (thread demo)"
            "\n0. Exit"
        )
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                print_employee_list(
                    *directory.all_employees(),
                    title="All Employees",
                    show_company=True,
                )
            elif choice == "2":
                add_employee_from_input(directory)
            elif choice == "3":
                search_text = input("Name to search for: ").strip()
                matches = directory.search_by_name(search_text)
                print_employee_list(*matches, title="Name Search Results")
            elif choice == "4":
                department = input("Department: ").strip()
                matches = directory.filter_by_department(department)
                print_employee_list(*matches, title=f"{department} Employees")
            elif choice == "5":
                employee = directory.find_by_id(input("Employee ID to update: ").strip())
                name = input(f"New name (Enter to keep {employee.get_name()}): ").strip()
                department = input(
                    f"New department (Enter to keep {employee.get_department()}): "
                ).strip()
                salary_text = input(
                    f"New salary (Enter to keep INR {employee.get_salary():,.2f}): "
                ).strip()
                if name:
                    employee.set_name(name)
                if department:
                    employee.set_department(department)
                if salary_text:
                    employee.set_salary(parse_salary(salary_text))
                print("Employee details updated.")
            elif choice == "6":
                employee = directory.remove_employee(input("Employee ID to remove: ").strip())
                print(f"Removed {employee.get_name()}.")
            elif choice == "7":
                employee = directory.find_by_id(input("Employee ID to pin: ").strip())
                directory.pin_to_top(employee.get_employee_id())
                print(f"Pinned {employee.get_name()} to the top of the list.")
            elif choice == "8":
                print_employee_list(
                    *directory.latest_hires(),
                    title="Three Most Recently Added Employees",
                )
            elif choice == "9":
                run_report_in_thread(directory)
                print(f"Employee objects created this run: {Employee.created_count()}")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Choose one of the listed menu options.")
        except ValueError as error:
            print(f"Error: {error}")


# This guard prevents the menu from starting if this file is imported by another script.
if __name__ == "__main__":
    run_directory()
