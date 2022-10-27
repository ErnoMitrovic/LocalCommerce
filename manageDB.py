import sqlite3
import utils


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
    keys = str(utils.get_values_pojo(val).keys())[11:-2].replace("'", "")
    vals = str(utils.get_values_pojo(val).values())[13:-2]
    query = "INSERT INTO {0} ({1}) VALUES ({2})".format(table_name, keys, vals)
    print(query)
    cursor.execute(query)
    connection.commit()
    cursor.close()


def close(connection):
    # close the connection
    connection.close()
    print("Connection terminated")
