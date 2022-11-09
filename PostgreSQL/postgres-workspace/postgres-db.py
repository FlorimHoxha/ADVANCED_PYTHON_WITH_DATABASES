import psycopg2
import pandas as pd
import csv
from tabulate import tabulate
conn = psycopg2.connect(database="finalproject",
        user="root",
        password="password",
        host="localhost",
        port="5432")

# conn.autocommit = True
cursor = conn.cursor()

cursor.execute("SELECT * FROM sales limit 20")
data_results = cursor.fetchall()
df = pd.DataFrame(data_results, columns=['order_num','order_type','cust_name','cust_state','prod_category',
                  'prod_number','prod_name','quantity','price','discount','order_total'])
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# cursor.execute("""INSERT INTO SALES (ORDER_NUM, 
#             ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME,
#             QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
#             (1105910,'Retail', 'Syman Mapstone', 'EB521',
#             'Understanding Artificial Intelligence', 3,
#             19.5, 0, 58.5) """)
cursor.execute("SELECT CUST_NAME, ORDER_TOTAL from SALES WHERE ORDER_NUM = 1105910")
rows = cursor.fetchall()

for row in rows:
    print(f"Customer Name: {row[0]}")
    print(f"Order Total: {row[1]} \n")

# creat_query = """CREATE TABLE sales 
#                (ORDER_NUM INT PRIMARY KEY,
#                 ORDER_TYPE TEXT,
#                 CUST_NAME TEXT,
#                 CUST_STATE TEXT,
#                 PROD_CATEGORY TEXT,
#                 PROD_NUMBER TEXT,
#                 PROD_NAME TEXT,
#                 QUANTITY INT,
#                 PRICE FLOAT,
#                 DISCOUNT FLOAT,
#                 ORDER_TOTAL FLOAT);"""
# cursor.execute("DROP TABLE IF EXISTS sales")
# cursor.execute(creat_query)

# with open('red30.csv','r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     cursor.copy_from(f, 'sales', sep=',')
# sql2 = '''COPY sales
# FROM '/var/lib/postgresql/data/red30.csv'
# DELIMITER ','
# CSV HEADER;'''
# cursor.execute(sql2)

conn.commit()
conn.close()
