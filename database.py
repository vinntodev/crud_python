import sqlite3

def create_connection():
    conn = sqlite3.connect("data.db", check_same_thread=False)
    return conn

def create_table():
    conn = create_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT,email TEXT, address TEXT)''')
    conn.commit()

def insert_data(name, email, address):
  conn = create_connection()
  conn.execute("INSERT INTO users (name, email, address) VALUES (?, ?, ?)", (name, email, address))
  conn.commit()

def get_all_users():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_all_user_id(user_id):
  conn = create_connection()
  cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
  result = cursor.fetchone()
  cursor.close()
  conn.close()
  return result

def update_user(user_id, name, email, address):
  conn = create_connection()
  conn.execute("UPDATE users SET name = ?, email = ?, address = ? WHERE id = ?", (name, email, address, user_id))
  conn.commit()

def delete_user(user_id):
  conn = create_connection()
  conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
  conn.commit()