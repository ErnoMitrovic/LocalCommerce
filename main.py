# import time
import manageDB as mDB
from pojos.Owner import *
import utils
connection = mDB.open_connection("gfg.db")
# time.sleep(2)
# mDB.create_table(connection, "owners", owner_table_specs)
owner = Owner()
owner.name = "Erno"
owner.owner_id = 1
owner.street_name = "val"
owner.street_num = 25
owner.zip = 10424
# mDB.add_values(connection, "owners", owner)
cursor = connection.cursor()
cursor.execute("SELECT * FROM owners;")
print(cursor.fetchone())
mDB.close(connection)

