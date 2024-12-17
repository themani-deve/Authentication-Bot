import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER primary key AUTOINCREMENT,
        first_name TEXT,
        phone_number TEXT,
        password TEXT
    );
"""

connection.execute(create_table_query)
connection.commit()
connection.close()
