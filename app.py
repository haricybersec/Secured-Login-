from flask import Flask
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def init_database():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return "Secure Login Project - Step 1"


if __name__ == "__main__":
    init_database()
    app.run(debug=True)
