import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('speed_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS network_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            download REAL,
            upload REAL,
            ping REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_log(download, upload, ping):
    conn = sqlite3.connect('speed_data.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO network_logs (timestamp, download, upload, ping) VALUES (?, ?, ?, ?)',
                   (timestamp, download, upload, ping))
    conn.commit()
    conn.close()
    print(f"Logged: {download} Mbps, {upload} Mbps")