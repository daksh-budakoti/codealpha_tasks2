import sqlite3

def init_db():
    conn = sqlite3.connect('bus_pass.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            route TEXT,
            date TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_ticket(name, route, date, price):
    conn = sqlite3.connect('bus_pass.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tickets (name, route, date, price) VALUES (?, ?, ?, ?)
    ''', (name, route, date, price))
    conn.commit()
    conn.close()
