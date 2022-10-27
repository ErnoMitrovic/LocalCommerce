customer_table_specs = [
    ["customer_id", "INT", "NOT NULL", "AUTO_INCREMENT"],
    ["cash", "INT"],
    ["credit", "INT"],
    ["debit", "INT"],
    ["customer_name", "VARCHAR(255)"],
    ["customer_coordinates", "VARCHAR(255)"],
    ["PRIMARY KEY (customer_id)"]
]


class Customer:
    def __init__(self, cash=0, credit=0, debit=0, customer_name="", customer_coordinates=""):
        self.cash = cash
        self.credit = credit
        self.debit = debit
        self.customer_name = customer_name
        self.customer_coordinates = customer_coordinates

    @property
    def cash(self):
        return self.cash

    @property
    def credit(self):
        return self.credit

    @property
    def debit(self):
        return self.debit

    @property
    def customer_name(self):
        return self.customer_name

    @property
    def customer_coordinates(self):
        return self.customer_coordinates

    @cash.setter
    def cash(self, value):
        self._cash = value

    @credit.setter
    def credit(self, value):
        self._credit = value

    @debit.setter
    def debit(self, value):
        self._debit = value

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    @customer_coordinates.setter
    def customer_coordinates(self, value):
        self._customer_coordinates = value
