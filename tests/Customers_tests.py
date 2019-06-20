import unittest
from Customer import Customer 
from ddt import ddt, unpack, data

@ddt
class CustomerTests(unittest.TestCase):
    def test_creation_of_customer(self):
        pass
        


if __name__ == '__main__':
    unittest.main()