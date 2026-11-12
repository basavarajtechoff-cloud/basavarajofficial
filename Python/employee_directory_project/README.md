# Employee Directory Practice Project

This is a small interactive command-line Python project based on the concepts in the practice
scripts in the parent `Python` folder. It starts with three sample employees and
lets you add, search, update, remove, and organize employee records.

## Run the project

Open a terminal in this folder and run:

```powershell
py .\employee_directory.py
```

If the `py` command is unavailable but Python is installed and on `PATH`, use:

```powershell
python .\employee_directory.py
```

If neither command works, install Python and reopen the terminal before trying
again.

## What the sections demonstrate

- **Classes and inheritance:** `Company` stores shared company information;
  `Employee` inherits it and calls `super()` in its constructor.
- **Instance, class, and static methods:** employee details belong to an object,
  `created_count()` reads a class-level value, and `is_valid_salary()` validates
  a number without needing an object.
- **Encapsulation:** employee fields use double-underscore names and are read or
  changed through getter and setter methods.
- **Lists and dictionaries:** the directory keeps an ordered employee list and
  a dictionary indexed by employee ID. It demonstrates append, insert, remove,
  pop, slicing, and dictionary lookups.
- **Functions and arguments:** helpers return values, accept regular arguments,
  and `print_employee_list` demonstrates `*args` and `**options`.
- **Comprehensions and collection functions:** list and dictionary
  comprehensions, `map`, `filter`, `lambda`, and `reduce` are used in search and
  payroll reporting.
- **Multithreading:** the payroll report runs on a separate thread; `join()`
  waits for the report to finish before the menu continues.

Comments in `employee_directory.py` explain each major section and the Python
concepts being used.
