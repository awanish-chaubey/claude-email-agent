import sqlite3
from datetime import datetime
import uuid

DB_NAME = "email_agent.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS refunds (
            id TEXT PRIMARY KEY,
            email_id TEXT,
            order_id TEXT,
            reason TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incident_tickets (
            id TEXT PRIMARY KEY,
            email_id TEXT,
            order_id TEXT,
            reason TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clarifications (
            id TEXT PRIMARY KEY,
            email_id TEXT,
            order_id TEXT,
            needed_clarity TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escalations (
            id TEXT PRIMARY KEY,
            email_id TEXT,
            order_id TEXT,
            reason TEXT,
            urgency TEXT,
            action_point TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialised.")
####### insert_refund
def insert_refund(email_id, order_id, reason):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    row_id = str(uuid.uuid4())
    created_at = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO refunds (id, email_id, order_id, reason, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (row_id, email_id, order_id, reason, created_at))

    conn.commit()
    conn.close()
    return row_id


#### insert_incident_ticket

def insert_incident_ticket(reason,email_id, order_id=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    row_id = str(uuid.uuid4())
    created_at = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO incident_tickets (id, email_id, order_id, reason, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (row_id, email_id, order_id, reason, created_at))

    conn.commit()
    conn.close()
    return row_id

#### ##############

def insert_clarification(email_id,needed_clarity,order_id=None, ):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    row_id = str(uuid.uuid4())
    created_at = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO clarifications (id, email_id, order_id, needed_clarity, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (row_id, email_id, order_id, needed_clarity, created_at))

    conn.commit()
    conn.close()
    return row_id

#### ##############

def insert_escalation(email_id,  reason, urgency, action_point, order_id=None,):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    row_id = str(uuid.uuid4())
    created_at = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO escalations (id, email_id, order_id, reason,urgency, action_point, created_at)
        VALUES (?, ?, ?, ?, ?,?,?)
    """, (row_id, email_id, order_id, reason,urgency, action_point, created_at))

    conn.commit()
    conn.close()
    return row_id

##############
if __name__ == "__main__":
    init_db()
    
    # Test insert
    test_id = insert_refund(
        email_id="test_email_001",
        order_id="4471",
        reason="Customer received wrong item"
    )
    print(f"Inserted refund with id: {test_id}")
