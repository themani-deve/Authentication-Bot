import sqlite3

connection = sqlite3.connect('sqlite3.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

create_users_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER primary key AUTOINCREMENT,
        first_name TEXT,
        phone_number TEXT,
        password TEXT
    );
"""

cursor.execute('DROP TABLE IF EXISTS channels')

create_channels_table_query = """
    CREATE TABLE IF NOT EXISTS channels(
        id INTEGER primary key AUTOINCREMENT,
        channel_name TEXT,
        channel_id INTEGER
    );
"""

connection.execute(create_users_table_query)
connection.execute(create_channels_table_query)
connection.commit()
connection.close()
