import sqlite3

values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28),
)

with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS People")
    cursor.execute("""
                CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
                );"""
                )
    cursor.executemany("INSERT INTO People VALUES(?, ?, ?);", values)
    # Выбрать все имена и фамилии людей, возраст которых
    # превышает 30 лет
    cursor.execute(
        "SELECT FirstName, LastName FROM People WHERE Age > 30;"
    )
for row in cursor.fetchall():
    print(row)
