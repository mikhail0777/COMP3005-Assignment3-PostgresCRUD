YT link:https://youtu.be/gsA8DuoumJ4

# PostgreSQL CRUD Assignment — Psycopg v3 (Windows-friendly)

## Setup (Windows CMD)

```cmd
python -m venv .venv
.\.venv\Scripts ctivate.bat
pip install -r requirements.txt
```

Create DB and table (if needed):
```cmd
psql -d school -f db\schema.sql
psql -d school -f db\seed.sql
```

Set env vars (for this CMD session):
```cmd
set PGHOST=localhost
set PGPORT=5432
set PGDATABASE=school
set PGUSER=postgres
set PGPASSWORD=your_password
```

Run the demo:
```cmd
python app.py demo
```
