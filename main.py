# Shokhrukh Abdusaidov
import time

import psycopg2
import requests


# # Task 1
# db_name = 'new_db'
# password = 'Sql7575'
# host = 'localhost'
# port = 5432
# user = 'postgres'

# conn = psycopg2.connect(dbname=db_name,
#                         user=user,
#                         password=password,
#                         host=host,
#                         port=port)
#
# cur = conn.cursor()
#
#
# def create_table():
#     create_table_query = """CREATE TABLE IF NOT EXISTS Product(
#     id serial PRIMARY KEY,
#     name varchar(50) not null unique,
#     price int not null,
#     color varchar(25) not null,
#     image varchar(255) not null)"""
#     cur.execute(create_table_query)
#     conn.commit()


#create_table()

# Task 2
# def insert_data():
#     name = input("Enter Product Name: ")
#     price = input("Enter Product Price: ")
#     color = input("Enter Product Color: ")
#     image = input("Enter Product Image URL: ")
#     insert_data_query = """INSERT INTO Product(name,price,color,image) VALUES(%s,%s,%s,%s)"""
#     cur.execute(insert_data_query, (name, price, color, image))
#     conn.commit()
#     print("Product inserted successfully")
#
#
# #insert_data()
#
# def read_all():
#     select_all_query = """SELECT * FROM Product"""
#     cur.execute(select_all_query)
#     data = cur.fetchall()
#     for row in data:
#         print(row)
#
#
# # read_all()
#
#
# def update_product():
#     old_name = input("Enter Product Name: ")
#     new_name = input("Enter New Product Name: ")
#     price = input("Enter New Product Price: ")
#     color = input("Enter New Product Color: ")
#     image = input("Enter New Product Image URL: ")
#     update_product_query = """UPDATE Product SET name = %s, price = %s, color = %s, image = %s
#      WHERE name = %s"""
#     data = (new_name, price, color, image, old_name)
#     cur.execute(update_product_query, data)
#     conn.commit()
#     print("Product updated successfully")
#
#
# #update_product()
#
# def delete_product():
#     name = input("Enter Product Name: ")
#     delete_product_query = "Delete  FROM Product WHERE name = %s"
#     cur.execute(delete_product_query, (name,))
#     conn.commit()
#     print("Product deleted successfully")
#
#
# #delete_product()
#
# # Task 3
#
# import string
#
#
# class Alphabet:
#     def __init__(self):
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         letters = string.ascii_uppercase
#         if self.index >= len(letters):
#             raise StopIteration
#         else:
#             letter = letters[self.index]
#             self.index += 1
#             return letter
#
#
# # alphabet = Alphabet()
# # next(alphabet)
# # for i in alphabet:
# #     print(i)
#
# # Task 4
# import threading
#
#
# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)
#
#
# def print_letters():
#     for i in "ABCDE":
#         print(i)
#         time.sleep(1)
#
#
# # thread_number = threading.Thread(target=print_numbers)
# # thread_letter = threading.Thread(target=print_letters)
# # thread_number.start()
# # thread_letter.start()
# # thread_number.join()
# # thread_letter.join()
#
# # Task 5
#
# class Product:
#     def __init__(self,
#                  name: str,
#                  price: int,
#                  color: str,
#                  image: str):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image
#
#     def save(self):
#         insert_data_query = """INSERT INTO Product(name,price,color,image) VALUES(%s,%s,%s,%s)"""
#         cur.execute(insert_data_query, (self.name, self.price, self.color, self.image))
#         conn.commit()
#         print("Product inserted successfully")
#
#
# iphone12 = Product("Iphone 12 pro", 15000, "Gold", "https://hjegfd")


# iphone12.save()

# Task 6

# class DbConnect:
#     def __init__(self,
#                  dbname: str,
#                  user: str,
#                  password: str,
#                  host: str,
#                  port: int):
#         self.dbname = dbname
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(dbname=self.dbname,
#                                      user=self.user,
#                                      password=self.password,
#                                      host=self.host,
#                                      port=self.port)
#         self.cur = self.conn.cursor()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cur.close()
#         self.conn.close()
#         print("Database connection closed")
#
#
# with DbConnect("new_db", "postgres", "Sql7575", "localhost", 5432) as manager:
#     get_all = """select * from product"""
#     manager.cur.execute(get_all)
#     data = manager.cur.fetchall()
#     for row in data:
#         print(row)


# Task 7
url = 'https://dummyjson.com/products/'

r = requests.get(url)
conn = psycopg2.connect(dbname='new_db',
                        user='postgres',
                        password='Sql7575',
                        host='localhost',
                        port=5432)
cur = conn.cursor()

create_table_products_query = """create table products(
        id serial primary key ,
        title varchar(255) ,
        description text ,
        price int,
        discountPercentage float,
        rating float ,
        stock int,
        brand varchar(255),
        category varchar(200),
        thumbnail varchar(255)
);"""

def create_table_products():
    cur.execute(create_table_products_query)
    conn.commit()
    print("Table created successfully")

#create_table_products()

insert_into_query = """insert into products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail)

    values (%s,%s,%s,%s,%s,%s,%s,%s,%s);

"""

for product in r.json()['products']:
    cur.execute(insert_into_query, (
        product['title'], product['description'], product['price'], product['discountPercentage'], product['rating'],
        product['stock'], product['brand'], product['category'], product['thumbnail']))
    conn.commit()
    print("Products inserted successfully")
