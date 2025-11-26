import sqlite3
from db.connection import get_db_connection
from employees.models import Employee, Department, Salaries

class EmployeeOperations:

    @staticmethod
    def add_employee(employee: Employee):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employees (first_name, last_name, email, phone_number, job_title, age) VALUES (?, ?, ?, ?, ?, ?)",
            (employee._first_name, employee._last_name, employee._email, employee._phone_number, employee._job_title, employee._age)
        )
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
                job_title=row["job_title"]
            )
        return None

    @staticmethod
    def update_employee(employee: Employee):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE employees SET first_name = ?, last_name = ?, email = ?, phone_number = ?, job_title = ? WHERE employee_id = ?",
            (employee._first_name, employee._last_name, employee._email, employee._phone_number, employee._job_title, employee.get_employee_id())
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
        cursor.execute("INSERT INTO departments(department_name, location, manager_id) VALUES (?, ?, ?)", (department._department_name, department._location, department._manager_id))
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
            "UPDATE departments SET department_name = ?, location = ?, manager_id = ? WHERE department_id = ?",
            (department._department_name, department._location, department._manager_id, department._department_id)
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