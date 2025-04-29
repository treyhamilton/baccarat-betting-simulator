import sqlite3
import bcrypt
import os

DB_FILE = "users.db"

def create_users_table():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists

def login_user(username, password):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()

    if result:
        stored_password_hash = result[0]
        return bcrypt.checkpw(password.encode(), stored_password_hash.encode('utf-8'))
    else:
        return False

# --- New: Create user_sessions table ---
def create_user_sessions_table():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            session_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            input_file TEXT,
            starting_balance INTEGER,
            starting_bet INTEGER,
            final_balance REAL,
            total_profit REAL,
            win_rate TEXT,
            hands_played INTEGER,
            output_file TEXT,
            strategy_used TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

# --- New: Log a session ---
def log_user_session(
    username,
    input_file,
    starting_balance,
    starting_bet,
    final_balance,
    total_profit,
    win_rate,
    hands_played,
    output_file,
    strategy_used
):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Get the user_id from the username
    c.execute('SELECT id FROM users WHERE username = ?', (username,))
    user = c.fetchone()

    if user:
        user_id = user[0]
        c.execute('''
            INSERT INTO user_sessions (
                user_id, input_file, starting_balance, starting_bet,
                final_balance, total_profit, win_rate, hands_played,
                output_file, strategy_used
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id, input_file, starting_balance, starting_bet,
            final_balance, total_profit, win_rate, hands_played,
            output_file, strategy_used
        ))
        conn.commit()
    conn.close()

def get_user_sessions(username):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT session_date, input_file, starting_balance, starting_bet,
               final_balance, total_profit, win_rate, hands_played,
               output_file, strategy_used
        FROM user_sessions
        JOIN users ON users.id = user_sessions.user_id
        WHERE users.username = ?
        ORDER BY session_date DESC
    ''', (username,))
    rows = c.fetchall()
    conn.close()
    return rows
