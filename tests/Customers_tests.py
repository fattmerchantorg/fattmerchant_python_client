import unittest
from ddt import ddt, unpack, data
from fattmerchant.Customer import CustomerApi

@ddt
class CustomerTests(unittest.TestCase):
    def test_creation_of_customerApi(self):
        customer = CustomerApi("None", 123, None)
        print(customer)
        


if __name__ == '__main__':
    unittest.main()