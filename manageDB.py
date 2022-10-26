import sqlite3


def open_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection


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
    cursor.close()
    print("Table", table_name, "created")


def add_values(connection, table_name, val):
    cursor = connection.cursor()
    query = "INSERT INTO {0} VALUES {1}".format(table_name, val.get_values())
    cursor.execute(query)
    cursor.close()


def close(connection):
    # close the connection
    connection.close()
    print("Connection terminated")
