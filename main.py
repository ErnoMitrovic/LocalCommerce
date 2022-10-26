# import time
import manageDB as mDB
from pojos.Owner import *
connection = mDB.open_connection("gfg.db")
# time.sleep(2)
# mDB.create_table(connection, "owners", Owner.owner_table_specs)
mDB.close(connection)
owner = Owner()
owner.name = "Erno"
owner.owner_id = 1
owner.address = ["AV", 723, 15923]
owner.get_values()

