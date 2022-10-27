import mysql.connector
from mysql.connector import errorcode
from pojos import Owner, Local, Customer, Order, Product
import utils


def open_connection(db_name):
    try:
        connection = mysql.connector.connect(
            user="root",
            password="ErnoMitrovic2.718281828459045235",
            host="localhost",
            database=db_name
        )
        print("Connection started")
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def start_values(connection):
    tables_names = [
        ["owners", Owner.owner_table_specs],
        ["products", Product.product_table_specs],
        ["customers", Customer.customer_table_specs],
        ["locals", Local.local_table_specs],
        ["orders", Order.order_table_specs],
    ]
    for table_name, table_specs in tables_names:
        create_table(connection, table_name, table_specs)


def create_table(connection, table_name, field_specs):
    query = "CREATE TABLE IF NOT EXISTS " + table_name + "("
    cursor = connection.cursor()
    for fields in field_specs:
        for field in fields:
            query += field + " "
        if fields != field_specs[-1]:
            query += ", "
    query += ");"
    # print(query)
    cursor.execute(query)
    if cursor.fetchone() is None:
        print("Table", table_name, "created")
    cursor.close()


def add_values(connection, table_name, val):
    cursor = connection.cursor()
    keys = str(utils.get_values_pojo(val).keys())[11:-2].replace("'", "")
    vals = str(utils.get_values_pojo(val).values())[13:-2]
    query = "INSERT INTO {0} ({1}) VALUES ({2})".format(table_name, keys, vals)
    print(query)
    cursor.execute(query)
    connection.commit()
    cursor.close()


def show_elements(connection, table_name, elements_to_show: list, delimiters: list):
    query = "SELECT "
    if not elements_to_show:
        query += "* FROM {};".format(table_name)
    else:
        for element in elements_to_show:
            query += element
            if element is not elements_to_show[-1]:
                query += ", "
        query += " FROM {}".format(table_name)
    if delimiters:
        query += " WHERE "
        for delimiter in delimiters:
            query += delimiter
            if delimiter is not delimiters[-1]:
                query += ", "
    query += ";"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    elements = cursor.fetchall()
    cursor.close()
    return elements


def close(connection):
    # close the connection
    connection.close()
    print("Connection terminated")
