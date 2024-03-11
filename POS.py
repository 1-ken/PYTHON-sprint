class SalesItem:
    def __init__(self, item_id, name, unit_price):
        # Constructor for SalesItem class
        self.item_id = item_id
        self.name = name
        self.unit_price = unit_price

class StandardItem(SalesItem):
    def __init__(self, item_id, name, unit_price, quantity):
        # Constructor for StandardItem class, inheriting from SalesItem
        super().__init__(item_id, name, unit_price)
        self.quantity = quantity
        self.total = 0

    def calculate_total(self):
        # Method to calculate total price for StandardItem
        self.total = self.quantity * self.unit_price

class DiscountedItem(SalesItem):
    def __init__(self, item_id, name, unit_price, discounted_percentage):
        # Constructor for DiscountedItem class, inheriting from SalesItem
        super().__init__(item_id, name, unit_price)
        self.discounted_percentage = discounted_percentage
        self.discount = 0

    def calculate_total(self):
        # Method to calculate total price for DiscountedItem, applying discount
        self.discount = self.unit_price * (self.discounted_percentage / 100)
        self.unit_price = self.unit_price - self.discount

class ServiceItem(SalesItem):
    def __init__(self, item_id, name, unit_price, hourly_rate, no_of_hours):
        # Constructor for ServiceItem class, inheriting from SalesItem
        super().__init__(item_id, name, unit_price)
        self.hourly_rate = hourly_rate
        self.total = 0
        self.no_of_hours = no_of_hours

    def calculate_total(self):
        # Method to calculate total price for ServiceItem based on hourly rate and number of hours
        self.total = self.hourly_rate * self.no_of_hours
