import sqlite3

DB_NAME = "flights.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure TEXT,
        destination TEXT,
        date TEXT,
        seat_number TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_reservation(data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data['name'], data['flight_number'], data['departure'], data['destination'], data['date'], data['seat_number']))
    conn.commit()
    conn.close()

def get_all_reservations():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_reservation(res_id, data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
      UPDATE reservations SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=? WHERE id=?
    """, (data['name'], data['flight_number'], data['departure'], data['destination'], data['date'], data['seat_number'], res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
