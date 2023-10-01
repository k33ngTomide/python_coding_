import sqlite3

conn = sqlite3.connect('diary_users_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT,
        body TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

conn.commit()
cursor.close()
conn.close()


def register_user(username, password):
    conn = sqlite3.connect('users_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    cursor.close()
    conn.close()


def login_user(username, password):
    conn = sqlite3.connect('users_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def save_entry(user_id, title, body):
    conn = sqlite3.connect('users_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (user_id, title, body) VALUES (?, ?, ?)', (user_id, title, body))
    conn.commit()
    cursor.close()
    conn.close()


def get_entries(user_id):
    conn = sqlite3.connect('users_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries WHERE user_id=?', (user_id,))
    entries = cursor.fetchall()
    cursor.close()
    conn.close()
    return entries
