import sqlite3
from db.connection import get_db_connection
from employees.models import Employees as Employee

def get_total_employees() -> int:
  connection = get_db_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT COUNT (*) FROM employees")
  total = cursor.fetchone()[0]
  connection.close()
  return total


def get_average_age()-> float:
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute("SELECT AVG(age) AS average_age FROM employees")
  row = cursor.fetchone()
  cursor.close()
  return row[0] if row else None
  
