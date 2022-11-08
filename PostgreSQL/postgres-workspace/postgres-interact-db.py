import psycopg2
import pandas as pd
import csv
from tabulate import tabulate

def insert_sale(conn, order_num, order_type, cust_name, 
    prod_number, prod_name, quantity, price, discount):

    order_total = quantity * price
    if discount != 0:
        order_total *= discount
    sale_data = (order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount, order_total)
    cur = conn.cursor()
    cur.execute('''INSERT INTO sales(order_num, order_type, cust_name, 
                   prod_number, prod_name, quantity, price, discount, order_total)
                   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)''', sale_data)
    conn.commit()

    cur.execute('''SELECT CUST_NAME, ORDER_TOTAL 
                   FROM sales WHERE ORDER_NUM = %s;''', (order_num,))
    rows = cur.fetchall()
    for row in rows:
        print(f"Customer Name: {row[0]}")
        print(f"Order Total: {row[1]} \n")

    

if __name__ == '__main__':
    conn = psycopg2.connect(database="finalproject",
        user="root",
        password="password",
        host="localhost",
        port="5432")
    order_num = int (input("What is the order number?\n"))
    order_type = input ("What is the order type: Retail or Wholesale?\n")
    cust_name = input ("What is the customer's name? \n")
    prod_number = input("What is the product number?\n")
    prod_name = input ("What is the product name?\n")
    quantity = float (input ("How many were bought?\n"))
    price = float(input ("What is the price of the product?\n"))
    discount = float(input ("What is the discount, if there is one?\n"))
    insert_sale(conn,order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount)
    conn.close()