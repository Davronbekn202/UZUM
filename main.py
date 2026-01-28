from datetime import datetime
from information import *
def insert_to_users_main():
    full_name = input("Enter full-name: ")
    phone = int(input("Enter phone: "))
    password = input("Enter password: ")
    role = input("Enter your role: ")
    insert_to_users(full_name, phone, password, role)
def categories_main():
    name = input("Enter your name: ")
    categories(name)
def products_main():
    name = input("Enter your name: ")
    description = input("Enter description: ")
    price = float(input("Enter the price: "))
    stock = int(input("Enter the stock: "))
    category_id = int(input("Enter category-id: "))
    products(name, description, price, stock, category_id)
def carts():
    carts_id = int(input("Enter your carts-id: "))
    carts(carts_id)
def cart_items_main():
    carts_id = int(input("Enter your carts-id: "))
    product_id = int(input("Enter your product-id: "))
    quantity = int(input("Enter the quantity: "))
    cart_items(carts_id, product_id, quantity)
def orders():
    user_id = int(input("Enter your user-id: "))
    total_price = float(input("Enter total price: "))
    status = input("Enter status: ")
    orders(user_id, total_price, status)
def order_items():
    order_id = int(input("Enter your order-id: "))
    product_id = int(input("Enter product-id"))
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter the price: "))
    order_items(order_id, product_id, quantity, price)
def payments():
    order_id = int(input("Enter id of order: "))
    product_id = int(input("Enter id of product: "))
    amount = float(input("Enter the amount: "))
    status = input("Enter the status: ")
    paid_at = datetime.now()
    payments(order_id, product_id, amount, status, paid_at)

def reviews():
    product_id = int(input("Enter your user-id: "))
    user_id = int(input("Enter your user-id: "))
    rating = int(input("try to rate: "))
    comment = input("Enter the comment: ")
    reviews(product_id, user_id, rating, comment)
