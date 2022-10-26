owner_table_specs = [
    ["name", "VARCHAR(255)"],
    ["street_num", "INT"],
    ["owner_id", "INT", "NOT NULL"],
    ["str_name", "VARCHAR(255)"],
    ["zip", "INT"],
    ["PRIMARY KEY(owner_id)"]
]


class Owner:
    def __init__(self):
        self.owner_id = 0
        self.name = ""
        self.address = {"street_name": "", "street_num": 0, "zip": 0}

    @property
    def owner_id(self):
        return self.owner_id

    @property
    def name(self):
        return self.name

    @property
    def address(self):
        return self.address

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value

    @name.setter
    def name(self, value):
        self._name = value

    @address.setter
    def address(self, value):
        self._address = value

    def get_values(self):
        vals = ""
        for val in self.__dict__:
            vals += str(self.__dict__[val]) + " "
        print(vals)
