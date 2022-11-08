import sqlalchemy as db
import pandas as pd
from tabulate import tabulate
# Creates sqlite database users-sqlalchemy.db  
engine = db.create_engine('sqlite:///users-sqlalchemy.db')
metadata = db.MetaData()
connection = engine.connect()

#********************** Create Table ***************************
# users = db.Table('Users', metadata,
#     db.Column('user_id', db.Integer, primary_key=True),
#     db.Column( 'first_name', db.Text),
#     db.Column( 'last_name', db.Text),
#     db.Column( 'email_address', db.Text))
# metadata.create_all(engine)

#********************** Insert Values ***************************
# insertion_query = users.insert().values([
#     {"first_name": "Tina", "last_name" : "Mccoy", "email_address":"tmccoyl@hplussport"},
#     {"first_name": "Joan", "last_name":"Ruiz", "email_address": "jruixma@hplussport"},
#     {"first_name": "Sara", "last_name": "Cox", "email_address": "scoxn@hplussport"},
#     {"first_name": "Jessica", "last_name": "Alvarez", "email_address":"jalvarezo@hplussport"},
#     {"first_name":"Amanda", "last_name": "Butler", "email_address": "abutlerp@hplussport"}
# ])
 #********************** Fetch and display email addresses ***************************
# connection.execute(insertion_query)
# selection_query = db.select([users.columns.email_address])
# selection_result = connection.execute(selection_query)
# print(selection_result.fetchall())

people = db.Table('Users', metadata, autoload=True, autoload_with=engine)
get_data = db.select([people])
results = connection.execute(get_data).fetchall()

df = pd.DataFrame(results, columns=['User ID', 'First Name', 'Last Name', 'Email Address'])
print(df)

print("\n", tabulate(df, headers='keys', tablefmt='psql', showindex=False))
