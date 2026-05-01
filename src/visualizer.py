import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def generate_graph():
    conn = sqlite3.connect('speed_data.db')
    df = pd.read_sql_query("SELECT * FROM network_logs", conn)
    conn.close()

    if not df.empty:
        plt.figure(figsize=(10, 5))
        plt.plot(df['timestamp'], df['download'], label='Download (Mbps)', color='blue')
        plt.plot(df['timestamp'], df['upload'], label='Upload (Mbps)', color='green')
        plt.xticks(rotation=45)
        plt.legend()
        plt.title('Network Speed Over Time')
        plt.tight_layout()
        plt.savefig('static/speed_graph.png')
        print("Graph saved to static/speed_graph.png")