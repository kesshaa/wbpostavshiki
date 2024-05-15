import csv
import sqlite3

con = sqlite3.connect('WBbase.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Client(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Postavshik(
    id integer primary key autoincrement,
    Number integer,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Tovar(
    id integer primary key autoincrement,
    Name text,
    count integer,
    idPostavshik integer references Postavshik(id),
    idClient integer references Client(id)
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Rabotnik(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Postavki(
    id integer primary key autoincrement,
    datetime text,
    count integer,
    idPostavshik integer references Postavshik(id),
    idTovar integer references Tovar(id),
    idRabotnik integer references Rabotnik(id)
    )
    ''')

with open('postavki.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['datetime'] and row['count']:
            cur.execute("INSERT INTO Postavki(datetime, count) VALUES ( ?, ?)", (row['datetime'], row['count']))

cur.execute("SELECT * FROM Client")
rows = cur.fetchall()

with open('ExpoClient.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(rows)

con.commit()
con.close()
