import sqlite3
from datetime import datetime

DB_FILE = "results.db"

def init_db():
    """Creates the database if it doesn't exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                config_name TEXT,
                success BOOLEAN,
                start_time TEXT,
                end_time TEXT,
                log_file TEXT,
                error_trace TEXT
            )
        """)
        conn.commit()

def log_run(config_name: str, success: bool, start_time: datetime, end_time: datetime, log_file: str, error_trace: list = None):
    """Logs a test run to the database."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO test_runs (config_name, success, start_time, end_time, log_file, error_trace)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (config_name, success, start_time.isoformat(), end_time.isoformat(), log_file, "\n".join(error_trace) if error_trace else None))
        conn.commit()

# Initialize DB on import
init_db()

