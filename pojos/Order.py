order_table_specs = [
    ["order_num", "INT", "NOT NULL", "AUTO_INCREMENT"],
    ["product_id", "INT", "NOT NULL"],
    ["local_id", "INT", "NOT NULL"],
    ["customer_id", "INT", "NOT NULL"],
    ["PRIMARY KEY (order_num, product_id, local_id, customer_id)"],
    ["FOREIGN KEY (local_id) REFERENCES locals(local_id)"],
    ["FOREIGN KEY (product_id) REFERENCES products(product_id)"],
    ["FOREIGN KEY (customer_id) REFERENCES customers(customer_id)"]
]


class Order:
    def __init__(self, product_id=0, local_id=0, customer_id=0):
        self.product_id = product_id
        self.local_id = local_id
        self.customer_id = customer_id

    @property
    def product_id(self):
        return self.product_id

    @property
    def local_id(self):
        return self.local_id

    @property
    def customer_id(self):
        return self.customer_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @local_id.setter
    def local_id(self, value):
        self._local_id = value

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
