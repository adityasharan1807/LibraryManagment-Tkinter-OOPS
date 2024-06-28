import sqlite3

def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        isbn TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        book_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,
        issue_date TEXT NOT NULL,
        return_date TEXT,
        fine REAL,
        FOREIGN KEY(book_id) REFERENCES books(id),
        FOREIGN KEY(member_id) REFERENCES members(id)
    )
    ''')
    
    conn.commit()
    conn.close()

init_db()
