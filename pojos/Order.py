order_table_specs = [
    ["order_num", "INT", "NOT NULL"],
    ["product_id", "INT", "NOT NULL"],
    ["local_id", "INT", "NOT NULL"],
    ["customer_id", "INT", "NOT NULL"],
    ["PRIMARY KEY (order_num, product_id, local_id, customer_id)"],
    ["FOREIGN KEY (local_id) REFERENCES locals(local_id)"],
    ["FOREIGN KEY (product_id) REFERENCES products(product_id)"],
    ["FOREIGN KEY (customer_id) REFERENCES customers(customer_id)"]
]


class Order:
    def __init__(self, order_num=0, product_id=0, local_id=0, customer_id=0):
        self.order_num = order_num
        self.product_id = product_id
        self.local_id = local_id
        self.customer_id = customer_id

    @property
    def order_num(self):
        return self.order_num

    @property
    def product_id(self):
        return self.product_id

    @property
    def local_id(self):
        return self.local_id

    @property
    def customer_id(self):
        return self.customer_id

    @order_num.setter
    def order_num(self, value):
        self._order_num = value

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @local_id.setter
    def local_id(self, value):
        self._local_id = value

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
