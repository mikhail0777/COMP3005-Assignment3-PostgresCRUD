
"""
app.py (Psycopg v3)
PostgreSQL CRUD demo using psycopg (v3).
"""
import os
import sys
from psycopg import connect, errors, OperationalError

def get_connection():
    try:
        conn = connect(
            host=os.getenv("PGHOST", "localhost"),
            port=int(os.getenv("PGPORT", "5432")),
            dbname=os.getenv("PGDATABASE", "postgres"),
            user=os.getenv("PGUSER", "postgres"),
            password=os.getenv("PGPASSWORD", ""),
        )
        conn.autocommit = True
        return conn
    except OperationalError as e:
        print(f"[Connection Error] {e}")
        sys.exit(1)

def getAllStudents():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students ORDER BY student_id;")
            rows = cur.fetchall()
            result = [
                {
                    "student_id": r[0],
                    "first_name": r[1],
                    "last_name": r[2],
                    "email": r[3],
                    "enrollment_date": r[4].isoformat() if r[4] else None,
                }
                for r in rows
            ]
            return result
    finally:
        conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                RETURNING student_id;
                """,
                (first_name, last_name, email, enrollment_date),
            )
            new_id = cur.fetchone()[0]
            return new_id
    except errors.UniqueViolation:
        print("[Insert Error] Email must be unique. That email already exists.")
        raise
    finally:
        conn.close()

def updateStudentEmail(student_id, new_email):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE students
                SET email = %s
                WHERE student_id = %s;
                """,
                (new_email, student_id),
            )
            return cur.rowcount
    finally:
        conn.close()

def deleteStudent(student_id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
            return cur.rowcount
    finally:
        conn.close()

def demo():
    print("=== Initial rows ===")
    print(getAllStudents())

    print("\n=== Adding a new student ===")
    sid = addStudent("Alice", "Wonder", "alice.wonder@example.com", "2023-09-03")
    print(f"Inserted student_id={sid}")
    print(getAllStudents())

    print("\n=== Updating student email ===")
    updated = updateStudentEmail(sid, "alice.w@example.com")
    print(f"Rows updated: {updated}")
    print(getAllStudents())

    print("\n=== Deleting the student ===")
    deleted = deleteStudent(sid)
    print(f"Rows deleted: {deleted}")
    print(getAllStudents())

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        print("Usage: python app.py demo  # runs the CRUD demo")
