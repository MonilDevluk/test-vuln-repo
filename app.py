import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()
# trigger
# patch test
# retry
# gemini test
# new key test
# groq test
# groq test
# model fix
# sandbox test
# db test
