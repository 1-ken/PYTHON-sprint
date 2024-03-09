class SalesItem:
    def __init__(self,item_id,name, unit_price):
        self.item_id = item_id
        self.name = name
        self.unit_price =unit_price
class StandardItem(SalesItem):
    def __init__(self, item_id, name, unit_price, quantity):
        super().__init__(item_id, name, unit_price)
        self.quantity = quantity
        self.total = 0
    def calculare_total(self):
        self.total  = self.quantity * self.unit_price
class DiscoutedItem(SalesItem):
    def __init__(self, item_id, name, unit_price,discouted_percentage):
        super().__init__(item_id, name, unit_price)
        self.discouted_percentage = discouted_percentage
        self.discount = 0
    def calculare_total(self):
        self.discount =  self.unit_price * (self.discouted_percentage /100)
        self.unit_price = self.unit_price - self.discount
class ServiceItem(SalesItem):
    def __init__(self, item_id, name, unit_price, hourly_rate, no_of_hours):
        super().__init__(item_id, name, unit_price)
        self.hourly_rate =  hourly_rate
        self.total = 0
        self.no_of_hours = no_of_hours
        
    def  calculare_total(self):
        self.total = self.hourly_rate * self.no_of_hours
        
