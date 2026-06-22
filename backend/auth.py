import sqlite3

DB_PATH = "database/student_management.db"


def register_user(fullname, username, email, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users(fullname, username, email, password)
            VALUES (?, ?, ?, ?)
        """, (fullname, username, email, password))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def login_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user

def reset_password(username, new_password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET password=? WHERE username=?",
        (new_password, username)
    )

    conn.commit()

    updated = cursor.rowcount > 0

    conn.close()

    return updated

if __name__ == "__main__":
    print("Auth Module Loaded Successfully")

