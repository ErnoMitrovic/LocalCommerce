product_table_specs = [
    ["product_id", "INT", "NOT NULL", "AUTO_INCREMENT"],
    ["product_name", "VARCHAR(255)"],
    ["barcode", "VARCHAR(20)"],
    ["product_description", "VARCHAR(255)"],
    ["PRIMARY KEY (product_id)"]
]


class Product:
    def __init__(self, product_name="", barcode="", product_description=""):
        self.product_name = product_name
        self.barcode = barcode
        self.product_description = product_description

    @property
    def product_name(self):
        return self.product_name

    @property
    def barcode(self):
        return self.barcode

    @property
    def product_description(self):
        return self.product_description

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @barcode.setter
    def barcode(self, value):
        self._barcode = value

    @product_description.setter
    def product_description(self, value):
        self._product_description = value
