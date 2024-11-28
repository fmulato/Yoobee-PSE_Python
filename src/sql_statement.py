# constants

DEFAULT_DB_NAME = "mydatabase"

CREATE_DB = "CREATE DATABASE IF NOT EXISTS "

CREATE_STUDENT_TABLE = """CREATE TABLE IF NOT EXISTS students (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255) NOT NULL, 
                   address VARCHAR(255), 
                   age INT);"""

INSERT_STUDENT = f"INSERT INTO students (name, address, age) VALUES (%s, %s, %s)"

UPDATE_STUDENT = f"UPDATE students SET address = %s, age = %s WHERE id = %s"

DELETE_STUDENT = f"DELETE FROM students WHERE id = %s"

FIND_STUDENT = f"SELECT name, address, age FROM students WHERE name LIKE %s"

LIST_ALL = f"SELECT id, name, address, age FROM students ORDER BY name"




