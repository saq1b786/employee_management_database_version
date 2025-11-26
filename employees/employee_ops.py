import sqlite3
from db.connection import get_db_connection
from employees.models import Employee, Department, Salaries


class EmployeeOperations:

    @staticmethod
    def add_employee(employee: Employee):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO employees 
            (first_name, last_name, email, phone_number, job_title, age) 
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (employee.first_name, employee.last_name, employee.email,
             employee.phone_number, employee.job_title, employee.age)
        )
        employee.employee_id = cursor.lastrowid   # <-- IMPORTANT
        conn.commit()
        conn.close()

    @staticmethod
    def get_employee(employee_id: int) -> Employee:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Employee(
                employee_id=row["employee_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                email=row["email"],
                phone_number=row["phone_number"],
                job_title=row["job_title"],
                age=row["age"]       
            )
        return None

    @staticmethod
    def update_employee(employee: Employee):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE employees 
            SET first_name = ?, last_name = ?, email = ?, phone_number = ?, job_title = ?, age = ?
            WHERE employee_id = ?
            """,
            (employee.first_name, employee.last_name, employee.email,
             employee.phone_number, employee.job_title, employee.age,
             employee.employee_id)  
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_employee(employee_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
        conn.commit()
        conn.close()



class Department_ops:

    @staticmethod
    def add_department(department: Department):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO departments (department_name, location, manager_id) VALUES (?, ?, ?)",
            (department.department_name, department.location, department.manager_id)
        )
        department.department_id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_department(department_id: int) -> Department:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM departments WHERE department_id = ?", (department_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Department(
                department_id=row["department_id"],
                department_name=row["department_name"],
                location=row["location"],
                manager_id=row["manager_id"]
            )
        return None

    @staticmethod
    def update_department(department: Department):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE departments 
            SET department_name = ?, location = ?, manager_id = ?
            WHERE department_id = ?
            """,
            (department.department_name, department.location,
             department.manager_id, department.department_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_department(department_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM departments WHERE department_id = ?", (department_id,))
        conn.commit()
        conn.close()


class Salary_ops:

    @staticmethod
    def add_salary(salary: Salaries):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO salaries (employee_id, amount, effective_date) VALUES (?, ?, ?)",
            (salary.employee_id, salary.amount, salary.effective_date)
        )
        salary.salary_id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_salary(salary_id: int) -> Salaries:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salaries WHERE salary_id = ?", (salary_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Salaries(
                salary_id=row["salary_id"],
                employee_id=row["employee_id"],
                amount=row["amount"],
                effective_date=row["effective_date"]
            )
        return None
    
    @staticmethod
    def update_salaries(salary: Salaries):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE salaries SET employee_id = ?, amount = ?, effective_date = ? WHERE salary_id = ?", 
            (salary.employee_id, salary.amount, salary.effective_date, salary.salary_id) 
        )
        conn.commit()
        conn.close()
        
    @staticmethod
    def delete_salary(salary_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM salaries WHERE salary_id = ?", (salary_id,))
        conn.commit()
        conn.close()