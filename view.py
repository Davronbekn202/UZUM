from db import *

def see_info():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
    select * from users
    """)
    user_info_fetched = cursor.fetchall()
    for i in user_info_fetched:
        print(i)

def make_view():
    connect = get_connection()
    cursor = connect.cursor()   # 👈 parentheses matter

    cursor.execute("""
        CREATE VIEW as_use AS
        SELECT
            u.id,
            u.full_name,
            o.total_price
        FROM users u
        INNER JOIN orders o
            ON u.id = o.user_id;
    """)

    connect.commit()
    cursor.close()
    connect.close()
    print("as_use created")


see_info()