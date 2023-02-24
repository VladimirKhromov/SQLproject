# Создайте новую базу данных, содержащую таблицу Roster.
# Таблица состоит из трех полей: Name, Species и Age.
# Столбцы Name и Species должны быть текстовыми, а столбец Age должен быть целочисленным полем.

import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Roster")

create_table = """
CREATE TABLE Roster(
    Name TEXT,
    Species TEXT,
    Age INT
);"""
cursor.execute(create_table)

# Заполните созданную таблицу следующими значениями:
values = (('Benjamin Sisko', 'Human', 40),
          ('Jadzia Dax', 'Trill', 300),
          ('Kira Nerys', 'Bajoran', 29),
          )

cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)

# Обновите поле Name записи Jadzia Dax, чтобы оно содержало значение Ezri Dax

cursor.execute("UPDATE Roster SET Name=? WHERE Name=?", ('Ezri Dax', 'Jadzia Dax'))

# Выведите значения Name и Age для всех строк данных, у которых поле Species содержит значение Bajoran

result = cursor.execute("SELECT Name, Age FROM Roster WHERE Species=?", ("Bajoran",))
print(result.fetchall())

# bonus Вывод всех результатов
print("Вывод всех результатов:")
result = cursor.execute("SELECT * FROM Roster")
print(result.fetchall())