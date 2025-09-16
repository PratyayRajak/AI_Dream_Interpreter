import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "dream_logs.db"

def get_connection():
    """Return a connection to the SQLite DB."""
    return sqlite3.connect(DB_PATH)

def reset_db():
    """Drop and recreate dream table (for dev/debug)."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS dreams")
    conn.commit()
    conn.close()
