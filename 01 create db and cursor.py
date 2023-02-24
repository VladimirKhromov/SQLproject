import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

queue = "Select datetime('now', 'localtime');"
result = cursor.execute(queue)
print(result.fetchone()[0])

connection.close()

# with Context Manager

with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()
    queue = "Select datetime('now', 'localtime');"
    result = cursor.execute(queue)
    print(result.fetchone()[0])
