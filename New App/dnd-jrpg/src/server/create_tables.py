import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# create_table = "CREATE TABLE IF NOT EXISTS levels (level_id INTEGER PRIMARY KEY, monsters text)"
# cursor.execute(create_table)

#will need more columns for hero stats
# create_table = "CREATE TABLE IF NOT EXISTS heroes (hero_id INTEGER PRIMARY KEY, CONSTRAINT fk_users FOREIGN KEY(user_id) REFERENCES users(user_id), hero_info text)"
# cursor.execute(create_table)



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