from main import *

print("""
1 - Admin
2 - User
""")
secret_key_admin = 'a102938b'
check = int(input("choose: "))
if check == 1:
    for i in range(10):
        cut = input("Enter secret-key of admins: ")
        if cut == secret_key_admin:
            print("Welcome Admin")
        else:
            print("You are not admin")
elif check == 2:
    print("""
    1 - add user
    2 - payment
    """)
    choice = int(input("choose: "))
    if choice == 1:
        insert_to_users_main()
    elif choice == 2:
        payments_main()

else:
    try:
        if type(check) == str:
            raise TypeError("type have to be int.")
        else:
            pass
    except Exception as x:
        print(x)
