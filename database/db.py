import sqlite3
from pathlib import Path

DB_PATH = Path("database/results.db")
DB_PATH.parent.mkdir(exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS benchmark_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            algorithm TEXT,
            benchmark_method TEXT,
            upper_limit INTEGER,
            num_processes INTEGER,
            execution_time REAL
        );
    """)

    conn.commit()
    conn.close()

def save_result(algorithm, benchmark, upper_limit, num_processes, execution_time):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO benchmark_results
        (algorithm, benchmark_method, upper_limit, num_processes, execution_time)
        VALUES (?, ?, ?, ?, ?);
    """, (algorithm, benchmark, upper_limit, num_processes, execution_time))

    conn.commit()
    conn.close()