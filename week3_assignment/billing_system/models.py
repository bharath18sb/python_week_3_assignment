class Item:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity

class Invoice:
    def __init__(self, tax_rate=18):
        self.items = []
        self.tax_rate = tax_rate

    def add_item(self, item):
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.get_total() for item in self.items)

    def calculate_tax(self):
        return self.calculate_subtotal() * (self.tax_rate / 100)

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()
