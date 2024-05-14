import sqlite3

conn = sqlite3.connect('xxxxxx.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS medicine (id INT, name TEXT, date INT, value INT)')
cursor.execute('''INSERT INTO medicine (id, name, date, value)VALUES (0, 'KUPEN', 2021, 55500)''')
cursor.execute('''INSERT INTO medicine (id, name, date, value)VALUES (1, 'Vazelin', 2030, 9500)''')
cursor.execute('''INSERT INTO medicine (id, name, date, value)VALUES (2, 'FANIGAN', 5040, 7000000)''')



