# import time
import manageDB as mDB
import utils
from pojos import Customer, Local, Order, Owner, Product


def print_format(cursor_data: list) -> None:
    for el in cursor_data:
        if not None:
            print(el)


def register_data(pojo: object) -> tuple:
    print(utils.get_values_pojo(pojo).keys())
    element_to_show = input("- Insert element to show (DEF select all): ")
    elements = []
    while element_to_show:
        if element_to_show:
            elements.append(element_to_show)
        element_to_show = input("- Any other element? (empty if not): ")
    delimiter = input("- Delimiters (DEF none): ")
    delimiters = []
    while delimiter:
        if delimiter:
            delimiters.append(delimiter)
        delimiter = input("- Add delimiter (emtpy if not): ")
    return elements, delimiters


def menu(connection):
    option = 1
    while option >= 0:
        print('1. Register Commerce Owner ')
        print('2. Register Buyer ')
        print('3. Register Product ')
        print('4. Register Local ')
        print('5. Register Order ')
        print('6. Browse products ')
        print('7. Browse customers ')
        print('8. Browse orders ')
        print('9. Browse locals ')
        print('10. Browse owners ')
        print('0. Exit ')
        option = int(input("Select an option: "))
        match option:
            case 1:
                owner_obj = Owner.Owner()
                owner_obj.name = input("- Insert name: ")
                owner_obj.street_num = input("- Insert street number: ")
                owner_obj.street_name = input("- Insert street name: ")
                owner_obj.zip = input("- Insert zip: ")
                mDB.add_values(connection, "owners", owner_obj)
            case 2:
                customer_obj = Customer.Customer()
                customer_obj.customer_name = input("- Insert name: ")
                customer_obj.cash = input("- Insert cash: ")
                customer_obj.credit = input("- Insert credit: ")
                customer_obj.debit = input("- Insert debit: ")
                customer_obj.customer_coordinates = input("- Insert coordinates: ")
                mDB.add_values(connection, "customers", customer_obj)
            case 3:
                product_obj = Product.Product()
                product_obj.product_name = input("- Insert name: ")
                product_obj.product_description = input("- Insert product description: ")
                product_obj.barcode = input("- Insert barcode: ")
                mDB.add_values(connection, "products", product_obj)
            case 4:
                owner_ids = mDB.show_elements(connection, "owners", ["owner_id", "name"])
                product_ids = mDB.show_elements(connection, "products", ["product_id", "product_name"])
                if owner_ids is None or product_ids is None:
                    print("CANNOT ADD LOCAL, NO DATA")
                else:
                    print(owner_ids)
                    print(product_ids)
                    local_obj = Local.Local()
                    local_obj.local_name = input("- Insert local name: ")
                    local_obj.local_coordinates = input("- Insert coordinates: ")
                    local_obj.local_address = input("- Insert address: ")
                    local_obj.number_employees = int(input("- Insert number of employees: "))
                    local_obj.product_id = int(input("- Insert product ID: "))
                    local_obj.owner_id = int(input("- Insert owner ID: "))
                    mDB.add_values(connection, "locals", local_obj)
            case 5:
                product_ids = mDB.show_elements(connection, "products", ["product_id", "product_name"])
                local_ids = mDB.show_elements(connection, "locals", ["local_id", "local_name"])
                customers_ids = mDB.show_elements(connection, "customers", ["customer_id", "customer_name"])
                if local_ids is None or product_ids is None or customers_ids is None:
                    print("CANNOT ADD LOCAL, NO DATA")
                else:
                    print(local_ids)
                    print(product_ids)
                    print(customers_ids)
                    order_obj = Order.Order()
                    order_obj.local_id = int(input("- Insert local id: "))
                    order_obj.product_id = int(input("- Insert product id: "))
                    order_obj.customer_id = int(input("- Insert customer id: "))
                    mDB.add_values(connection, "orders", order_obj)
            case 6:
                elements, delimiters = register_data(Product.Product())
                print_format(mDB.show_elements(connection, "products", elements, delimiters))
            case 7:
                elements, delimiters = register_data(Customer.Customer())
                print_format(mDB.show_elements(connection, "customers", elements, delimiters))
            case 8:
                elements, delimiters = register_data(Order.Order())
                print_format(mDB.show_elements(connection, "orders", elements, delimiters))
            case 9:
                elements, delimiters = register_data(Local.Local())
                print_format(mDB.show_elements(connection, "locals", elements, delimiters))
            case 10:
                elements, delimiters = register_data(Owner.Owner())
                print_format(mDB.show_elements(connection, "owners", elements, delimiters))
            case 0:
                print("Thanks for visiting")
                connection.close()
                option = -1


def main():
    connection = mDB.open_connection("local_commerce")
    mDB.start_values(connection)
    menu(connection)
    # time.sleep(2)
    # mDB.create_table(connection, "owners", owner_table_specs)
    # owner = Owner()
    # owner.name = "Cris"
    # owner.street_name = "JK"
    # owner.street_num = 31
    # owner.zip = 10415
    # mDB.add_values(connection, "owners", owner)
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM owners;")
    # print(cursor.fetchall())


if __name__ == "__main__":
    main()
