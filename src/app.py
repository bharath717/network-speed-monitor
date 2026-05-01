from flask import Flask, render_template
import sqlite3
import os
from db_manager import init_db

app = Flask(__name__)

# Ensure the database and table exist before the first request starts
# This fixes the sqlite3.OperationalError you encountered
def setup_database():
    # We call the init_db function from your db_manager module
    init_db()

def get_latest_data():
    """Fetches the most recent speed test result from the database."""
    try:
        # Connect to the database file
        conn = sqlite3.connect('speed_data.db')
        cursor = conn.cursor()
        
        # Pull the last entry based on the auto-incrementing ID
        cursor.execute('SELECT * FROM network_logs ORDER BY id DESC LIMIT 1')
        data = cursor.fetchone()
        conn.close()
        return data
    except sqlite3.OperationalError:
        # If the table still doesn't exist for some reason, return None
        return None

@app.route('/')
def index():
    latest = get_latest_data()
    
    # If the database is empty or doesn't exist yet
    if latest is None:
        return """
        <html>
            <head><title>Network Monitor</title></head>
            <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
                <h1>Network Speed Monitor</h1>
                <p style="color: orange;">⚠️ No data found in the database yet.</p>
                <p>Please ensure <strong>src/main.py</strong> is running and has completed at least one test.</p>
                <button onclick="location.reload()">Refresh Page</button>
            </body>
        </html>
        """
    
    # Extract data from the database row
    # latest[1] is timestamp, [2] is download, [3] is upload, [4] is ping
    return f"""
    <html>
        <head>
            <title>Network Dashboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; }}
                .card {{ 
                    background: white; border-radius: 10px; padding: 20px; 
                    display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
                    margin-top: 50px;
                }}
                .speed {{ font-size: 2em; color: #2c3e50; }}
                .timestamp {{ color: #7f8c8d; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Live Network Status</h1>
                <p class="timestamp">Last Checked: {latest[1]}</p>
                <hr>
                <p class="speed">⬇️ Download: <strong>{latest[2]} Mbps</strong></p>
                <p class="speed">⬆️ Upload: <strong>{latest[3]} Mbps</strong></p>
                <p>Latency (Ping): {latest[4]} ms</p>
                <br>
                <button onclick="location.reload()">Refresh Data</button>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Initialize the database table before the server starts
    setup_database()
    
    # Start the Flask server
    print("Dashboard is starting at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)