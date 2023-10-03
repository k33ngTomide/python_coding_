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
    user_conn = sqlite3.connect('diary_users_database.db')
    user_cursor = user_conn.cursor()
    user_cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    user_conn.commit()
    user_cursor.close()
    user_conn.close()


def login_user(username, password):
    login_conn = sqlite3.connect('diary_users_database.db')
    login_cursor = login_conn.cursor()
    login_cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = login_cursor.fetchone()
    login_cursor.close()
    login_conn.close()
    return user


def save_entry(user_id, title, body):
    save_conn = sqlite3.connect('diary_users_database.db')
    save_cursor = save_conn.cursor()
    save_cursor.execute('INSERT INTO entries (user_id, title, body) VALUES (?, ?, ?)',
                        (user_id, title, body))
    save_conn.commit()
    save_cursor.close()
    save_conn.close()


def get_entry(user_id, entry_id):
    one_entry_conn = sqlite3.connect('diary_users_database.db')
    one_entry_cursor = one_entry_conn.cursor()
    one_entry_cursor.execute('SELECT * FROM entries WHERE user_id=? AND entry_id=?',
                             (user_id, entry_id))
    entry = one_entry_cursor.fetchone()
    one_entry_cursor.close()
    one_entry_conn.close()
    return entry


def get_all_entries(user_id):
    entry_conn = sqlite3.connect('diary_users_database.db')
    entry_cursor = entry_conn.cursor()
    entry_cursor.execute('SELECT * FROM entries WHERE user_id=?', (user_id,))
    entries = cursor.fetchall()
    entry_cursor.close()
    entry_conn.close()
    return entries



