import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        dbname=os.getenv("POSTGRES_DB", "app"),
        user=os.getenv("POSTGRES_USER", "app"),
        password=os.getenv("POSTGRES_PASSWORD", "app"),
    )

@app.route("/health")
def health():
    return "ok\n"

@app.route("/")
def index():
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visits ("
                "id SERIAL PRIMARY KEY, visited_at TIMESTAMP DEFAULT now())"
            )
            cur.execute("INSERT INTO visits DEFAULT VALUES")
        return f"Hello from Docker, Суринов. Visits: {get_visits(conn)}\n"
    finally:
        conn.close()

def get_visits(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT count(*) FROM visits")
        return cur.fetchone()[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0")
