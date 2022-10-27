local_table_specs = [
    ["local_id", "INT", "NOT NULL", "AUTO_INCREMENT"],
    ["local_name", "VARCHAR(255)"],
    ["local_address", "VARCHAR(255)"],
    ["number_employees", "INT"],
    ["local_coordinates", "VARCHAR(255)"],
    ["owner_id", "INT", "NOT NULL"],
    ["product_id", "INT", "NOT NULL"],
    ["PRIMARY KEY (local_id, owner_id, product_id)"],
    ["FOREIGN KEY (owner_id) REFERENCES owners(owner_id)"],
    ["FOREIGN KEY (product_id) REFERENCES products(product_id)"]
]


class Local:
    def __init__(self, local_name="", local_address="", number_employees=0, local_coordinates=""):
        self.local_name = local_name
        self.local_address = local_address
        self.number_employees = number_employees
        self.local_coordinates = local_coordinates
        self.owner_id = 0
        self.product_id = 0

    @property
    def local_name(self):
        return self.local_name

    @property
    def local_address(self):
        return self.local_address

    @property
    def number_employees(self):
        return self.number_employees

    @property
    def local_coordinates(self):
        return self.local_coordinates

    @property
    def owner_id(self):
        return self.owner_id

    @property
    def product_id(self):
        return self.product_id

    @local_name.setter
    def local_name(self, value):
        self._local_name = value

    @local_address.setter
    def local_address(self, value):
        self._local_address = value

    @number_employees.setter
    def number_employees(self, value):
        self._number_employees = value

    @local_coordinates.setter
    def local_coordinates(self, value):
        self._local_coordinates = value

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
