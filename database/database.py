import sqlite3

conn = sqlite3.connect("database/student_management.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    fullname TEXT,
    gender TEXT,
    dob TEXT,
    email TEXT,
    phone TEXT,
    course TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id TEXT,
    course_name TEXT,
    duration TEXT
)
""")

conn.commit()

print("Database and Tables Created Successfully!")

conn.close()

