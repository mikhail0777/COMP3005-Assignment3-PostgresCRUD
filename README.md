# COMP 3005 – Assignment 3  Mikhail Simanian
### PostgreSQL CRUD Application (Python + Psycopg v3)

This project connects a Python app to a PostgreSQL database to perform **CRUD** (Create, Read, Update, Delete) operations on a `students` table.

---

## Video
(https://youtu.be/gsA8DuoumJ4)

---

## Setup (Windows CMD)
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt

CREATE DATABASE school;
\c school
\i db/schema.sql
\i db/seed.sql


set PGHOST=localhost
set PGPORT=5432
set PGDATABASE=school
set PGUSER=postgres
set PGPASSWORD=your_password

yt video link:https://youtu.be/gsA8DuoumJ4

python app.py demo

