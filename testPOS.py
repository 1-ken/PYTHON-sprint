import unittest
from POS import StandardItem, DiscountedItem, ServiceItem

class TestSalesItem(unittest.TestCase):

    def test_standard_item(self):
        item = StandardItem("1001", "Product A", 10, 5)
        self.assertEqual(item.item_id, "1001")
        self.assertEqual(item.name, "Product A")
        self.assertEqual(item.unit_price, 10)
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.calculate_total(), 50)

    def test_discounted_item(self):
        item = DiscountedItem("2001", "Product B", 20, 10)
        self.assertEqual(item.item_id, "2001")
        self.assertEqual(item.name, "Product B")
        self.assertEqual(item.unit_price, 20)
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.discounted_percentage, 10)
        self.assertEqual(item.calculate_total(), 180)

    def test_service_item(self):
        item = ServiceItem("3001", "Service C", 0, 15, 2)
        self.assertEqual(item.item_id, "3001")
        self.assertEqual(item.name, "Service C")
        self.assertEqual(item.unit_price, 0)
        self.assertEqual(item.hourly_rate, 15)
        self.assertEqual(item.no_of_hours, 2)
        self.assertEqual(item.calculate_total(), 30)

if __name__ == '__main__':
    unittest.main()