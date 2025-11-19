CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    job_title VARCHAR(50) NOT NULL
);


ALTER TABLE employees ADD age INTEGER;   

CREATE TABLE IF NOT EXISTS departments(
  department_id INTEGER PRIMARY KEY AUTOINCREMENT,
  department_name VARCHAR(100) NOT NULL, 
  location VARCHAR(50) NOT NULL, 
  manager_id INTEGER, 
  FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

CREATE TABLE IF NOT EXISTS salaries(
  salary_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  employee_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  effective_date DATE NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);