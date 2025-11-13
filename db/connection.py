import sqlite3 

DATABASE_FILE = 'employee_data.db'

def get_db_connection(db_name=DATABASE_FILE):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  
    return conn

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.executescript(open('db/schema.sql').read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()