# import time
import manageDB as mDB
from pojos import Owner
connection = mDB.open_connection("gfg.db")
# time.sleep(2)
mDB.create_table(connection, "owners", Owner.owner_table_specs)
mDB.close(connection)
