from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_latest_data():
    conn = sqlite3.connect('speed_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM network_logs ORDER BY id DESC LIMIT 1')
    data = cursor.fetchone()
    conn.close()
    return data

@app.route('/')
def index():
    latest = get_latest_data()
    return f"<h1>Latest Speed Test</h1><p>Download: {latest[2]} Mbps</p><p>Upload: {latest[3]} Mbps</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)