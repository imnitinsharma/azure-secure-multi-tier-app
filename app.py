import os
import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Database path (In cloud, you will replace SQLite with managed MySQL/PostgreSQL)
DB_PATH = os.environ.get("DB_PATH", "app_database.db")

def init_db():
    """Creates the database table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize DB on startup
init_db()

@app.route('/')
def home():
    """Renders the frontend Web Interface."""
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    """API Endpoint: Fetch all users from database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, created_at FROM users')
    rows = cursor.fetchall()
    conn.close()
    
    users = [{"id": r[0], "name": r[1], "created_at": r[2]} for r in rows]
    return jsonify({"status": "success", "data": users})

@app.route('/api/users', methods=['POST'])
def add_user():
    """API Endpoint: Save a user name to database safely."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"status": "error", "message": "Name is required"}), 400

    user_name = data['name'].strip()
    
    # Secure parameterized SQL query (prevents SQL injection)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (user_name,))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": f"User '{user_name}' created!"}), 201

if __name__ == '__main__':
    # Runs web server locally for testing
    app.run(host='0.0.0.0', port=5000, debug=True)