import sqlite3

DB_PATH = "crm.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            last_contact TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_pending_leads():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone FROM leads WHERE status='pending'")
    leads = cur.fetchall()
    conn.close()
    return leads

def update_lead_status(lead_id, status):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE leads SET status=? WHERE id=?", (status, lead_id))
    conn.commit()
    conn.close()
