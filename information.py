from unicodedata import category

from db import get_connection

def insert_to_users(full_name,phone,password,role):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
        insert into users (full_name,phone,password,role)
        values (%s,%s,%s,%s)
    """,(full_name,phone,password,role))
    connect.commit()
    cursor.close()
def categories(name):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into categories (name)
    values (%s)
    """,(name,))



def products(name,description,price,stock,category_id):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into poducts (name,description,price,stock,category_id)
    values (%s,%s,%s,%s,%s)""",(name,description,price,stock,category_id))

def carts(carts_id):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into (carts_id)
    values (%s)
    """,(carts_id))

def cart_items(carts_id,product_id,quantity):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into (carts_id)
    values (%s)
    """,(carts_id,product_id,quantity))

def cart_items(carts_id,product_id,quantity):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into cart_items (carts_id,product_id,quantity)
    values (%s,%s,%s)
    """,(carts_id,product_id,quantity))

def orders(user_id,total_price,status):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into orders (user_id,total_price,status)
    values (%s,%s,%s)
    """,(user_id,total_price,status))

def order_items(order_id,product_id,quantity,price):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into orders (order_id,product_id,quantity,price)
    values (%s,%s,%s,%s)
    """,(order_id,product_id,quantity,price))

def payments(order_id,product_id,amount,status,paid_at):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into orders (order_id,product_id,amount,status,paid_at)
    values (%s,%s,%s,%s,%s)
    """,(order_id,product_id,amount,status,paid_at))

def reviews(product_id,user_id,rating,comment):
    connect = get_connection()
    cursor = connect.curor
    cursor.execute("""
    insert into orders (product_id,user_id,rating,comment)
    values (%s,%s,%s,%s,%s)
    """,(product_id,user_id,rating,comment))


