import sqlite3

connection = sqlite3.connect('data.db')
connection.execute("PRAGMA foreign_keys = 1")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username text UNIQUE, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS levels (level_id INTEGER PRIMARY KEY, monsters text)"
cursor.execute(create_table)

# will need more columns for hero stats
create_table = "CREATE TABLE IF NOT EXISTS heroes (hero_id INTEGER PRIMARY KEY, username text, heroname text, atk REAL, hp REAL, max_hp REAL, sprite BLOB, FOREIGN KEY (username) REFERENCES USERS (username))"
# create_table = "CREATE TABLE IF NOT EXISTS heroes (hero_id INTEGER PRIMARY KEY, hero_info text)"
cursor.execute(create_table)
connection.commit



# CREATE TABLE departments
# ( department_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   department_name VARCHAR
# );

# CREATE TABLE employees
# ( employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   last_name VARCHAR NOT NULL,
#   first_name VARCHAR,
#   department_id INTEGER,
#   CONSTRAINT fk_departments
#     FOREIGN KEY (department_id)
#     REFERENCES departments(department_id)
# );