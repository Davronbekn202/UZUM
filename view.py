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
see_info()