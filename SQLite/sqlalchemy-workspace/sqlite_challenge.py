from importlib.metadata import metadata
import sqlite3
import pandas as pd
from tabulate import tabulate

# connection = sqlite3.connect('person.db')

# cursor = connection.cursor()

# users_table = """CREATE TABLE IF NOT EXISTS Users
#                  (User_id int,
#                   First_Name text,
#                   Last_Name text,
#                   Email_Address text)"""

# users_data = [(2, 'FirstName_2', 'LastName_2', 'Email_Address_2'),\
#          (3, 'FirstName_3', 'LastName_3', 'Email_Address_3'),\
#          (4, 'FirstName_4', 'LastName_4', 'Email_Address_4'),\
#          (5, 'FirstName_5', 'LastName_5', 'Email_Address_5')]
# users = ("INSERT INTO Users VALUES(1, 'FirstName_1', 'LastName_1', 'Email_Address_1')")
# cursor.executemany("INSERT INTO Users VALUES (?,?,?,?)", users_data)
# records = cursor.execute("SELECT Email_Address FROM Users").fetchall()
# print(records)


# df = pd.DataFrame(records, columns=['User ID', 'First Name', 'Last Name', 'Email Address'])
# df = pd.DataFrame(records, columns=['Email Address'])
# print(tabulate(df,headers='keys', tablefmt='psql', showindex=False))
# connection.commit()
# connection.close()

#************************************ SQLALCHEMY ******************************************* 
import sqlalchemy as db
print("\n *********************** SQLALCHEMY ********************************")
engine = db.create_engine('sqlite:///person.db')
connection = engine.connect()
metadata = db.MetaData()

people = db.Table('Users', metadata, autoload=True, autoload_with=engine)
# query = db.select([people])
# query = db.select([people.columns.First_Name, people.columns.Email_Address])
query = db.select([people.columns.First_Name, people.columns.Email_Address]).where(people.columns.First_Name == 'FirstName_1')
results_proxy = connection.execute(query).fetchall()

# df = pd.DataFrame(results_proxy, columns=['ID', 'First Name','Last Name', 'Email Address'])
df = pd.DataFrame(results_proxy, columns=['First Name','Email Address'])
# results_set = results_proxy.fetchall()
df = df.drop_duplicates()
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
