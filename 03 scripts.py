import sqlite3
from pprint import pprint

sql = """
DROP TABLE IF EXISTS People;
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    42   
);"""


with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()
    # executescript
    cursor.executescript(sql)


people_values = (
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28),
    ("Michel", "Lerris", 20),
)

with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()
    # executescript
    cursor.executescript(sql)
    cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
    result = cursor.execute("SELECT * FROM People")
    pprint(result.fetchall())
