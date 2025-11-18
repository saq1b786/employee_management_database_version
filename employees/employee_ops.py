import sqlite3
from db.connection import get_db_connection
from employees.models import Employees as Employee

class EmployeeOperations:

    @staticmethod
    def add_employee(employee: Employee):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employees (first_name, last_name, email, phone_number, job_title) VALUES (?, ?, ?, ?, ?)",
            (employee.first_name, employee.last_name, employee.email, employee.phone_number, employee.job_title)
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
            (employee.first_name, employee.last_name, employee.email, employee.phone_number, employee.job_title, employee.employee_id)
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


