from platform import release
import sqlite3


connection = sqlite3.connect('person.db')

# cursor = connection.cursor()

# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")
# cursor.execute("SELECT * FROM Movies")
# famousFilms = [('Puplp Fiction', 'Quinton Tarantino', 1994), ('Back to the Future', 'Steven Spielberg', 1985),\
#                 ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany("INSERT INTO Movies VALUES (?,?,?)", famousFilms)
# records = cursor.execute("SELECT * FROM Movies")

# print(cursor.fetchall())

# for record in records:
#     print(record)
# release_year = (1985,)
# cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
# print(cursor.fetchall())
connection.commit()
connection.close()
