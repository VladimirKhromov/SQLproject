import sqlite3

create_table = """
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT    
);"""

insert_values = """
INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    42
);"""

with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()
    try:
        cursor.execute(create_table)
    except:
        pass
    cursor.execute(insert_values)
    result = cursor.execute("SELECT * FROM People")
    print(result.fetchone())
