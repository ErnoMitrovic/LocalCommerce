# import time
import manageDB as mDB
from pojos.Owner import *


def menu():
    option = 1
    while option > 1:
        print('1. Register Commerce Owner ')
        print('2. Register Buyer ')
        print('3. Browse products ')
        print('4. Browse products ')
        print('5. Browse orders ')
        print('0. Exit ')
        option = input("Select an option: ")
        match option:
            case "1":
                owner_obj = Owner()
                owner_obj.name = input("- Insert name: ")
                owner_obj.street_num = input("- Insert street number: ")
                owner_obj.street_name = input("- Insert street name: ")
                owner_obj.zip = input("- Insert zip: ")
                mDB.add_values(owner_obj)
            case "2":
                print("You can become a Data Scientist")
            case "3":
                print("You can become a backend developer")
            case "4":
                print("You can become a Blockchain developer")
            case "5":
                print("You can become a mobile app developer")
            case "0":
                print("Thanks for visiting")
                connection.close()


connection = mDB.open_connection("local_commerce")
# time.sleep(2)
mDB.create_table(connection, "owners", owner_table_specs)
owner = Owner()
owner.name = "Cris"
owner.street_name = "JK"
owner.street_num = 31
owner.zip = 10415
mDB.add_values(connection, "owners", owner)
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM owners;")
# print(cursor.fetchall())
mDB.close(connection)
