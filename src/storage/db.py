import sqlite3
from datetime import datetime
from pathlib import Path

# Database path inside storage
DB_PATH = Path(__file__).parent / "dream_logs.db"

def init_db():
    """Initialize dream table if not exists."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dreams
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  dream TEXT,
                  emotion TEXT,
                  interpretation TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_dream(dream, emotion, interpretation):
    """Save a dream entry into DB."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO dreams (dream, emotion, interpretation, timestamp) VALUES (?, ?, ?, ?)",
              (dream, emotion, interpretation, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def fetch_dreams():
    """Fetch all dream logs."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM dreams ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return rows
