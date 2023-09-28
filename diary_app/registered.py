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



# register_user('john_doe', 'password123')

# user = login_user('john_doe', 'password123')
#
# if user:
#     user_id, username, _ = user
#     print(f'Welcome, {username}!')
#
#     num_entries = int(input("How many entries would you like to save? "))
#     for _ in range(num_entries):
#         entry_content = input("Enter your entry: ")
#         save_entry(user_id, entry_content)
#
#     entries = get_entries(user_id)
#     print("\nYour Entries:")
#     for entry in entries:
#         entry_id, user_id, content = entry
#         print(f"Entry ID: {entry_id}, Content: {content}")
# else:
#     print("Invalid login credentials.")



# username = input("Enter your username: ")
# password = input("Enter your password: ")
#
# register_user(username, password)
#
# conn.close()
#
# conn = sqlite3.connect('user_credentials.db')
# cursor = conn.cursor()
#
# login_username = input("Enter your username for login: ")
# login_password = input("Enter your password for login: ")
#
# if check_user(login_username, login_password):
#     print("Login successful!")
# else:
#     print("Invalid login credentials.")
#
# conn.close()
