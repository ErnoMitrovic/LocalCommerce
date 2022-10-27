owner_table_specs = [
    ["name", "VARCHAR(255)"],
    ["street_num", "INT"],
    ["owner_id", "INT", "NOT NULL", "AUTO_INCREMENT"],
    ["street_name", "VARCHAR(255)"],
    ["zip", "INT"],
    ["PRIMARY KEY(owner_id)"]
]


class Owner:
    def __init__(self, name="", street_num=0, street_name="", zip_num=0):
        self.name = name
        self.street_num = street_num
        self.street_name = street_name
        self.zip = zip_num

    @property
    def name(self):
        return self.name

    @property
    def street_name(self):
        return self.street_name

    @property
    def street_num(self):
        return self.street_num

    @property
    def zip(self):
        return self.zip

    @name.setter
    def name(self, value):
        self._name = value

    @street_name.setter
    def street_name(self, value):
        self._street_name = value

    @street_num.setter
    def street_num(self, value):
        self._street_num = value

    @zip.setter
    def zip(self, value):
        self._zip = value
